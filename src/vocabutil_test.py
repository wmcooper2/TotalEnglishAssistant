#!/usr/bin/env python3.7
# vocabutil_test.py
"""Test module for vocabutil.py"""

# 3rd party
import pytest

# custom
from vocabutil import *


def test_in_question_range():
    assert in_question_range(9) is False
    assert in_question_range(-1) is False
    assert in_question_range(101) is False
    assert in_question_range(10) is True
    assert in_question_range(100) is True


def test_in_test_range():
    assert in_test_range(0) is False
    assert in_test_range(-1) is False
    assert in_test_range(51) is False
    assert in_test_range(1) is True


def test_valid_q_input():
    assert valid_q_input(9) is False
    assert valid_q_input(-1) is False
    assert valid_q_input(101) is False
    assert valid_q_input(10) is True
    assert valid_q_input(100) is True


def test_valid_lang():
    assert valid_lang("") is False
    assert valid_lang(1) is False
    assert valid_lang("english") is True
    assert valid_lang("japanese") is True
    assert valid_lang("english_japanese") is True


def test_pages_chosen():
    assert pages_chosen(-1, -100) is False
    assert pages_chosen(0, 1000) is False
    assert pages_chosen(300, -1) is False
    assert pages_chosen(100, 100) is False
    assert pages_chosen(0, 100) is True
    assert pages_chosen(10, 20) is True


def test_date_time():
    assert type(date_time()) is str


def test_page_num():
    assert type(page_num(1)) is str


def test_make_file_name():
    assert type(make_file_name(1, 3, "english")) is str


def test_grade_number():
    assert type(grade_number(1)) is str
