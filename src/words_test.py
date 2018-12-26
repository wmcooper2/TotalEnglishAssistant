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

def test_make_plural():
    assert make_plural("person") == "people"
    assert make_plural("woman") == "women"
    assert make_plural("cat") == "cats"
    assert make_plural("lunch") == "lunches"
    assert make_plural("box") == "boxes"
    assert make_plural("pass") == "passes"
    assert make_plural("gentleman") == "gentlemen"
    assert make_plural("lady") == "ladies"
    assert make_plural("knife") == "knives"

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

def test_get_irregular_nouns():
    assert len(get_irregular_nouns()) == 107

def test_get_base_irregular_noun():
    assert get_base_irregular_noun("algae") == "alga"
    assert get_base_irregular_noun("alumni") == "alumnus"
    assert get_base_irregular_noun("teeth") == "tooth"

def test_get_base_foreign_word():
    pass

def test_get_nouns():
    assert len(get_nouns()) == 851
    
def test_get_pronouns():
    assert len(get_pronouns()) == 45
    
def test_get_verbs():
    assert len(get_verbs()) == 301
    
def test_get_adjectives():
    assert len(get_adjectives()) == 230

def test_get_adverbs():
    assert len(get_adverbs()) == 93
    
def test_get_auxverbs():
    assert len(get_auxverbs()) == 10
    
def test_get_conjunctions():
    assert len(get_conjunctions()) == 8
    
def test_get_interjections():
    assert len(get_interjections()) == 7
    
def test_get_prepositions():
    assert len(get_prepositions()) == 33

def test_get_articles():
    assert len(get_articles()) == 3

def test_get_japanese_words():
    assert len(get_japanese_words()) == 1450

def test_get_english_words():
    assert len(get_english_words()) == 1450

def test_get_words_in_language():
    assert len(get_words_in_language("english")) == 1450
    assert len(get_words_in_language("japanese")) == 1450
    assert len(get_words_in_language("english_japanese")) == 2900
