#!/usr/bin/env python3.7
# words_test.py
"""Test module for words.py"""

# 3rd party
import pytest

# custom
from words import *

# make test_is_proper_noun()


def test_final_es():
    assert final_es("crates") is True
    assert final_es("plates") is True
    assert final_es("party") is False


def test_final_x():
    assert final_x("box") is True
    assert final_x("fox") is True
    assert final_x("locks") is False


def test_final_o():
    assert final_o("who") is True
    assert final_o("tornado") is True
    assert final_o("box") is False


def test_sock_stew():
    assert sock_stew("lunch") is True
    assert sock_stew("sash") is True
    assert sock_stew("bird") is False


def test_final_y():
    assert final_y("play") is True
    assert final_y("may") is True
    assert final_y("lie") is False


def test_y_to_ies():
    assert y_to_ies("party") == "parties"
    assert y_to_ies("may") == "maies"
    assert y_to_ies("lay") == "laies"


def test_final_f1():
    assert final_f1("chef") is True
    assert final_f1("beef") is True
    assert final_f1("knife") is False


def test_final_f2():
    assert final_f2("knife") is True
    assert final_f2("life") is True
    assert final_f2("chef") is False


def test_special_f_end():
    assert special_f_end("chef") is True
    assert special_f_end("beef") is True
    assert special_f_end("chief") is False


def test_double_f_end():
    assert double_f_end("stuff") is True
    assert double_f_end("buff") is True
    assert double_f_end("chief") is False


def test_add_ves():
    assert add_ves("cat") == "catves"
    assert add_ves("beef") == "beefves"
    assert add_ves("banana") == "bananaves"


def test_add_s():
    assert add_s("cat") == "cats"
    assert add_s("beef") == "beefs"
    assert add_s("banana") == "bananas"


def test_add_es():
    assert add_es("cat") == "cates"
    assert add_es("beef") == "beefes"
    assert add_es("banana") == "bananaes"


def test_make_plural():
    assert make_plural("box") == "boxes"
    assert make_plural("cat") == "cats"
    assert make_plural("gentleman") == "gentlemen"
    assert make_plural("knife") == "knives"
    assert make_plural("lady") == "ladies"
    assert make_plural("lunch") == "lunches"
    assert make_plural("pass") == "passes"
    assert make_plural("person") == "people"
    assert make_plural("woman") == "women"


def test_remove_punctuation():
    assert remove_punctuation("cats!") == "cats"
    assert remove_punctuation("bananas?") == "bananas"
    assert remove_punctuation("!x#$%&'") == "x'"


def test_remove_numbers():
    assert remove_numbers("cats9") == "cats"
    assert remove_numbers("0bananas") == "bananas"
    assert remove_numbers("0123y8765") == "y"


def test_base_verb():
    assert base_verb("running") == "run"
    assert base_verb("blown") == "blow"
    assert base_verb("walking") == " "


def test_base_noun():
    assert base_noun("bananas") == "banana"
    assert base_noun("wishes") == "wish"
    assert base_noun("cats") == "cat"


def test_get_base_irregular_noun():
    assert get_base_irregular_noun("algae") == "alga"
    assert get_base_irregular_noun("alumni") == "alumnus"
    assert get_base_irregular_noun("teeth") == "tooth"


def test_get_words_in_language():
    assert len(get_words_in_language("english")) == 1450
    assert len(get_words_in_language("japanese")) == 1450
    assert len(get_words_in_language("english_japanese")) == 2900


def test_get_lang_func():
    assert type(get_lang_func("english")).__name__ == "function"
