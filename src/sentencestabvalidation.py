import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

validation_title = "Data Validation"
sentence_instructions = "'Input any sentence' must be greater than 0 and less than {0} characters."

def show_valid_input_instructions(length):
    """Shows a pop up window with input instructions. Returns None."""
    messagebox.showinfo(title = validation_title, message = sentence_instructions.format(length))

def sentence_input(sentence, length):
    """Checks for valid user input. Returns Boolean."""
    if len(sentence) > 0 and len(sentence) <= length:
        return True
    else:
        show_valid_input_instructions(length)
        return False
