"""Test module for vocabutil.py"""
#3rd party
import pytest

#custom
from vocabutil import *

def test_in_question_range():
    assert in_question_range(9)     == False
    assert in_question_range(-1)    == False
    assert in_question_range(101)   == False
    assert in_question_range(10)    == True
    assert in_question_range(100)   == True

def test_in_test_range():
    assert in_test_range(0)     == False
    assert in_test_range(-1)    == False
    assert in_test_range(51)    == False
    assert in_test_range(1)     == True

def test_valid_q_input():
    assert valid_q_input(9)     == False
    assert valid_q_input(-1)    == False
    assert valid_q_input(101)   == False
    assert valid_q_input(10)    == True
    assert valid_q_input(100)   == True

def test_valid_lang():
    assert valid_lang("")                  == False
    assert valid_lang(1)                   == False
    assert valid_lang("english")           == True
    assert valid_lang("japanese")          == True
    assert valid_lang("english_japanese")  == True

def test_pages_chosen():
    assert pages_chosen(-1, -100)   == False
    assert pages_chosen(0, 1000)    == False
    assert pages_chosen(300, -1)    == False
    assert pages_chosen(100, 100)   == False
    assert pages_chosen(0, 100)     == True
    assert pages_chosen(10, 20)     == True

def test_date_time():
    assert type(date_time()) is str

def test_page_num():
    assert type(page_num(1)) is str

def test_make_file_name():
    assert type(make_file_name(1, 3, "english")) is str

def test_grade_number():
    assert type(grade_number(1)) is str
