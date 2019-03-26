"""Test module for sentutil.py"""
# 3rd party
import pytest

# custom
from sentutil import *


def test_different_word():
    assert different_word("cat")    != "cat"
    assert different_word("run")    != "run"
    assert different_word("a")      != "a"

def test_is_valid_sent():
    assert is_valid_sent("I want a cat.")           == True
    assert is_valid_sent("I have a chicken.")       == True
    assert is_valid_sent("You are a hamburger.")    == True
    assert is_valid_sent("")                        == False

#no tests
def sentence_guide():
    pass
