"""Utility Module for senttab.py"""
# stand lib
from typing import Any
from typing import List

# 3rd party
import pytest
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

# custom
from dictutil import *

no_punc_words = lambda s: list(map(remove_punctuation, s.split()))


def different_word(word: str) -> str: 
    """Chooses a different word with same pos. Returns String."""
    somepos = get_pos(word)
    temp = word_list(FILES.get(somepos))
    while word in temp: 
        temp.remove(word)
    return random.choice(temp)


def is_valid_sent(sentence: str) -> bool:
    """Checks user inputted valid sentence string. Returns Boolean."""
    if len(sentence) > 0 and len(sentence) <= MAX_SENT_LEN:
        return True
    else:
        return False


def make_label(widget: Any, word: str, func: Any=None) -> Any:
    """Assembles a ttk Label widget. Returns ttk Label Widget."""
    if func != None:
        return ttk.Label(widget, text=func(word))
    else:
        return ttk.Label(widget, text=word)


def get_results(widget: Any, sent: str) -> List[Any]:
    """Creates a dictionary of the result labels. Returns List."""
    rows = []
    counter = 0

    for word in no_punc_words(sent):
        temp = {}
        base = None
        temp["word"] = word
        base = temp["word"]    
        if base_verb(word) != " ":          base = base_verb(word)
        elif base_noun(word) != " ":
            if not is_proper_noun(word):    base = base_noun(word.lower())
            else:                           base = base_noun(word)
        else: base = word

#         if is_valid(base): 
        if in_dict(base): 
            temp["given"]  = make_label(widget, word)
            temp["grade"]   = make_label(widget, base, func=grade)
            temp["page"]    = make_label(widget, base, func=page_num)
            temp["verb"]    = make_label(widget, base, func=base_verb)
            temp["noun"]    = make_label(widget, word, func=base_noun)
        else:
            temp["given"]  = make_label(widget, word)
            temp["grade"]   = ttk.Label(widget, text="#")
            temp["page"]    = ttk.Label(widget, text="#")
            temp["verb"]    = ttk.Label(widget, text="#")
            temp["noun"]    = ttk.Label(widget, text="#")
        rows.append(temp)
        counter = counter + 1
    return rows


#no tests
def sentence_guide(length: str) -> None:
    """Shows a pop up window with input instructions. Returns None."""
    messagebox.showinfo(title=VALIDATION_TITLE, 
        message=SENT_INSTR.format(length))
    return None
