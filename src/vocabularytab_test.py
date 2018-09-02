#!/usr/bin/python3

import unittest
import tkinter as tk
from tkinter import ttk
from vocabularytab import VocabularyTab

class VocabularyTabTest(unittest.TestCase):

    win = tk.Tk()
    questions = "30"
    tests = "3"
    grade = "3"
    from_ = "3"
    until = "30"
    language = "english"

##    def setup(self):
##        tab_control = ttk.Notebook(self.win)
##        vocabulary_tab = VocabularyTab(tab_control)

    def test_is_proper_instance(self):
        tab_control = ttk.Notebook(self.win)
        vocabulary_tab = VocabularyTab(tab_control)
        self.assertIsInstance(vocabulary_tab, VocabularyTab)

           
  
    
        

if __name__ == "__main__":
    unittest.main()
    
        



