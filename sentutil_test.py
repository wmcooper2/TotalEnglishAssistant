#!/usr/bin/env python3.7
# sentutil_test.py
"""Test module for sentutil.py"""

# 3rd party
import pytest

# custom
from sentutil import *


def test_different_word():
    assert different_word("cat") != "cat"
    assert different_word("run") != "run"
    assert different_word("a") != "a"


def test_is_valid_sent():
    assert is_valid_sent("I want a cat.") is True
    assert is_valid_sent("I have a chicken.") is True
    assert is_valid_sent("You are a hamburger.") is True
    assert is_valid_sent("") is False


# no tests
def sentence_guide():
    pass
