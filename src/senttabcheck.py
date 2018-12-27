import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

validation_title = "Data Validation"
sentence_instructions = "'Input any sentence' must be greater than 0 and less than {0} characters."

def sentence_guide(length):
    """Shows a pop up window with input instructions. Returns None."""
    messagebox.showinfo(title=validation_title, 
        message=sentence_instructions.format(length))

def is_valid_input(sentence):
    """Checks user inputted valid sentence string. Returns Boolean."""
    if len(sentence) > 0 and len(sentence) <= MAXSENTLEN:
        return True
    else:
        sentence_guide(MAXSENTLEN)
        return False

