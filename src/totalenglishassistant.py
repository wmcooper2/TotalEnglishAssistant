#!/usr/bin/python3
"""The Total English Assistant GUI tool."""

#stand lib
import sys
sys.path += ["./src/"]
sys.path += ["./src/data"]

import tkinter as tk
from tkinter import filedialog
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk

#custom
import directories
directories.make_dirs()

from dictionariestab import DictionaryTab
#from imagestab import ImagesTab
from programinfo import About
from sentencestab import SentenceTab
from vocabularytab import VocabularyTab

info = About()
program_info = info.show_program_info
contact_info = info.show_contact_info
program_reqs = info.show_program_reqs
dictionary_info = info.show_dictionary_info
show_license = info.show_license_info

def quit_():
    """Quits the program, returns None."""
    win.quit()
    win.destroy()

win = tk.Tk()
win.title("Total English Assistant")

menu_bar = Menu(win)
win.config(menu = menu_bar)
file_menu = Menu(menu_bar, tearoff = 0)
dictionary_menu = Menu(menu_bar, tearoff = 0)
about_menu = Menu(menu_bar, tearoff = 0)

file_menu.add_command(label = "Exit", command = quit_)
menu_bar.add_cascade(label = "Program", menu = file_menu)
menu_bar.add_cascade(label = "Dictionary", menu = dictionary_menu)
about_menu.add_command(label = "Program Information", command = program_info)
about_menu.add_command(label = "Dictionaries", command = dictionary_info)
about_menu.add_command(label = "Contact", command = contact_info)
about_menu.add_command(label = "License", command = show_license)
menu_bar.add_cascade(label = "About", menu = about_menu)

tab_control = ttk.Notebook(win)
vocabulary_tab = VocabularyTab(tab_control)
sentence_tab = SentenceTab(tab_control)
dictionary_tab = DictionaryTab(tab_control)
#images_tab = ImagesTab(tab_control)

win.mainloop()

