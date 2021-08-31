#!/usr/bin/env python3.7
# senttab.py
"""GUI's Sentence Tab."""

# stand lib
import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import Menu

# custom
from constants import SENT_WIDGET_LEN
from sentutil import get_results
from sentutil import get_results2
from words import remove_punctuation


class SentenceTab():
    """Creates the 'Sentence' tab in the GUI, returns None."""
    def __init__(self, tab_control):
        self.sentence_tab = ttk.Frame(tab_control)
        tab_control.add(self.sentence_tab, text="Sentences")
        tab_control.grid()

        self.from_page = tk.IntVar()
        self.until_page = tk.IntVar()
        self.student_grade_level = tk.IntVar()

        self.original = []
        self.no_punct_sent = []
        self.result_labels = []
        self.results_rows = []
        self.results_dict = {}

        # box 1
        input_frame = ttk.LabelFrame(self.sentence_tab,
                                     text="Enter any sentence")
        input_frame.grid(column=0, row=1, padx=6, pady=6)

        self.sent_input = ttk.Entry(input_frame,
                                    width=SENT_WIDGET_LEN)
        self.sent_input.grid(column=0, row=0, columnspan=2,
                             padx=6, pady=6)

        check_but = ttk.Button(input_frame, text="Check",
                               command=self.results)
        check_but.grid(column=0, row=1, padx=6, pady=6)

        reset_but = ttk.Button(input_frame, text="Reset",
                               command=self.reset_gui)
        reset_but.grid(column=1, row=1, padx=6, pady=6)

        # box 2 (drawn after button click)
        self.draw_res_fr()

    def results(self) -> None:
        """Shows results of input sentence in the GUI. Returns None."""
        self.reset_res_fr()
        self.draw_res_fr()
        self.original = self.sent_input.get()
        self.results_rows = get_results2(self.res_fr, self.original)
        self.draw_results_labels()
        self.draw_results_rows()
        return None

    def draw_results_rows(self) -> None:
        """Draws the result/button groups to the GUI. Returns None."""
        counter = 1
        for group in self.results_rows:
            group["given"].grid(column=counter, row=0, padx=6, pady=6)
            group["grade"].grid(column=counter, row=1, padx=6, pady=6)
            group["page"].grid(column=counter, row=2, padx=6, pady=6)
            group["verb"].grid(column=counter, row=3, padx=6, pady=6)
            group["noun"].grid(column=counter, row=4, padx=6, pady=6)
            counter = counter + 1
        return None

    def draw_results_labels(self) -> None:
        """Draws the row labels for the results widget. Returns None."""
        ttk.Label(self.res_fr,
                  text="given:").grid(column=0, row=0, padx=6, pady=6,
                                      sticky=tk.E)
        ttk.Label(self.res_fr,
                  text="grade:").grid(column=0, row=1, padx=6, pady=6,
                                      sticky=tk.E)
        ttk.Label(self.res_fr,
                  text="page:").grid(column=0, row=2, padx=6, pady=6,
                                     sticky=tk.E)
        ttk.Label(self.res_fr,
                  text="base verb:").grid(column=0, row=3, padx=6, pady=6,
                                          sticky=tk.E)
        ttk.Label(self.res_fr,
                  text="base noun:").grid(column=0, row=4, padx=6, pady=6,
                                          sticky=tk.E)
        return None

    def reset_res_fr(self) -> None:
        """Removes the results frame from the GUI. Returns None."""
        self.res_fr.grid_forget()
        return None

    def draw_res_fr(self) -> None:
        """Draws the results frame to the GUI. Returns None."""
        self.res_fr = ttk.LabelFrame(self.sentence_tab, text="Results")
        self.res_fr.grid(column=0, row=2, padx=6, pady=6)
        return None

    def break_up_no_punct_sent(self) -> None:
        """Adds no-punct words to self.user_sentence. Returns None."""
        self.no_punct_sent = []
        for word in self.sent_input.get().split(" "):
            self.no_punct_sent.append(remove_punctuation(word))
        return None

    def break_up_original_sent(self) -> None:
        """Breaks up user's sentence by spaces. Returns None."""
        self.original = []
        for word in self.sent_input.get().split(" "):
            self.original.append(word)
        return None

    def reset_gui(self) -> None:
        """Clears user's results from gui. Returns None."""
        self.sent_input.delete(0, "end")
        self.reset_res_fr()
        return None

    def quit_(self) -> None:
        """Quits the program. Returns None."""
        win.quit()
        win.destroy()
        return None


if __name__ == '__main__':
    win = tk.Tk()
    win.title("Test of Sentence Tab only")
    tab_control = ttk.Notebook(win)
    menu_bar = Menu(win)
    win.config(menu=menu_bar)
    sentence_tab = SentenceTab(tab_control)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=sentence_tab.quit_)
    menu_bar.add_cascade(label="File", menu=file_menu)
    win.mainloop()
