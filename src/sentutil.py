"""Utility Module for senttab.py"""
#3rd party
import pytest
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

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
    while word in temp: temp.remove(word)
    return random.choice(temp)

def is_valid_sent(sentence):
    """Checks user inputted valid sentence string. Returns Boolean."""
    if len(sentence) > 0 and len(sentence) <= MAXSENTLEN:
        return True
    else: return False

def make_label(widget, word, func=None):
    """Assembles a ttk Label widget. Returns ttk Label Widget."""
    if func != None:    return ttk.Label(widget, text=func(word))
    else:               return ttk.Label(widget, text=word)

def get_results(widget, sent):
    """Creates a dictionary of the result labels. Returns List."""
    rows = []
    counter = 0

    for word in list(map(remove_punctuation, sent.split())):
        temp = {}
        base = None
        temp["word"] = word
#        print("base verb::", base_verb(word))
#        print("base noun::", base_noun(word))
        base = temp["word"]    
        if base_verb(word) != " ":          base = base_verb(word)
        elif base_noun(word) != " ":
            if not is_proper_noun(word):    base = base_noun(word.lower())
            else:                           base = base_noun(word)
        else: base = word

        if is_valid(base): 
            temp["result"]  = make_label(widget, base)
            temp["grade"]   = make_label(widget, base, func=grade)
            temp["page"]    = make_label(widget, base, func=page_num)
            temp["verb"]    = make_label(widget, base, func=base_verb)
            temp["noun"]    = make_label(widget, word, func=base_noun)
            #add pos for each base
        else:
            temp["result"]  = make_label(widget, base)
            temp["grade"]   = ttk.Label(widget, text="#")
            temp["page"]    = ttk.Label(widget, text="#")
            temp["verb"]    = ttk.Label(widget, text="#")
            temp["noun"]    = ttk.Label(widget, text="#")
        rows.append(temp)
        counter = counter + 1
    return rows

#no tests
def sentence_guide(length):
    """Shows a pop up window with input instructions. Returns None."""
    messagebox.showinfo(title=validation_title, 
        message=sentence_instructions.format(length))
