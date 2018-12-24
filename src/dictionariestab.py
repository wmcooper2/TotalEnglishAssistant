#!/usr/bin/python3

#stand lib
import collections
import os
from pathlib import Path
import pprint
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog

#custom
from dictionaries import *
import directories

class DictionaryTab():
    """Creates the Dictionary Tab in the GUI. Returns None."""
    entry = ""
    value_edits = []
    key_edits = []
        
    def __init__(self, tab_control):
        """Draws the widgets to the Dictionary tab. Returns None."""
        self.dictionary_tab = ttk.Frame(tab_control)
        tab_control.add(self.dictionary_tab, text='Dictionaries')
        tab_control.grid()
        self.center_box = ttk.LabelFrame(self.dictionary_tab)
        self.center_box.grid(column=0, row=0, padx=6, pady=6)
        current_dictionary = ttk.Label(self.center_box, 
            text="Current dictionary: " + DICTNAME)
        current_dictionary.grid(column=0, row=0, padx=6, pady=6, 
            sticky=tk.W) 

        self.draw_entry_box()
        self.draw_results()
        self.request.focus()

        self.new_dict_box = ttk.LabelFrame(self.dictionary_tab)
        self.new_dict_box.grid(column=1, row=0, padx=6, pady=6, sticky=tk.N)

    def draw_entry_box(self):
        """Draws the entry box and buttons to the GUI. Returns None."""
        request_box = ttk.LabelFrame(self.center_box, 
            text="Get entry information")
        request_box.grid(column=0, row=2, padx=6, pady=6)

        self.request = ttk.Entry(request_box)
        self.request.grid(column=0, columnspan=2, row=0, padx=6, pady=6)

        request_button = ttk.Button(request_box, text="Display Entry", 
            command=self.draw_entry)
        request_button.grid(column=0, row=1, padx=6, pady=6)

    def draw_entry(self):
        """Draws/Redraws the entry to the GUI. Returns None."""
        self.reset_frame()
        self.load_entry()
        self.draw_results()
        self.show_entry()

    def load_entry(self):
        """Loads the entry within the class for displaying. Returns None."""
        word = self.request.get()
        self.entry = get_entry(word.strip())

    def draw_results(self):
        """Draws the 'Results' frame to the GUI. Returns None."""
        self.word_results = ttk.LabelFrame(self.center_box, text="Results") 
        self.word_results.grid(column=0, row=3, padx=6, pady=6, sticky=tk.W)

    def reset_frame(self):
        """Removes the word entry from the GUI. Returns None."""
        self.word_results.grid_forget()

    def show_entry(self):
        """Shows the entire entry on the GUI. Returns None."""
        counter = 0        
        for key, value in self.entry.items():
            self.draw_key_value(key, value, counter)
            counter = counter + 1

    def add_key(self, key, row_counter):
        """Makes the dictionary-entry-key into an Entry widget object.
        Returns None."""
        key_object = ttk.Label(self.word_results, text=key)
        key_object.grid(column=0, row=row_counter, padx=6, pady=6, 
            sticky=tk.W)
        self.key_edits.append(key)
        
    def add_value(self, value, row_counter):
        """Makes the dictionary-entry-value into an Entry widget object.
        Returns None."""
        value_object = ttk.Entry(self.word_results)
        value_object.grid(column=1, row=row_counter, padx=6, pady=6, 
            sticky=tk.W)
        value_object.insert(0, value)
        self.value_edits.append(value_object)

    def draw_key_value(self, key, value, counter):
        """Draws the key value pairs of the pre-set entry to the GUI.
        Returns None."""
        dict_key = ttk.Label(self.word_results, text=key)
        dict_key.grid(column=0, row=counter, padx=6, pady=6, sticky=tk.W)
        dict_value = ttk.Label(self.word_results, text=value)
        dict_value.grid(column=1, row=counter, padx=6, pady=6, sticky=tk.W)

    def quit_(self):
        """Quits the program. Returns None."""
        win.quit()
        win.destroy()

if __name__ == '__main__':
    if "./data" not in sys.path:
        sys.path.append("./data")

    win = tk.Tk()
    win.title("Test of Dictionary Tab only")
    tab_control = ttk.Notebook(win)
    menu_bar = Menu(win)
    win.config(menu = menu_bar)
    dictionary_tab = DictionaryTab(tab_control)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=dictionary_tab.quit_)
    menu_bar.add_cascade(label="File", menu=file_menu)
    win.mainloop()
