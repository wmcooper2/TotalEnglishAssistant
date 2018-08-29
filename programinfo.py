#!/usr/bin/python3
##import PIL as pil
from pathlib import Path
import tkinter as tk
from tkinter import ttk
import pprint
from dictionaries import Dictionary
import license 

pil_path = Path("/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/PIL/")


class About():
    """Contains information about the Total English Assistant program."""
    dictionary = Dictionary()
    
    def __init__(self):
        """Contains some basic info about the program, returns None"""
        self.PROGRAM_VERSION = "1.0"
        self.AUTHOR = "Wandal M. Cooper"
        self.PYTHON_VERSION = ">= 3.6"
        self.PIL_VERSION = "5.0.0" #got this info through the command line, set up so that it pulls from my machine automatically and will update future versions automatically when I upload to github.
        self.AUTHORS_GITHUB = "https://github.com/wmcooper2"
        self.program_info_title = "Program Info"
        
        self.height = 300
        self.width = 300

        self.python_version = "Python Version: " + self.PYTHON_VERSION
        self.pil_version = "PIL Version: " + self.PIL_VERSION
        self.program_reqs_title = "Program Requirements"
        self.program_reqs_info = "For this program to work properly, you need to have the following installed: "
        self.program_reqs_info = [self.program_reqs_info,"\n", self.python_version, self.pil_version,]
        self.program_reqs = "\n".join(self.program_reqs_info)

        self.program_version_info = "Version: " + self.PROGRAM_VERSION
        self.program_created_by = "Author: " + self.AUTHOR
        self.program_info_message = [self.program_version_info, self.program_created_by]
        self.program_info = "\n".join(self.program_info_message)

        self.dictionary_name = "Total English: Books 1, 2 and 3."
        self.grade_one_words = str(self.dictionary.filter_words_by_grade(1))
        self.grade_two_words = str(self.dictionary.filter_words_by_grade(2))
        self.grade_three_words = str(self.dictionary.filter_words_by_grade(3))
        
        self.contact_info_title = "Contact Information"
        self.contact_info_github = "Contact me through: \n" + self.AUTHORS_GITHUB
        self.contact_infos = [self.contact_info_github,]
        self.contact_info = "\n".join(self.contact_infos)

        self.license_ = license.LICENSE

    def show_program_info(self):
        """Shows version and creation date in new window, returns None."""
        self.make_new_window(self.program_info, "General Information")

    def show_contact_info(self):
        """Shows github information of program creator, returns None."""
        self.make_new_window(self.contact_info, "Contact Me Here")

    def show_program_reqs(self):
        """Shows requirements in a popup for the program to run properly,
            returns None."""
        self.make_new_window(self.program_reqs, "Program Requirements")

    def show_dictionary_info(self):
        """Shows basic dictionary stats in the GUI, returns None."""
        new_window = tk.Tk()
        new_window.title("Dictionary Statistics")
        frame = ttk.LabelFrame(new_window)
        frame.grid()

        dictionary_box = ttk.LabelFrame(frame, text = "Current dictionary")
        dictionary_box.grid(column = 0, row = 0, padx = 6, pady = 6, sticky = tk.W)

        current_dictionary = ttk.Label(dictionary_box, text = self.dictionary_name)
        current_dictionary.grid(column = 0, row = 0, padx = 6, pady = 6)
        
        total_words = ttk.Label(dictionary_box, text = "Total words: " + str(self.dictionary.size))
        total_words.grid(column = 0, row = 1, padx = 6, pady = 6, sticky = tk.W)

        unique_words = ttk.LabelFrame(frame, text = "Unique words by grade")
        unique_words.grid(column = 0, row = 2, padx = 6, pady = 6, sticky = tk.W)

        grade_one_word_total = ttk.Label(unique_words, text = "Grade 1: " + self.grade_one_words)
        grade_one_word_total.grid(column = 0, row = 0, padx = 6, pady = 6, sticky = tk.W)

        grade_one_word_total = ttk.Label(unique_words, text = "Grade 2: " + self.grade_two_words)
        grade_one_word_total.grid(column = 0, row = 1, padx = 6, pady = 6, sticky = tk.W)

        grade_one_word_total = ttk.Label(unique_words, text = "Grade 3: " + self.grade_three_words)
        grade_one_word_total.grid(column = 0, row = 2, padx = 6, pady = 6, sticky = tk.W)

    def show_license_info(self):
        """Shows the program license in a new window, returns None."""
        new_window = tk.Tk()
        new_window.title("MIT License")
        frame = ttk.LabelFrame(new_window)
        frame.grid()
        
        counter = 0
        for line in self.license_:
            ttk.Label(frame, text = line).grid(column = 0, row = counter, sticky = tk.W)
            counter = counter + 1

    def make_new_window(self, info, title):
        about = tk.Tk()
        about.title(title)
        frame = ttk.LabelFrame(about)
        frame.grid(column = 0, row = 0)
        message = ttk.Label(frame, text = info)
        message.grid(column = 0, row = 0)
    

if __name__ == "__main__":
    about = About()
    about.show_license_info()
