#!/usr/bin/python3

#stand lib
from functools import partial
import logging as logger
import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import Menu

#custom
from dictionaries import Dictionary
import sentencestabvalidation as check
from words import Word

class SentenceTab():
    """Creates the 'Sentence' tab in the GUI, returns None."""
    MAX_LENGTH      = 20
    MAX_SENTENCE    = 39
    WIDTH           = 6
    words           = []
    result_labels   = []
    groups          = []
    results_dict    = {}
    results_buttons = {}
    dictionary      = Dictionary()

    def __init__(self, tab_control):
        """Draws the widgets in the 'Sentences' tab. Returns None."""
        self.sentence_tab = ttk.Frame(tab_control)
        tab_control.add(self.sentence_tab, text = "Sentences")
        tab_control.grid()
        
        self.from_page = tk.IntVar()
        self.until_page = tk.IntVar()
        self.student_grade_level = tk.IntVar()

        options_frame = ttk.LabelFrame(self.sentence_tab)
        options_frame.grid(column=0, columnspan=2, row=0, padx=6, pady=6)

        grade_box = ttk.LabelFrame(options_frame, text="Grade level")
        grade_box.grid(column=0, row=0, padx=6, pady=6)
        self.student_grade_level_input = ttk.Entry(grade_box, 
            width=self.WIDTH, textvariable=self.student_grade_level)
        self.student_grade_level_input.grid(column=0, row=0, pady=6, padx=6)

        page_range_box = ttk.LabelFrame(options_frame, text="Page range")
        page_range_box.grid(column=1, columnspan=2, row=0, padx=6, pady=6)
        from_page_text = ttk.Label(page_range_box, text="From: ")
        from_page_text.grid(column=0, row=0, padx=6, pady=6)
        self.from_page_input = ttk.Entry(page_range_box, 
            width=self.WIDTH, textvariable=self.from_page)
        self.from_page_input.grid(column=1, row=0, padx=6, pady=6)

        input_frame = ttk.LabelFrame(self.sentence_tab, 
            text="Enter any sentence")
        input_frame.grid(column=0, row=1, padx=6, pady=6)		
        self.sentence_input = ttk.Entry(input_frame, 
            width=self.MAX_SENTENCE)
        self.sentence_input.grid(column=0, row=0, columnspan=2, 
            padx=6, pady=6)
        
        check_sentence_button = ttk.Button(input_frame, text="Check", 
            command=self.results)
        check_sentence_button.grid(column=0, row=1, padx=6, pady=6)

        reset_button = ttk.Button(input_frame, text="Reset", 
            command=self.reset_choices)
        reset_button.grid(column=1, row=1, padx=6, pady=6)

        until_page_text = ttk.Label(page_range_box, text="Until: ")
        until_page_text.grid(column=2, row=0, sticky=tk.W, padx=6, pady=6)
        self.until_page_input = ttk.Entry(page_range_box, width=self.WIDTH, 
            textvariable=self.until_page)
        self.until_page_input.grid(column=3, row=0, padx=6, pady=6)

        self.draw_results_frame()

    def is_valid_input(self):
        """Validates the sentence. Returns Boolean."""
        return check.sentence_input(self.sentence_input.get(), 
                                    self.MAX_LENGTH)

    def quit_(self):
        """Quits the program. Returns None."""
        win.quit()
        win.destroy()

    def results(self):
        """Shows results of the input sentence in the GUI. Returns None."""
        self.reset_results_frame()
        self.draw_results_frame()
        self.convert_to_word_objects()
        self.make_groups() 
        self.draw_result_labels()
        self.draw_groups()

    def make_groups(self):
        """Creates a dictionary of the result labels. Returns None."""
        self.groups = []
        counter = 0
        for word in self.words:
            temp = {}
            temp["word"] = word
            if word.is_valid:
                temp["result"] = ttk.Label(self.results_frame, 
                                           text=word.english)
                temp["grade"] = ttk.Label(self.results_frame, 
                                          text=word.grade())
                temp["page"] = ttk.Label(self.results_frame, 
                                         text=word.page_number())
                temp["verb"] = ttk.Label(self.results_frame, 
                                         text=word.base_verb())
                temp["noun"] = ttk.Label(self.results_frame, 
                                         text=word.base_noun())
            else:
                temp["result"] = ttk.Label(self.results_frame, 
                                           text=word.english)
                temp["grade"] = ttk.Label(self.results_frame, text="")
                temp["page"] = ttk.Label(self.results_frame, text="")
                temp["verb"] = ttk.Label(self.results_frame, text="")
                temp["noun"] = ttk.Label(self.results_frame, text="")
            print("word's english = ", word.english)
            self.groups.append(temp)
            counter = counter + 1

    def draw_groups(self):
        """Draws the result/button groups to the GUI. Returns None."""
        counter = 1
        for group in self.groups:
            group["result"].grid(column=counter, row=0, padx=6, pady=6)
            group["grade"].grid(column=counter, row=1, padx=6, pady=6)
            group["page"].grid(column=counter, row=2, padx=6, pady=6)
            group["verb"].grid(column=counter, row=3, padx=6, pady=6)
            group["noun"].grid(column=counter, row=4, padx=6, pady=6)
            counter = counter + 1

    def draw_result_labels(self):
        """Draws the row labels for the results widget. Returns None."""
        ttk.Label(self.results_frame, text="given word:").grid(column=0, 
            row=0, padx=6, pady=6, sticky=tk.E)
        ttk.Label(self.results_frame, text="grade:").grid(column=0, 
            row=1, padx=6, pady=6, sticky=tk.E)
        ttk.Label(self.results_frame, text="page:").grid(column=0, row=2, 
            padx=6, pady=6, sticky=tk.E)
        ttk.Label(self.results_frame, text="base verb:").grid(column=0, 
            row=3, padx=6, pady=6, sticky=tk.E)
        ttk.Label(self.results_frame, text="singular noun:").grid(column=0, 
            row=4, padx=6, pady=6, sticky=tk.E)

    def reset_results_frame(self):
        """Removes the results frame from the GUI. Returns None."""
        self.results_frame.grid_forget()

    def draw_results_frame(self):
        """Draws the results frame to the GUI. Returns None."""
        self.results_frame = ttk.LabelFrame(self.sentence_tab, 
            text="Results" )
        self.results_frame.grid(column=0, row=2, padx=6, pady=6)        

    def convert_to_word_objects(self):
        """Adds words without punctuation to self.words. Returns None."""
        self.words = []
        words = []
        for element in self.sentence_input.get().split():
            word = Word(element)
            words.append(word)
        self.words = words

    def reset_choices(self):
        """Clears user's input/results from widgets. Returns None."""
        self.student_grade_level_input.delete(0, "end")
        self.from_page_input.delete(0, "end")
        self.until_page_input.delete(0, "end")
        self.sentence_input.delete(0, "end")
        self.reset_results_frame()

if __name__ == '__main__':
    win             = tk.Tk()
    win.title("Test of Sentence Tab only")
    tab_control     = ttk.Notebook(win)
    menu_bar        = Menu(win)
    win.config(menu=menu_bar)
    sentence_tab    = SentenceTab(tab_control)
    file_menu       = Menu(menu_bar, tearoff = 0)
    file_menu.add_command(label="Exit", command=sentence_tab.quit_)
    menu_bar.add_cascade(label="File", menu=file_menu)
    win.mainloop()
