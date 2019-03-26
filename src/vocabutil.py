"""Utility module for vocabtab.py"""
# stand lib
import datetime
from pathlib import Path
import random
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

# custom
from dictutil import *

validation_title = "Data Validation"
valid_input_instructions = ("Please follow these rules",
                            "when making your selections.")
not_enough_vocab_words = ( 
    "There are not enough words based on your choices.",
    "Would you like to write the test anyway?")
vocab_test_title = "Vocabulary Test"
no_vocab_test = "The vocabulary test was not written."
info_questions_per_test = (
        "'How many questions per test?'", 
        "must be an whole number between 10 and 100.")
info_amount_of_tests = (
        "'How many tests?'", 
        "must be a whole number between 1 and 50.")
info_student_grade_level = (
        "'Choose a grade level'", 
        "must be a whole number between 1 and 3.",
        "(This program was made for Junior High Schools in Japan.)")
info_language = "You need to choose a language."
info_from_page = "'From' must be a whole number greater than 0."
info_until_page = "'Until' must be a whole number less than 1000."

invalid_input_messages = [valid_input_instructions,
                         info_questions_per_test,
                         info_amount_of_tests,
                         info_student_grade_level,
                         info_language,
                         info_from_page,
                         info_until_page
                         ]
# input_instructions = "\n\n".join(invalid_input_messages)

date_time           = lambda: datetime.datetime.now().strftime('%Y_%m_%d')
grade_number        = lambda x: "Grade"+str(x)
in_question_range   = lambda num: num>=MIN_Q_PER_T and num<=MAX_Q_PER_T
in_test_range       = lambda num: num>=MIN_T_AMT and num<=MAX_T_AMT
test_num            = lambda x: "Test"+str(x+1)
pages_chosen        = lambda lo, hi: lo>=MIN_PAGE and hi<=MAX_PAGE and hi>lo


def didnt_write_test() -> None:
    """Shows a message that the vocabulary test was not written. 
    Returns None."""
    messagebox.showinfo(title=vocab_test_title, message=no_vocab_test)
    return None


def not_enough_words() -> None:
    """Shows yes/no box. Returns None."""
    messagebox.askyesno(title=vocab_test_title, 
                        message=" ".join(not_enough_vocab_words))
    return None


def test_name(num: int, std_grade: int, lang: str) -> str:
    """Formats the name of the save file. Returns String."""
    return "{0}_{1}_{2}_{3}".format(
        date_time(),
        lang.title(), 
        grade_number(std_grade),
        test_num(num))


def save_random_order(words: List[str], save_to: str) -> None:
    """Saves test to 'VocabularyTests/'. Returns None."""
    temp = words[:]
    file_path = ROOT_DIR+VOCAB_DIR+save_to
    with open(file_path, "w+", encoding = "utf-8") as f:
        for word in words:
            choice = random.choice(temp)
            f.write(choice+"\n")
            temp.remove(choice)
    return None


# how to test this, set.is_subset() of each other?
# what is test_words[:]?
def unique_words() -> None:
    """Filters out any duplicates in test_words. Returns None."""
    words_copy = test_words[:]
    temp = []
    for word in test_words:
        if word not in temp:
            temp.append(word)
    temp.sort()
    test_words = temp[:] 
    return None


def valid_lang_chosen(lang: str) -> bool: # called from where?
    """Validates a language choice was made. Returns Boolean."""
    if lang == "english" \
        or lang == "japanese" \
        or lang == "english_japanese":
        return True
    else:
        return False


def valid_q_input(amt: str) -> bool:
    """Validates user question amount input. Returns Boolean."""
    if in_question_range(amt) and type(amt) is int:
        return True
    else:
        return False


def vocabulary(have: List[str], want: int, lang: str) -> List[str]:
    """Returns List of random vocabulary words."""
    temp = []
    for i in range(want):
        try:
            choice = random.choice(have)
        except IndexError:
            break
        if lang == "english":
            temp.append(choice)
        elif lang == "japanese":
            temp.append(japanese(choice))
        elif lang == "english_japanese":
            func = random.choice([None, japanese])
            if func is not None:
                temp.append(japanese(choice))
            else: temp.append(choice)
        have.remove(choice)
    return temp
