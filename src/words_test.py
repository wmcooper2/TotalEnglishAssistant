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
    assert special_f_end("chef") == True
    assert special_f_end("beef") == True
    assert special_f_end("chief") == False

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

def test_foreign_origin():
    assert foreign_origin("piano") == True
    assert foreign_origin("kilo") == True
    assert foreign_origin("banana") == False

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
    assert remove_punctuation("bananas?") == "bananas"
    assert remove_punctuation("!x#$%&'") == "x'"

def test_remove_numbers():
    assert remove_numbers("cats9") == "cats"
    assert remove_numbers("0bananas") == "bananas"
    assert remove_numbers("0123y8765") == "y"

def test_dict_value():
    assert dict_value("apple", "important") == "yes"
    assert dict_value("California", "grade") == "3"
    assert dict_value("camera", "japanese") == "カメラ"

def test_japanese():
    assert japanese("apple") == "リンゴ"
    assert japanese("camera") == "カメラ"
    assert japanese("wrap") == "包む"

def test_page_number():
    assert page_number("after") == "76"
    assert page_number("amazing") == "12"
    assert page_number("beach") == "116"

def test_get_pos():
    assert get_pos("wrap") == "verb"
    assert get_pos("shrine") == "noun"
    assert get_pos("since") == "conjunction"

def test_grade():
    assert grade("beach") == "1"
    assert grade("became") == "2"
    assert grade("yellow") == "3"

def test_change_word():
    assert change_word("cat") != "cat"
    assert change_word("California") != "California"
    assert change_word("white") != "white"

def test_choose_different_word():
    assert choose_different_word("cat", get_nouns()) != "cat"
    assert choose_different_word("run", get_verbs()) != "run"
    assert choose_different_word("a", get_articles()) != "a"

#5 seconds
def test_get_words_in_page_range():
    assert len(get_words_in_page_range(0, 100)) == 1113
    assert len(get_words_in_page_range(0, 75)) == 827
    assert len(get_words_in_page_range(0, 50)) == 511

#11  seconds
def test_get_words_in_grade_range():
    assert len(get_words_in_grade_range(1, 1)) == 610
    assert len(get_words_in_grade_range(1, 2)) == 1113
    assert len(get_words_in_grade_range(1, 3)) == 1448 # 2 words missing
    assert len(get_words_in_grade_range(2, 2)) == 503
    assert len(get_words_in_grade_range(2, 3)) == 838
    assert len(get_words_in_grade_range(3, 3)) == 335
    assert len(get_words_in_grade_range(0, 0)) == 0

def test_get_japanese_words():
    assert len(get_japanese_words()) == 1450

def test_get_english_words():
    assert len(get_english_words()) == 1450

def test_get_words_in_language():
    assert len(get_words_in_language("english")) == 1450
    assert len(get_words_in_language("japanese")) == 1450
    assert len(get_words_in_language("")) == 2900

#add filters of the above 5 tests to narrow down results


def base_verb():
    pass

def base_noun():
    pass
    #rework the data2/nounforms.txt into a dict

