#!/usr/bin/python3

#stand lib

#3rd party
import pytest

#custom
from dictionaries import *

def test_japanese():
    assert japanese("apple")    == "リンゴ"
    assert japanese("camera")   == "カメラ"
    assert japanese("wrap")     == "包む"

def test_page_number():
    assert page_number("after")     == "76"
    assert page_number("amazing")   == "12"
    assert page_number("beach")     == "116"

def test_within_page_range():
    assert within_page_range("cat", 15, 20)     == True
    assert within_page_range("cause", 50, 100)  == True
    assert within_page_range("center", 40, 50)  == False

def test_in_pages():
    assert in_pages("cat", 1, 20)    == True
    assert in_pages("here", 50, 54) == True
    assert in_pages("juice", 17, 10)== False

def test_dict_value():
    assert dict_value("apple", "important")     == "yes"
    assert dict_value("California", "grade")    == "3"
    assert dict_value("camera", "japanese")     == "カメラ"

def test_get_pos():
    assert get_pos("wrap")      == "verb"
    assert get_pos("shrine")    == "noun"
    assert get_pos("since")     == "conjunction"

def test_grade():
    assert grade("beach")   == "1"
    assert grade("became")  == "2"
    assert grade("yellow")  == "3"

def test_same_grade():
    assert same_grade(3, "able")    == True
    assert same_grade(2, "aboard")  == True
    assert same_grade(3, "about")   == False

#tests should be testing a change in one variable?
def test_within_grade_range():
    assert within_grade_range("cat", -1, 0)    == False
    assert within_grade_range("cat", 3, 4)     == False
    assert within_grade_range("cat", 4, 4)     == False
    assert within_grade_range("cat", 0, 0)     == False
    assert within_grade_range("cat", 0, 3)     == True
    assert within_grade_range("cat", 1, 2)     == True
    assert within_grade_range("cat", 0, 4)     == True

def test_get_entry():
    assert type(get_entry("cat")) is dict
    assert type(get_entry("above")) is dict
    assert type(get_entry(" ")).__name__ == "NoneType"
    assert type(get_entry("!")).__name__ == "NoneType"

def test_exists():
    assert exists("apple")      == True
    assert exists("California") == True
    assert exists("yay")        == False

def test_in_dict():
    assert in_dict("apple")       == True
    assert in_dict("California")  == True
    assert in_dict("superduper")  == False
    assert in_dict(" ")           == False

def test_is_valid():
    assert is_valid("wonderful")    == True
    assert is_valid("California")   == True
    assert is_valid("!californ1a")  == False

def test_grade_filter():
    assert len(grade_filter(1, DICT)) == 610
    assert len(grade_filter(2, DICT)) == 503
    assert len(grade_filter(3, DICT)) == 335

def test_page_filter():
    assert len(page_filter(0, 100, DICT))   == 1113
    assert len(page_filter(0, 75, DICT))    == 827
    assert len(page_filter(0, 50, DICT))    == 511

def test_punct_filter():
    assert len(punct_filter(DICT)) == 43




#make
def save_dictionary():
    pass

def edit_entry():
    pass
