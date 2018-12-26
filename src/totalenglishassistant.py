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
from sentencestab import SentenceTab
from vocabtab import VocabularyTab

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

#GUI tabs
tab_control = ttk.Notebook(win)
vocabulary_tab = VocabularyTab(tab_control)
sentence_tab = SentenceTab(tab_control)
dictionary_tab = DictionaryTab(tab_control)
#images_tab = ImagesTab(tab_control)

win.mainloop()

