#stand lib

#3rd party
import pytest

#custom
from words import *

def test_final_es():
    assert final_es("crates") == True
    assert final_es("plates") == True
    assert final_es("party") == False

def test_final_x():
    assert final_x("box") == True
    assert final_x("fox") == True
    assert final_x("locks") == False

def test_final_o():
    assert final_o("who") == True
    assert final_o("tornado") == True
    assert final_o("box") == False

def test_sock_stew():
    assert sock_stew("lunch") == True
    assert sock_stew("sash") == True
    assert sock_stew("bird") == False

def test_final_y():
    assert final_y("play") == True
    assert final_y("may") == True
    assert final_y("lie") == False

def test_y_to_ies():
    assert y_to_ies("party") == "parties"
    assert y_to_ies("may") == "maies"
    assert y_to_ies("lay") == "laies"

def test_final_f1():
    assert final_f1("chef") == True
    assert final_f1("beef") == True
    assert final_f1("knife") == False

def test_final_f2():
    assert final_f2("knife") == True
    assert final_f2("life") == True
    assert final_f2("chef") == False

def test_special_f_end():
    assert spcecial_f_end("chef") == True
    assert spcecial_f_end("beef") == True
    assert spcecial_f_end("chief") == False

def test_double_f_end():
    assert double_f_end("stuff") == True
    assert double_f_end("buff") == True
    assert double_f_end("chief") == False

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

def test_foreign_word():
    assert foreign_word("piano") == True
    assert foreign_word("kilo") == True
    assert foreign_word("banana") == False

def test_irregular_noun():
    assert irregular_noun("person") == True
    assert irregular_noun("woman") == True
    assert irregular_noun("cat") == False

def test_make_plural():
    assert irregular_noun("person") == True
    assert irregular_noun("woman") == True
    assert irregular_noun("cat") == False

def test_good_char():
    assert good_char("a") == True
    assert good_char("-") == True
    assert good_char("!") == False

def test_remove_punctuation():
    assert remove_punctuation("cats!") == "cats"
    assert good_char("bananas?") == "bananas"
    assert good_char("!x#$%&'") == "x'"

def test_remove_numbers():
    pass

def dict_value():
    pass

def japanese():
    pass

def page_number():
    pass

def part_of_speech():
    pass

def grade():
    pass

def change_word():
    pass

def choose_different_word():
    pass

def base_verb():
    pass

def base_noun():
    pass


