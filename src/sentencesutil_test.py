#stand lib

#3rd party
import pytest

#custom
from sentencesutil import *

def test_get_pos_func():
    assert type(get_pos_func("cat")).__name__ == "function"
#    assert get_pos_func("California") != "California"
#    assert get_pos_func("white") != "white"

def test_different_word():
    assert different_word("cat") != "cat"
    assert different_word("run") != "run"
    assert different_word("a") != "a"
