# stand lib
import sys
import json
from pathlib import Path
import random

# custom
from words import *

gt_eq_grade = lambda w, g: int(grade(w))>=int(g) 
gt_eq_page = lambda w, p: int(page_num(w)) >= int(p)
lt_eq_grade = lambda w, g: int(grade(w))<=int(g)
lt_eq_page = lambda w, p: int(page_num(w))<=int(p)
# not_none = lambda w: w != None
dict_value = lambda w, val: DICT[w][val]


def edit_entry(key, entry):
    """Edits an entry in the dictionary. Returns None."""
    dictionary[key] = entry
    save_dictionary(dictionary, default_dict_path)


def exists(word: str) -> bool:
    """Checks if word exists in book's dictionary. Returns Boolean."""
#     if gt_zero(word):
    if not is_proper_noun(word):
        return in_dict(word.lower())
    elif is_proper_noun(word):
        return in_dict(word)
    else:
        return False


def get_entry(word):
    """Gets a single entry. Returns Dictionary."""
    if in_dict(word):
        return DICT.get(word)
    else:
        return None


def get_pos(word: str) -> str:
    """Gets part of speech for word. Returns String."""
#     if is_valid(word):
#     import pdb; pdb.set_trace()
    if in_dict(word):
        return dict_value(word, "part of speech")
    return ""


def grade(word: str) -> str:
    """Gets grade level of word. Returns String."""
#     if is_valid(word):
    if in_dict(word):
        return dict_value(word, "grade")


def grade_filter(grade: str, words: List[str]) -> List[str]:
    """Filters words based on grade level. Returns List."""
    return list(filter(lambda word: in_grade(grade, word), words))


def in_dict(word):
    """Checks if word in books' dictionaries. Returns Boolean."""
    dictionary = []
    with open(JHS_WORDS, "r") as f:
        for entry in f.readlines():
            dictionary.append(entry.strip())
        return word in dictionary


def in_grade(grade, word):
    """Checks word is in grade. Returns Boolean."""
    if int(grade) == int(DICT[word]["grade"]):
        return True
    else:
        return False


def is_valid(word):
    """Validates a word. Returns Boolean."""
#     if not_none(word):
    if word is not None:
#         return gt_zero(word) and is_str(word) and in_dict(word)
#         return is_str(word) and in_dict(word)
        return in_dict(word)
    else:
        return False


def in_pages(word: str, lo: str, hi: str) -> bool:
    """Checks if a word exists within a page range. Returns Boolean."""
    if gt_eq_page(word, lo) and lt_eq_page(word, hi):
        return True
    else:
        return False


def japanese(word):
    """Gets the Japanese definition. Returns String."""
#     if is_valid(word):
    if in_dict(word):
        return dict_value(word, "japanese")


def page_filter(lo: str, hi: str, words: List[str]) -> List[str]:
    """Filters words by page range. Returns List."""
    return list(filter(lambda word: in_pages(word, lo, hi), words))


def page_num(word):
    """Gets page number of word. Returns String."""
#     if is_valid(word):
    if in_dict(word):
        return dict_value(word, "page")


def punct_filter(some_list):
    """Filters out words containing apostrophe. Returns List."""
    return list(filter(lambda word: "'" in word, some_list.keys()))


def save_dictionary(save_this, file_path):
    """Saves dictionary to file_path. Returns None."""
    dump_here = open(file_path, "w+")
    json.dump(save_this, dump_here)
    dump_here.close()


def within_grade_range(word, start, end):
    """Gets word list within grade range. Returns Boolean."""
    if gt_eq_grade(word, start) and lt_eq_grade(word, end):
        return True
    else:
        return False


def within_page_range(word, start, end):
    """Checks if a word exists within a page range. Returns Boolean."""
    if int(page_num(word))>=int(start) and \
       int(page_num(word))<=int(end):
           return True
    else:
        return False
