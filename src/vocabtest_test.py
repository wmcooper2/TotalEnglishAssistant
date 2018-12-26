#stand lib

#3rd party
import pytest

#custom
from vocabtest import *

def test_date_time():
    assert type(date_time()) is str

def test_num():
    assert type(num(1)) is str

def test_make_name():
    assert type(make_name(1, 3, "english")) is str
