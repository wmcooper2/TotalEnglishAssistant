#!/usr/bin/env python3
"""Validation module for words.py."""

#stand lib
from pathlib import Path
import string

uppercase = string.ascii_uppercase
DATA = str(Path.cwd())+"/data2/"
#Notes
# lowercase all words before checking is_noun() or is_verb()???
# replaced is_important() with is_bolded()

def is_vowel(char):
    """Checks if char is a vowel. Returns Boolean."""
    return char in "aeiou"

def gt_zero(word):
    """Checks that word is greater than zero characters. Returns Boolean."""
    return len(word) > 0

def is_str(word):
    """Checks that word is a string. Returns Boolean."""
    return type(word) is str

def is_proper_noun(word):
    """Checks if word is proper noun. Returns Boolean."""
    return word[0] in uppercase

def in_dictionary(word):
    """Checks if word in books' dictionaries. Returns Boolean."""
    dictionary = []
    with open(DATA+"juniorhighenglishwords.txt", "r") as f:
        [dictionary.append(word.strip()) for word in f.readlines()]
    return word in dictionary

def exists(word):
    """Checks if word exists in book's dictionary. Returns Boolean."""
    if gt_zero(word):
        if not is_proper_noun(word):
            return in_dictionary(word.lower())
        elif is_proper_noun(word):
            return in_dictionary(word)

def is_valid(word):
    """Validates a word. Returns Boolean."""
    return gt_zero(word) and is_str(word) and in_dictionary(word)

def is_noun(word):
    """Checks if word is a noun. Returns Boolean."""
    nouns = []
    with open(DATA+"nouns.txt", "r") as f:
        [nouns.append(word.strip()) for word in f.readlines()]
    return word in nouns

def is_verb(word):
    """Checks if word is a verb. Returns Boolean."""
    verbs = []
    with open(DATA+"verbs.txt", "r") as f:
        [verbs.append(word.strip()) for word in f.readlines()]
    return word in verbs

def is_bolded(word):
    """Checks if word is bolded in the books' dictionaries. 
        Returns Boolean."""
    bolded = []
    with open(DATA+"bolded.txt", "r") as f:
        [bolded.append(word.strip()) for word in f.readlines()]
    return word in bolded
