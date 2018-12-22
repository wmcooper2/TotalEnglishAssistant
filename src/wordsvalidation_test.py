"""This module replaces 'words_test.py'"""

#stand lib

#3rd party
import pytest

#custom
from wordsvalidation import * 

def test_is_vowel():
    assert is_vowel("a") == True
    assert is_vowel("e") == True
    assert is_vowel("k") == False

def test_gt_zero():
    assert gt_zero("apple") == True
    assert gt_zero("a") == True
    assert gt_zero("") == False

def test_is_str():
    assert is_str("apple") == True
    assert is_str("'&!") == True
    assert is_str(1) == False

def test_is_proper_noun():
    assert is_proper_noun("Niagra Falls") == True
    assert is_proper_noun("California") == True
    assert is_proper_noun("apple") == False

def test_in_dictionary():
    assert in_dictionary("apple") == True
    assert in_dictionary("California") == True
    assert in_dictionary("superduper") == False

def test_exists():
    assert exists("apple") == True
    assert exists("California") == True
    assert exists("yay") == False

def test_is_valid():
    assert is_valid("wonderful") == True
    assert is_valid("California") == True
    assert is_valid("!californ1a") == False

def test_is_noun():
    assert is_noun("cat") == True
    assert is_noun("banana") == True
    assert is_noun("actually") == False

def test_is_verb():
    assert is_verb("run") == True
    assert is_verb("walk") == True
    assert is_verb("California") == False

def test_is_bolded():
    assert is_bolded("about") == True
    assert is_bolded("any") == True
    assert is_bolded("abroad") == False
