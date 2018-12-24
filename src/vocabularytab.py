#!/usr/bin/python3

#stand lib
import random
import time
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox

#custom
#import vocabularytabvalidation as check
from vocabularytabvalidation import *
from vocabularytest import VocabularyTest

class VocabularyTab():
    """Creates the 'Vocabulary' tab in the GUI, returns None."""
    test            = VocabularyTest()
    WIDTH           = 6
    MAX_QUESTIONS   = 100
    MIN_QUESTIONS   = 10
    MAX_TESTS       = 50
    MIN_TESTS       = 1
    MAX_GRADE       = 3
    MIN_GRADE       = 1
    MAX_PAGE        = 1000
    MIN_PAGE        = 0
    japanese        = "日本語"
    both_languages  = "English/" + japanese
    
    def __init__(self, tab_control):
        """Draws the widgets in the 'Vocabulary' tab, returns None."""
        self.vocab_tab = ttk.Frame(tab_control)
        tab_control.add(self.vocab_tab, text="Vocabulary")
        tab_control.grid()

        self.language               = tk.StringVar()
        self.amount_of_tests        = tk.IntVar()
        self.questions_per_test     = tk.IntVar()
        self.student_grade_level    = tk.IntVar()
        self.from_page              = tk.IntVar()
        self.until_page             = tk.IntVar()

        options_frame = ttk.LabelFrame(self.vocab_tab)
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

        until_page_text = ttk.Label(page_range_box, text="Until: ")
        until_page_text.grid(column=2, row=0, sticky=tk.W, padx=6, pady=6)
        self.until_page_input = ttk.Entry(page_range_box, 
            width=self.WIDTH, textvariable=self.until_page)
        self.until_page_input.grid(column=3, row=0, padx=6, pady=6)

        language_text = ttk.LabelFrame(self.vocab_tab)
        language_text.grid(column=0, row=1, columnspan=2, pady=6, padx=6)
        english_language = ttk.Radiobutton(language_text, text="English",
            value='english', variable=self.language)
        english_language.grid(column=0, row=0, pady=6, padx=6)
        japanese_language = ttk.Radiobutton(language_text, 
            text=self.japanese, value='japanese', variable=self.language)
        japanese_language.grid(column=1, row=0, pady=6, padx=6)
        english_and_japanese = ttk.Radiobutton(language_text, 
            text=self.both_languages, value='english_and_japanese', 
            variable=self.language)
        english_and_japanese.grid(column=2, row=0, pady=6, padx=6)

        how_many_box = ttk.LabelFrame(self.vocab_tab)
        how_many_box.grid(column=0, columnspan=2, row=2, padx=6, pady=6)
        
        questions_text = ttk.Label(how_many_box,
            text="How many questions per test?")
        questions_text.grid(column=0, row=0, sticky=tk.W, pady=6, padx=6)
        self.questions_per_test_input = ttk.Entry(how_many_box, 
            width=self.WIDTH, textvariable=self.questions_per_test)
        self.questions_per_test_input.grid(column=1, row=0, pady=6, padx=6,             sticky=tk.W)
        self.questions_per_test_input.focus()
        
        tests_text = ttk.Label(how_many_box, text="How many tests?")
        tests_text.grid(column=0, row=1, sticky=tk.W, pady=6, padx=6)
        self.tests_amount_input = ttk.Entry(how_many_box, width=self.WIDTH, 
            textvariable=self.amount_of_tests)
        self.tests_amount_input.grid(column=1, row=1, sticky=tk.W, 
            pady=6, padx=6)

        save_directory_box = ttk.LabelFrame(self.vocab_tab)
        save_directory_box.grid(column=0, columnspan=2, row=3, 
            padx=6, pady=6)
        save_button = ttk.Button(save_directory_box, 
            text="Make Test(s)", command=self.vocab_tests)
        save_button.grid(column=0, row=0, padx=6, pady=6)

        reset_button = ttk.Button(save_directory_box, text="Reset", 
            command=self.reset_choices)
        reset_button.grid(column=1, row=0, padx=6, pady=6)

    def is_valid_input(self):
        """Validates the user input. Returns Boolean."""
        if questions(self.questions_per_test.get(), 
           self.MAX_QUESTIONS, self.MIN_QUESTIONS) \
           and tests(self.amount_of_tests.get(), 
               self.MAX_TESTS, self.MIN_TESTS) \
           and grade(self.student_grade_level.get(), 
               self.MAX_GRADE, self.MIN_GRADE) \
           and language(self.language.get()) \
           and from_(self.from_page.get(), self.until_page.get(), 
               self.MIN_PAGE) \
           and until(self.until_page.get(), self.MAX_PAGE, 
               self.from_page.get()):
            return True
        else:
            return False

    def quit_(self):
        """Quits the program. Returns None."""
        win.quit()
        win.destroy()

    def reset_choices(self):
        """Clears the user's input from the entry widgets. Returns None."""
        self.student_grade_level_input.delete(0, "end")
        self.from_page_input.delete(0, "end")
        self.until_page_input.delete(0, "end")
        self.tests_amount_input.delete(0, "end")
        self.questions_per_test_input.delete(0, "end")

    def set_vocabulary_test_attributes(self):
        """Sets the attributes in for the vocabulary test. Returns None."""
        test = self.test
        test.test_amount = int(self.amount_of_tests.get())
        test.questions_per_test = int(self.questions_per_test.get())
        test.student_grade_level = int(self.student_grade_level.get())
        test.from_page = int(self.from_page.get())
        test.until_page = int(self.until_page.get())
        test.language_choice = self.language.get()
        test.set_vocabulary_test_words()        

    def vocab_tests(self):
        """Makes all of the vocabulary tests requested by the user.
            Returns None."""
        test = self.test
        if self.is_valid_input():
            self.set_vocabulary_test_attributes()
            test.save_test()
    
if __name__ == '__main__':
        win = tk.Tk()
        win.title("Test of Vocabulary Tab only")
        tab_control = ttk.Notebook(win)
        menu_bar = Menu(win)
        win.config(menu = menu_bar)
        vocabulary_tab = VocabularyTab(tab_control)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=vocabulary_tab.quit_)
        menu_bar.add_cascade(label="File", menu=file_menu)
        win.mainloop()
