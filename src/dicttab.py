#!/usr/bin/env python3.7
# dicttab.py
"""GUI's Dictionary Tab module."""

# stand lib
import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import Menu

# custom
from constants import DICT_NAME
from dictutil import *


class DictionaryTab():
    """Creates the Dictionary Tab in the GUI. Returns None."""
    def __init__(self, tab_control):
        self.dictionary_tab = ttk.Frame(tab_control)
        tab_control.add(self.dictionary_tab, text='Dictionaries')
        tab_control.grid()
        self.center_box = ttk.LabelFrame(self.dictionary_tab)
        self.center_box.grid(column=0, row=0, padx=6, pady=6)
        current_dictionary = ttk.Label(self.center_box,
                                       text="Dictionary: " + DICT_NAME)
        current_dictionary.grid(column=0, row=0, padx=6, pady=6)

        self.draw_entry_box()
        self.draw_results()
        self.entry = {}
        self.key_edits = []
        self.request.focus()
        self.value_edits = []

        self.new_dict_box = ttk.LabelFrame(self.dictionary_tab)
        self.new_dict_box.grid(column=1, row=0, padx=6, pady=6, sticky=tk.N)

    def draw_entry_box(self) -> None:
        """Draws entry box in the GUI. Returns None."""
        request_box = ttk.LabelFrame(self.center_box,
                                     text="Get entry information")
        request_box.grid(column=0, row=2, padx=6, pady=6)

        self.request = ttk.Entry(request_box)
        self.request.grid(column=0, columnspan=2, row=0, padx=6, pady=6)

        request_button = ttk.Button(request_box, text="Display Entry",
                                    command=self.draw_entry)
        request_button.grid(column=0, row=1, padx=6, pady=6)
        return None

    def draw_entry(self) -> None:
        """Draws the entry to the GUI. Returns None."""
        self.reset_frame()
        self.load_entry()
        self.draw_results()
        self.show_entry()
        return None

    def load_entry(self) -> None:
        """Loads entry within class for displaying. Returns None."""
        word = self.request.get()
        self.entry = get_entry(word.strip())
        return None

    def draw_results(self) -> None:
        """Draws the 'Results' frame to the GUI. Returns None."""
        self.word_results = ttk.LabelFrame(self.center_box, text="Results")
        self.word_results.grid(column=0, row=3, padx=6, pady=6)
        return None

    def reset_frame(self) -> None:
        """Removes the word entry from the GUI. Returns None."""
        self.word_results.grid_forget()
        return None

    def show_entry(self) -> None:
        """Shows the entire entry on the GUI. Returns None."""
        counter = 0
        try:
            for key, value in self.entry.items():
                self.draw_key_value(key, value, counter)
                counter = counter + 1
        except AttributeError:
            self.draw_key_value(self.entry, NOT_FOUND, counter)
        return None

    def add_key(self, key: str, row_counter: int) -> None:
        """Makes the dictionary-entry-key into an Entry widget object.
        Returns None."""
        key_object = ttk.Label(self.word_results, text=key)
        key_object.grid(column=0, row=row_counter, padx=6, pady=6,
                        sticky=tk.W)
        self.key_edits.append(key)
        return None

    def add_value(self, value: str, row_counter: int) -> None:
        """Makes dictionary-entry-value into an Entry widget object.
        Returns None."""
        value_object = ttk.Entry(self.word_results)
        value_object.grid(column=1, row=row_counter, padx=6, pady=6,
                          sticky=tk.W)
        value_object.insert(0, value)
        self.value_edits.append(value_object)
        return None

    def draw_key_value(self, key: str, value: str, counter: int) -> None:
        """Draws key-value pairs of pre-set entry in the GUI.
        Returns None."""
        dict_key = ttk.Label(self.word_results, text=key)
        dict_key.grid(column=0, row=counter, padx=6, pady=6, sticky=tk.W)
        dict_value = ttk.Label(self.word_results, text=value)
        dict_value.grid(column=1, row=counter, padx=6, pady=6, sticky=tk.W)

    def quit_(self) -> None:
        """Quits the program. Returns None."""
        win.quit()
        win.destroy()
        return None


if __name__ == '__main__':
    win = tk.Tk()
    win.title("Test of Dictionary Tab only")
    tab_control = ttk.Notebook(win)
    menu_bar = Menu(win)
    win.config(menu=menu_bar)
    dictionary_tab = DictionaryTab(tab_control)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=dictionary_tab.quit_)
    menu_bar.add_cascade(label="File", menu=file_menu)
    win.mainloop()
