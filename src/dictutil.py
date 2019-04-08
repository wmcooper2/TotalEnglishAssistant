#!/usr/bin/env python3.7
# dictutil.py
"""Utility module for dictionaries.py"""

# stand lib
import sys
import json
from pathlib import Path
import random
from typing import Dict
from typing import List
from typing import Text

# custom
from constants import JHS_WORDS
from data.jhsdict import jhswords as DICT
from words import is_proper_noun


def dict_value(word: Text, value: Text) -> Text:
    """Gets nested dictionary's value. Returns String."""
    return DICT[word][value]


def exists(word: Text) -> bool:
    """Checks if word exists in book's dictionary. Returns Boolean."""
    if not is_proper_noun(word):
        return in_dict(word.lower())
    elif is_proper_noun(word):
        return in_dict(word)
    else:
        return False


def get_entry(word: Text) -> dict:
    """Gets a single entry. Returns Dictionary."""
    if in_dict(word):
        return DICT.get(word)
    else:
        return {}


def get_pos(word: Text) -> Text:
    """Gets part of speech for word. Returns String."""
    if in_dict(word):
        return dict_value(word, "part of speech")
    return ""


def grade(word: Text) -> Text:
    """Gets grade level of word. Returns String."""
    if in_dict(word):
        return dict_value(word, "grade")
    return ""


def grade_filter(grade: Text, words: List[Text]) -> List[Text]:
    """Filters words based on grade level. Returns List."""
    return list(filter(lambda word: in_grade(grade, word), words))


def gt_eq_grade(word: Text, grade: Text) -> bool:
    """Checks if word in in or above grade. Returns Boolean."""
    return int(grade(word)) >= int(grade)


def gt_eq_page(word: Text, page: Text) -> bool:
    """Checks if word is on or after page. Returns Boolean."""
    return int(page_num(word)) >= int(page)


def in_dict(word: Text) -> bool:
    """Checks if word in books' dictionaries. Returns Boolean."""
    dictionary = []
    with open(JHS_WORDS, "r") as f:
        for entry in f.readlines():
            dictionary.append(entry.strip())
        return word in dictionary
    return False


def in_grade(grade: Text, word: Text) -> bool:
    """Checks word is in grade. Returns Boolean."""
    if int(grade) == int(DICT[word]["grade"]):
        return True
    else:
        return False


def is_valid(word: Text) -> bool:
    """Validates a word. Returns Boolean."""
    if word is not None:
        return in_dict(word)
    else:
        return False


def in_pages(word: Text, lo: Text, hi: Text) -> bool:
    """Checks if a word exists within a page range. Returns Boolean."""
    if gt_eq_page(word, lo) and lt_eq_page(word, hi):
        return True
    else:
        return False


def japanese(word: Text) -> Text:
    """Gets the Japanese definition. Returns String."""
    if in_dict(word):
        return dict_value(word, "japanese")
    else:
        return ""


def lt_eq_grade(word: Text, grade: Text) -> bool:
    """Checks if word is in or below grade. Returns Boolean."""
    return int(grade(word)) <= int(grade)


def lt_eq_page(word: Text, page: Text) -> bool:
    """Checks if word in before or on page. Returns Boolean."""
    return int(page_num(word)) <= int(page)


def page_filter(lo: Text, hi: Text, words: List[Text]) -> List[Text]:
    """Filters words by page range. Returns List."""
    return list(filter(lambda word: in_pages(word, lo, hi), words))


def page_num(word: Text) -> Text:
    """Gets page number of word. Returns String."""
    if in_dict(word):
        return dict_value(word, "page")
    else:
        return ""


def punct_filter(some_list: dict) -> List[Text]:
    """Filters out words containing apostrophe. Returns List."""
    return list(filter(lambda word: "'" in word, some_list.keys()))


def within_page_range(word: Text, start: Text, end: Text) -> bool:
    """Checks if a word exists within a page range. Returns Boolean."""
    if int(page_num(word)) >= int(start) and \
       int(page_num(word)) <= int(end):
        return True
    else:
        return False
