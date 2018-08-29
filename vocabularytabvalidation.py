import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

def questions(questions, upper, lower):
    """Validates the amount of questions per test is within 10 and 100,
        returns Boolean."""
    if questions >= lower \
       and questions <= upper \
       and type(questions) is int:
        return True
    else:
        return False
    
def tests(tests, upper, lower):
    """Validates the amount of tests is between 1 and 50, returns Boolean."""
    if tests >= lower \
       and tests <= upper \
       and type(tests) is int:
        return True
    else:
        return False

def grade(grade, upper, lower):
    """Validates student grade level is between 1 and 3, returns Boolean."""
    if grade >= lower \
       and grade <= upper \
       and type(grade) is int:
        return True
    else:
        return False

def language(language):
    """Validates a language choice, returns Boolean."""
    if language == "english" \
        or language == "japanese" \
        or language == "english_and_japanese":
        return True
    else:
        return False

def from_(from_, upper, lower):
    """Validates a starting page, returns Boolean."""
    if from_ >= lower \
       and from_ <= upper \
       and type(from_) is int:
        return True
    else:
        return False

def until(until, upper, lower):
    """Validates an ending page, returns Boolean."""
    if until <= upper \
       and until >= lower \
       and type(until) is int:
        return True
    else:
        return False

def not_enough_words():
    """Shows message box of inusfficient word count, returns None."""
    answer = messagebox.askyesno(title = vocab_test_title, message = not_enough_vocab_words)
    return answer
    
def didnt_write_test():
    """Shows a message that the vocabulary test was not written, returns None."""
    messagebox.showinfo(title = vocab_test_title, message = no_vocab_test)
