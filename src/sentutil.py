"""Utility Module for senttab.py"""
#3rd party
import pytest
from tkinter import filedialog
from tkinter import messagebox

#custom
from dictutil import *

validation_title = "Data Validation"
sentence_instructions = "'Input any sentence' must be greater than 0 and less than {0} characters."

def get_pos_func(word):
    """Returns function that will get a word list matching 
        the part of speech 'word'. Returns Function."""
    return {
        "noun"          : get_nouns,
        "pronoun"       : get_pronouns,
        "verb"          : get_verbs,
        "adjective"     : get_adjectives,
        "adverb"        : get_adverbs,
        "auxverb"       : get_auxverbs,
        "conjunction"   : get_conjunctions,
        "interjection"  : get_interjections,
        "preposition"   : get_prepositions,
        "article"       : get_articles,
    }.get(get_pos(word)) 

def different_word(word): 
    """Chooses a different word with the same part of speech. 
        Returns String."""
    temp = get_pos_func(word)()
    while word in temp:
        temp.remove(word)
    return random.choice(temp)

def is_valid_sent(sentence):
    """Checks user inputted valid sentence string. Returns Boolean."""
    if len(sentence) > 0 and len(sentence) <= MAXSENTLEN:
        return True
    else: return False


#no tests
def sentence_guide(length):
    """Shows a pop up window with input instructions. Returns None."""
    messagebox.showinfo(title=validation_title, 
        message=sentence_instructions.format(length))
