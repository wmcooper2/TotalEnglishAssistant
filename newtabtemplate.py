#!/usr/bin/python3
import time
import random
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog
from tkinter import messagebox

class Tab():
    """A template for trying out inheritence when making new tabs for the GUI,
        returns None."""
    def __init__(self, tab_control):
        self.tab_control = tab_control
        vocabulary_tab = ttk.Frame(tab_control)
        tab_control.add(vocabulary_tab, text = "TEMPLATE")
        tab_control.grid(column = 0, row = 0, pady = 6, padx = 6)

    def quit_(self):
        """Quits the program, returns None."""
        win.quit()
        win.destroy()

if __name__ == '__main__':
        win = tk.Tk()
        win.title("TEMPLATE")
        tab_control = ttk.Notebook(win)
        menu_bar = Menu(win)
        win.config(menu=menu_bar)
        tab = Tab(tab_control)
        file_menu = Menu(menu_bar, tearoff = 0)
        file_menu.add_command(label = "Exit", command = tab.quit_)
        menu_bar.add_cascade(label = "File", menu = file_menu)
        win.mainloop()
