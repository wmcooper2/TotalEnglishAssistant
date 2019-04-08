#!/usr/bin/env python3.7
# vocabutil.py
"""Utility module for vocabtab.py"""

# stand lib
import datetime
from pathlib import Path
import random
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from typing import List
from typing import Text

# custom
from constants import VOCAB_DIR
from constants import MAX_PAGE
from constants import MAX_Q_PER_T
from constants import MAX_T_AMT
from constants import MIN_PAGE
from constants import MIN_Q_PER_T
from constants import MIN_T_AMT
from dictutil import japanese

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


def date_time() -> Text:
    """Gets timestamp. Returns String."""
    return datetime.datetime.now().strftime('%Y_%m_%d')


def grade_number(num: int) -> Text:
    """Grade number for file name. Returns String."""
    return "Grade"+str(num)


def in_question_range(num: int) -> bool:
    """Checks for proper question amount. Returns Boolean."""
    return num >= MIN_Q_PER_T and num <= MAX_Q_PER_T


def in_test_range(num: int) -> bool:
    """Checks for proper test amount. Returns Boolean."""
    return num >= MIN_T_AMT and num <= MAX_T_AMT


def test_num(num: int) -> Text:
    """Test number for file name. Returns String."""
    return "Test" + str(num + 1)


def pages_chosen():
    """Checks for proper page range. Returns Boolean."""
    return lo >= MIN_PAGE and hi <= MAX_PAGE and hi > lo


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


def test_name(num: int, std_grade: int, lang: Text) -> Text:
    """Formats the name of the save file. Returns String."""
    return "{0}_{1}_{2}_{3}".format(
        date_time(),
        lang.title(),
        grade_number(std_grade),
        test_num(num))


def save_random_order(words: List[Text], save_to: Text) -> None:
    """Saves test to 'VocabularyTests/'. Returns None."""
    temp = words[:]
    file_path = VOCAB_DIR + save_to
    with open(file_path, "w+", encoding="utf-8") as f:
        for word in words:
            choice = random.choice(temp)
            f.write(choice + "\n")
            temp.remove(choice)
    return None


def valid_lang(lang: Text) -> bool:
    """Validates a language choice was made. Returns Boolean."""
    if lang == "english" or lang == "japanese" or lang == "english_japanese":
        return True
    else:
        return False


def valid_q_input(amt: Text) -> bool:
    """Validates user question amount input. Returns Boolean."""
    if in_question_range(amt) and type(amt) is int:
        return True
    else:
        return False


def vocabulary(have: List[Text], want: int, lang: Text) -> List[Text]:
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
            else:
                temp.append(choice)
        have.remove(choice)
    return temp


def valid_grade(grade: Text) -> bool:
    """Validates user grade selection. Returns Boolean."""
    return 1 <= int(grade) and int(grade) <= 3
