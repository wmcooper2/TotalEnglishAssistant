"""Utility module for vocabtab.py"""
#stand lib
import datetime
from pathlib import Path
import random
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

#custom
from dictutil import *

validation_title = "Data Validation"
valid_input_instructions = "Please follow these rules when making your selections."
not_enough_vocab_words = "There are not enough words available within your requested parameters. Would you like to write the test anyway?"
vocab_test_title = "Vocabulary Test"
no_vocab_test = "The vocabulary test was not written."
info_message__questions_per_test = "'How many questions per test?' must be an whole number between 10 and 100."
info_message__amount_of_tests = "'How many tests? must be a whole number between 1 and 50.'"
info_message__student_grade_level = "'Choose a grade level' must be a whole number between 1 and 3. (This program was made for Junior High Schools in Japan.)"
info_message__language = "You need to choose a language."
info_message__from_page = "'From' must be a whole number greater than 0."
info_message__until_page = "'Until' must be a whole number less than 1000."

invalid_input_messages = [valid_input_instructions,
                         info_message__questions_per_test,
                         info_message__amount_of_tests,
                         info_message__student_grade_level,
                         info_message__language,
                         info_message__from_page,
                         info_message__until_page
                         ]
input_instructions = "\n\n".join(invalid_input_messages)

date_time           = lambda: datetime.datetime.now().strftime('%Y_%m_%d')
grade_number        = lambda x: "Grade"+str(x)
in_question_range   = lambda num: num>=MINQPERTEST and num<=MAXQPERTEST
in_test_range       = lambda num: num>=MINTESTAMT and num<=MAXTESTAMT
test_num            = lambda x: "Test"+str(x+1)
pages_chosen        = lambda lo, hi: lo>=MINPAGE and hi<=MAXPAGE and hi>lo

def valid_q_input(amt):
    """Validates the amount of questions per test is within 10 and 100.
        Returns Boolean."""
    if in_question_range(amt) and type(amt) is int: return True
    else: return False

def tst_amt(amt): #called from where?
    """Validates 'amt' is between 1 and 50. Returns Boolean."""
    if in_test_range(amt) and type(amt) is int: return True
    else: return False

def valid_lang_chosen(lang): #called from where?
    """Validates a language choice was made. Returns Boolean."""
    if lang == "english" \
        or lang == "japanese" \
        or lang == "english_japanese":
        return True
    else: return False

def make_file_name(num, std_grade, lang):
    """Formats the name of the save file. Returns String."""
    return "{0}_{1}_{2}_{3}".format(
        date_time(),
        lang.title(), 
        grade_number(std_grade),
        test_num(num))

#how to test this, set.is_subset() of each other?
#what is test_words[:]?
def unique_words():
    """Filters out any duplicates in test_words. Returns None."""
    words_copy = test_words[:]
    temp = []
    for word in test_words:
        if word not in temp:
            temp.append(word)
    temp.sort()
    test_words = temp[:] 

def save(words, val):
    """Saves amt of tests to '<programroot>/VocabularyTests/<testname>'.
        - val is a dictionary.
        - <testname> is incremented with amt acting as a counter.
        Returns None."""
    if val["amt"] > 0:
        for test_num in range(val["amt"]):
            file_name = make_file_name(test_num, val["grade"], val["lang"])
            write_file(file_name, words)
    else: print("make error message")

def write_file(file_name, words):
    """Writes words to file_name. Returns None."""
    vocab_copy = words[:]
    with open(ROOTDIR+VOCABDIR+file_name, "w+", encoding = "utf-8") as f:
        for word in words:
            choice = random.choice(vocab_copy)
            f.write(choice+"\n")
            vocab_copy.remove(choice)

#pop up windows
def not_enough_words():
    """Shows message box of inusfficient word count. Returns None."""
    return messagebox.askyesno(title=vocab_test_title, 
        message=not_enough_vocab_words)
    
def didnt_write_test():
    """Shows a message that the vocabulary test was not written. 
    Returns None."""
    messagebox.showinfo(title=vocab_test_title, message=no_vocab_test)
