#!/usr/bin/python3

#stand lib

#3rd party
import pytest

#custom
from dictionaries import *

def test_japanese():
    assert japanese("apple") == "リンゴ"
    assert japanese("camera") == "カメラ"
    assert japanese("wrap") == "包む"

def test_page_number():
    assert page_number("after") == "76"
    assert page_number("amazing") == "12"
    assert page_number("beach") == "116"

def test_within_page_range():
    assert within_page_range("cat", 15, 20) == True
    assert within_page_range("cause", 50, 100) == True
    assert within_page_range("center", 40, 50) == False

def within_pages():
    pass

def test_dict_value():
    assert dict_value("apple", "important") == "yes"
    assert dict_value("California", "grade") == "3"
    assert dict_value("camera", "japanese") == "カメラ"

def test_get_pos():
    assert get_pos("wrap") == "verb"
    assert get_pos("shrine") == "noun"
    assert get_pos("since") == "conjunction"

def test_grade():
    assert grade("beach") == "1"
    assert grade("became") == "2"
    assert grade("yellow") == "3"

def test_same_grade():
    assert same_grade(3, "able") == True
    assert same_grade(2, "aboard") == True
    assert same_grade(3, "about") == False

def test_grade_filter():
    assert len(grade_filter(1, DICT)) == 610
    assert len(grade_filter(2, DICT)) == 503
    assert len(grade_filter(3, DICT)) == 335

def test_page_filter():
    assert len(page_filter(0, 100, DICT)) == 1113
    assert len(page_filter(0, 75, DICT)) == 827
    assert len(page_filter(0, 50, DICT)) == 511

def test_punct_filter():
    assert len(punct_filter(DICT)) == 43

def save_dictionary():
    pass

def load_dictionary():
    pass

def edit_entry():
    pass

def get_entry():
    pass

def test_size_unchanged():
    assert len(DICT) == 1450
