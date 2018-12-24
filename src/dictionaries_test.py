#!/usr/bin/python3

#stand lib

#3rd party
import pytest

#custom
from dictionaries import *

def test_size_unchanged():
    assert len(DEFAULTDICT) == 1450

def test_filter_words_by_grade():
    assert len(filter_words_by_grade(1, DEFAULTDICT)) == 610
    assert len(filter_words_by_grade(2, DEFAULTDICT)) == 503
    assert len(filter_words_by_grade(3, DEFAULTDICT)) == 335

def test_filter_words_by_punctuation():
    assert len(filter_words_by_punctuation(DEFAULTDICT)) == 43

def filter_words_by_page_range():
    assert len(filter_words_by_page_range(0, 100, DEFAULTDICT)) == 1113
    assert len(filter_words_by_page_range(0, 75, DEFAULTDICT)) == 827
    assert len(filter_words_by_page_range(0, 50, DEFAULTDICT)) == 511

def same_grade():
    assert same_grade(3, "able") == True
    assert same_grade(2, "aboard") == True
    assert same_grade(1, "about") == False

#tested in words_test.py
def within_page_range():
    pass

def save_dictionary():
    pass

def load_dictionary():
    pass

def edit_entry():
    pass

def get_entry():
    pass

