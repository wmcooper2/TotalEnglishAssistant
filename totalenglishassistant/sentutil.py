#!/usr/bin/env python3.7
# sentutil.py
"""Utility Module for senttab.py"""

# stand lib
from collections import defaultdict
import random
from typing import Any
from typing import List
from typing import Text

# 3rd party
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

# custom
from constants import FILES
from constants import MAX_SENT_LEN
from constants import VALIDATION_TITLE
from constants import SENT_INSTR
from dictutil import get_pos
from dictutil import grade
from dictutil import in_dict
from dictutil import page_num
from words import base_noun
from words import base_verb
from words import remove_punctuation
from words import word_list


def no_punc_words(words: List[Text]) -> List[Text]:
    """Removes punctuation from words. Returns List."""
    return list(map(remove_punctuation, words.split()))


def different_word(word: Text) -> Text:
    """Chooses a different word with same pos. Returns String."""
    somepos = get_pos(word)
    file_ = FILES.get(somepos)
    temp = word_list(file_)
    while word in temp:
        temp.remove(word)
    return random.choice(temp)


def is_valid_sent(sentence: Text) -> bool:
    """Checks user inputted valid sentence string. Returns Boolean."""
    if len(sentence) > 0 and len(sentence) <= MAX_SENT_LEN:
        return True
    else:
        return False


def make_label(widget: Any, word: Text, func: Any = None) -> Any:
    """Assembles a ttk Label widget. Returns ttk Label Widget."""
    if func is not None:
        return ttk.Label(widget, text=func(word))
    else:
        return ttk.Label(widget, text=word)


def get_results(widget: Any, sent: Text) -> List[Any]:
    """Creates a dictionary of the result labels. Returns List."""
    rows = []
    counter = 0

    for word in no_punc_words(sent):
        temp = {}
        temp["word"] = word
        base = temp["word"]
        if base_verb(word) != " ":
            base = base_verb(word)
            print("base 1", base)
        elif base_noun(word) != " ":
            if not is_proper_noun(word):
                base = base_noun(word.lower())
                print("base 2", base)
            else:
                base = base_noun(word)
                print("base 3", base)
        else:
            base = word
            print("base 4", base)
        temp["given"] = make_label(widget, word)

        print("base 5", base)
        print("base before first in_dict() call", base)
        if in_dict(base):
#             temp["given"] = make_label(widget, word)
            temp["grade"] = make_label(widget, base, func=grade)
            temp["page"] = make_label(widget, base, func=page_num)
            temp["verb"] = make_label(widget, base, func=base_verb)
            temp["noun"] = make_label(widget, word, func=base_noun)
        else:
#             temp["given"] = make_label(widget, word)
            temp["grade"] = ttk.Label(widget, text="#")
            temp["page"] = ttk.Label(widget, text="#")
            temp["verb"] = ttk.Label(widget, text="#")
            temp["noun"] = ttk.Label(widget, text="#")
        rows.append(temp)
        counter = counter + 1
    return rows


def get_results2(widget: Any, sent: Text) -> List[Any]:
    """Creates a dictionary of the result labels. Returns List."""
    rows = []
    counter = 0

    for word in no_punc_words(sent):
        temp = {}
        temp["given"] = make_label(widget, word)
        temp["grade"] = make_label(widget, word, func=grade)
        temp["page"] = make_label(widget, word, func=page_num)
        temp["verb"] = make_label(widget, word, func=base_verb)
        temp["noun"] = make_label(widget, word, func=base_noun)
        rows.append(temp)
        counter = counter + 1
    return rows


def get_results_cli(sent: Text) -> List[Text]:
    """Gets sentence results. Returns List."""
    rows = []
    counter = 0

    for word in no_punc_words(sent):
        temp = {}
        temp["given"] = word
        temp["grade"] = grade(word)
        temp["page"] = page_num(word)
        temp["verb"] = base_verb(word)
        temp["noun"] = base_noun(word)
        rows.append(temp)
        counter = counter + 1
    return rows
 

# no tests
def sentence_guide(length: Text) -> None:
    """Shows a pop up window with input instructions. Returns None."""
    messagebox.showinfo(title=VALIDATION_TITLE,
                        message=SENT_INSTR.format(length))
    return None
