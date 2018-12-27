#3rd party
import pytest

#custom
from sentutil import *

def test_get_pos_func():
    assert type(get_pos_func("cat")).__name__ == "function"
    assert type(get_pos_func("above")).__name__ == "function"
    assert type(get_pos_func("dog")).__name__ == "function"

def test_different_word():
    assert different_word("cat") != "cat"
    assert different_word("run") != "run"
    assert different_word("a") != "a"
