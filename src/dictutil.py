#!/usr/bin/python3

#stand lib
import sys
import json
from pathlib import Path
import random

#custom
from words import *

def japanese(word):
    """Gets the Japanese definition. Returns String."""
    if is_valid(word):
        return dict_value(word, "japanese")

def page_number(word):
    """Gets page number of word. Returns String."""
    if is_valid(word):
        return dict_value(word, "page")

def within_page_range(word, start, end):
    """Checks if a word exists within a page range. Returns Boolean."""
    if int(page_number(word))>=int(start) and \
       int(page_number(word))<=int(end):
        return True
    else: return False

def in_pages(word, lo, hi):
    """Checks if a word exists within a page range. Returns Boolean."""
    if gt_eq_page(word, lo) and lt_eq_page(word, hi): return True
    else: return False

def dict_value(word, value):
    """Gets word's value from dictionary. Returns String."""
    return DICT[word][value]

def get_pos(word):
    """Gets part of speech for word. Returns String."""
    if is_valid(word):
        return dict_value(word, "part of speech")

def grade(word):
    """Gets grade level of word. Returns String."""
    if is_valid(word):
        return dict_value(word, "grade")

def same_grade(grade, word):
    """Checks that a word is in grade level. Returns Boolean."""
    if int(grade) == int(DICT[word]["grade"]): return True
    else: return False

def gt_eq_page(word, page_num):
    """Checks if word is on or after page_num. Returns Boolean."""
    return int(page_number(word)) >= int(page_num)

def lt_eq_page(word, page_num):
    """Checks if word is on or before page_num. Returns Boolean."""
    return int(page_number(word)) <= int(page_num)

def same_grade(std_grade, word):
    """Checks if the word is in grade. Returns Boolean."""
    return std_grade == int(grade(word))

#refactor
def within_grade_range(word, start, end):
    """Gets word list within grade range. Returns Boolean."""
    if int(grade(word))>=int(start) and int(grade(word))<=int(end):
        return True
    else: return False

def get_entry(word):
    """Gets a single entry. Returns Dictionary."""
    if in_dict(word): return DICT.get(word)
    else: return None

def exists(word):
    """Checks if word exists in book's dictionary. Returns Boolean."""
    if gt_zero(word):
        if not is_proper_noun(word): return in_dict(word.lower())
        elif is_proper_noun(word): return in_dict(word)

def in_dict(word):
    """Checks if word in books' dictionaries. Returns Boolean."""
    dictionary = []
    with open(JHSWORDS, "r") as f:
        [dictionary.append(word.strip()) for word in f.readlines()]
    return word in dictionary

def is_valid(word):
    """Validates a word. Returns Boolean."""
    return gt_zero(word) and is_str(word) and in_dict(word)

def grade_filter(grade, some_list):
    """Filters some_list based on grade level. Returns List."""
    return list(filter(lambda word: same_grade(grade, word), some_list))

def page_filter(lo, hi, some_list):
    """Filters some_list by page range. Returns List."""
    return list(filter(lambda word: in_pages(word, lo, hi), some_list))

def punct_filter(some_list):
    """Filters by words that have an apostrophe. Returns List."""
    return list(filter(lambda word: "'" in word, some_list.keys()))




#make tests
def save_dictionary(save_this, file_path):
    """Saves dictionary to file_path. Returns None."""
    dump_here = open(file_path, "w+")
    json.dump(save_this, dump_here)
    dump_here.close()

def edit_entry(key, entry):
    """Edits an entry in the dictionary. Returns None."""
    dictionary[key] = entry
    save_dictionary(dictionary, default_dict_path)
