#!/usr/bin/python3

#stand lib
import sys
import json
from pathlib import Path
import random

#custom
from words import *

def same_grade(grade, word):
    """Checks that a word is in grade level. Returns Boolean."""
    if int(grade) == int(DEFAULTDICT[word]["grade"]): return True
    else: return False

def filter_words_by_grade(grade, some_list):
    """Filters some_list based on grade level. Returns List."""
    words = []
    for word in some_list:
        if same_grade(grade, word):
            words.append(word)
    return words

def filter_words_by_page_range(start, end, some_list):
    """Filters some_list by page range. Returns List."""
    temp = []
    for word in some_list:
        if within_page_range(word, start, end):
            temp.append(word)
    return temp

#copied from words.py
def within_page_range(word, start, end):
    """Checks if a word exists within a page range. Returns Boolean."""
    if int(page_number(word))>=int(start) and \
       int(page_number(word))<=int(end):
        return True
    else: return False

def filter_words_by_punctuation(some_list):
    """Filters some_list by words that have an apostrophe. Returns List."""
    temp = []
    for word in some_list.keys():
        if "'" in word:
            temp.append(word)
    return temp

def save_dictionary(save_this, file_path):
    """Saves dictionary to file_path. Returns None."""
    dump_here = open(file_path, "w+")
    json.dump(save_this, dump_here)
    dump_here.close()

def edit_entry(key, entry):
    """Edits an entry in the dictionary. Returns None."""
    dictionary[key] = entry
    save_dictionary(dictionary, default_dict_path)

def get_entry(word):
    """Sets a single entry. Returns None."""
    if in_dictionary(word):
        return DICT[word]
    else:
    #replace with dictionary.get(word, "not found")?
        try:
            return dictionary[word]
        except KeyError:
            return DEFAULTENTRY
