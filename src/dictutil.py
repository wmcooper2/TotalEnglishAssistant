# stand lib
import sys
import json
from pathlib import Path
import random

# custom
from words import *

gt_eq_grade = lambda w, g: int(grade(w)) >= int(g)
gt_eq_page = lambda w, p: int(page_num(w)) >= int(p)
lt_eq_grade = lambda w, g: int(grade(w)) <= int(g)
lt_eq_page = lambda w, p: int(page_num(w)) <= int(p)
dict_value = lambda w, val: DICT[w][val]


def exists(word: str) -> bool:
    """Checks if word exists in book's dictionary. Returns Boolean."""
    if not is_proper_noun(word):
        return in_dict(word.lower())
    elif is_proper_noun(word):
        return in_dict(word)
    else:
        return False


def get_entry(word: str) -> dict:
    """Gets a single entry. Returns Dictionary."""
    if in_dict(word):
        return DICT.get(word)
    else:
        return {}


def get_pos(word: str) -> str:
    """Gets part of speech for word. Returns String."""
    if in_dict(word):
        return dict_value(word, "part of speech")
    return ""


def grade(word: str) -> str:
    """Gets grade level of word. Returns String."""
    if in_dict(word):
        return dict_value(word, "grade")
    return ""


def grade_filter(grade: str, words: List[str]) -> List[str]:
    """Filters words based on grade level. Returns List."""
    return list(filter(lambda word: in_grade(grade, word), words))


def in_dict(word: str) -> bool:
    """Checks if word in books' dictionaries. Returns Boolean."""
    dictionary = []
    with open(JHS_WORDS, "r") as f:
        for entry in f.readlines():
            dictionary.append(entry.strip())
        return word in dictionary
    return False


def in_grade(grade: str, word: str) -> bool:
    """Checks word is in grade. Returns Boolean."""
    if int(grade) == int(DICT[word]["grade"]):
        return True
    else:
        return False


def is_valid(word: str) -> bool:
    """Validates a word. Returns Boolean."""
    if word is not None:
        return in_dict(word)
    else:
        return False


def in_pages(word: str, lo: str, hi: str) -> bool:
    """Checks if a word exists within a page range. Returns Boolean."""
    if gt_eq_page(word, lo) and lt_eq_page(word, hi):
        return True
    else:
        return False


def japanese(word: str) -> str:
    """Gets the Japanese definition. Returns String."""
    if in_dict(word):
        return dict_value(word, "japanese")
    else:
        return ""


def page_filter(lo: str, hi: str, words: List[str]) -> List[str]:
    """Filters words by page range. Returns List."""
    return list(filter(lambda word: in_pages(word, lo, hi), words))


def page_num(word: str) -> str:
    """Gets page number of word. Returns String."""
    if in_dict(word):
        return dict_value(word, "page")
    else:
        return ""


def punct_filter(some_list: dict) -> List[str]:
    """Filters out words containing apostrophe. Returns List."""
    return list(filter(lambda word: "'" in word, some_list.keys()))



def within_page_range(word: str, start: str, end: str) -> bool:
    """Checks if a word exists within a page range. Returns Boolean."""
    if int(page_num(word)) >= int(start) and int(page_num(word)) <= int(end):
        return True
    else:
        return False
