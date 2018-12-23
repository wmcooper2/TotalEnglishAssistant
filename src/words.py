#!/usr/bin/python3

#stand lib
import random
import sys
import string

#custom
#from lists import Lists
from data import verbforms
from data.irregularnouns import irregular_nouns
import juniorhighenglishwords
from pathlib import Path
from wordsvalidation import *

alphabet = string.ascii_uppercase + string.ascii_lowercase
good_punctuation = ["'", "-"]
DATA = str(Path.cwd())+"/data2/"
NUMBERS = string.digits
DICTIONARY = juniorhighenglishwords.Junior_High_English_Words

def final_es(word):
    """Checks if final two letters are 'es'. Returns Boolean."""
    return word[-2:] == "es"
    
def final_x(word):
    """Checks if the last letter is x. Returns Boolean."""
    return word[-1] == "x"

def final_o(word):
    """Checks if the last letter is o. Returns Boolean."""
    return word[-1] == "o"

def sock_stew(word):
    """Checks if the last two letters are 'ss', 'ch', 'zz', 'sh'. 
        Returns Boolean."""
    return word[-2:] in ["ss", "ch", "zz", "sh"]

def final_y(word):
    """Checks if the last letter is y. Returns Boolean."""
    return word[-1] == "y"

def y_to_ies(word):
    """Changes the final y to 'ies'. Returns String."""
    return word[:-1]+"ies"

def final_f1(word):
    """Checks if the last letter is f. Returns Boolean."""
    return word[-1] == "f"

def final_f2(word):
    """Checks if the second to last letter is f. Returns Boolean."""
    return word[-2] == "f"

def special_f_end(word):
    """Checks if word is a special f-ending word. Returns Boolean."""
    return word in ["chef", "beef"]
 
def double_f_end(word):
    """Checks if word contains double f ending. Returns Boolean."""
    return (word[-3:-1] == "ff" or word [-2:] == "ff")

def add_ves(word):
    """Appends 'ves'. Returns String."""
    return word+"ves"

def add_s(word):
    """Appends 's'. Returns String."""
    return word+"s"

def add_es(word):
    """Appends 'es'. Returns String."""
    return word+"es"

def foreign_origin(word):
    """Checks if word is of foreign origin. Returns Boolean."""
    words = []
    with open(DATA+"foreignorigin.txt", "r") as f:
        [words.append(w.strip()) for w in f.readlines()]
    return word in words
    
def irregular_noun(word):
    """Checks if word is an irregular noun. Returns Boolean."""
    return word in irregular_nouns.keys()
        
def make_plural(word):
    """Makes word plural if it's a noun or verb. Returns None."""
    #special
    if foreign_origin(word):
        return add_s(word)
    elif irregular_noun(word): 
        return irregular_nouns.get(word) 

    # common
    elif final_es(word):
        return word
    elif (final_x(word) or final_o(word)) and not is_vowel(word[-2]):
        return add_es(word)
    elif final_x(word):
        return add_es(word)
    elif sock_stew(word):
        return add_es(word)
    elif final_y(word) and not is_vowel(word[-2]):
        return y_to_ies(word)        

    # f endings
    elif double_f_end(word):
        return add_s(word)
    elif special_f_end(word):
        return add_s(word)
    elif final_f1(word) and not special_f_end(word):
        return add_ves(word[:-1])
    elif final_f2(word):
        return add_ves(word[:-2])

    else:
        return add_s(word)

def good_char(char):
    """Checks if char is a letter or acceptable punctuation. 
        Returns Boolean."""
    return ((char in alphabet) or (char in good_punctuation))

def remove_punctuation(word):
    """Removes punctuation from the word. Returns String."""
    no_punct = []
    [no_punct.append(char) for char in word if good_char(char)]
    return ''.join(no_punct)

def is_number(char):
    """Checks if char is a number. Returns Boolean."""
    return char in NUMBERS

def remove_numbers(word):
    """Removes all numbers from the word. Returns String."""
    no_nums = []
    [no_nums.append(char) for char in word if not is_number(char)]
    return ''.join(no_nums)

def dict_value(word, value):
    """Gets word's value from dictionary. Returns String."""
    # replace with dict.get(word, value) ? 
    return DICTIONARY[word][value]

def japanese(word):
    """Gets the Japanese definition. Returns String."""
    if is_valid(word) and not is_proper_noun(word):
        return dict_value(word, "japanese")

class Word():
    """The Word class. Return None."""
#    lists               = Lists() 

    #working on vowels.
#    vowels              = lists.vowels

#    alphabet            = lists.alphabet
#    consonants          = lists.consonants
#    dictionary          = lists.dictionary
#    numbers             = string.digits
#    punctuation         = string.punctuation
#    good_punctuation    = lists.good_punctuation
#    uppercase           = string.ascii_uppercase
#    names               = lists.names
#    nouns               = lists.nouns
#    verbs               = lists.verbs
#    common_nouns        = lists.common_nouns
#    proper_nouns        = lists.proper_nouns
#    adverbs             = lists.adverbs
#    auxverbs            = lists.auxverbs
#    articles            = lists.articles
#    pronouns            = lists.pronouns
#    adjectives          = lists.adjectives
#    conjunctions        = lists.conjunctions
#    interjections       = lists.interjections
#    prepositions        = lists.prepositions
#    verb_forms          = lists.verb_forms

    def __init__(self, word):
        """Initializes Word() instance with default attributes. 
        Returns None."""
        self.english = word
#        self.remove_punctuation()
#        self.remove_numbers()
#        self.student_grade_level = self.grade()

    def page_number(self):
        """Gets the page number of a word. Returns String"""
        try:
            return self.dictionary.dictionary[self.english]["page"]
        except:
            try:
                return self.dictionary.dictionary[self.english.lower()]["page"]
            except:
                try:
                    return self.dictionary.dictionary[self.base_verb()]["page"]
                except:
                    try:
                        return self.dictionary.dictionary[self.base_noun()]["page"]
                    except:
                        return "" 
                                     
    def part_of_speech(self):
        """Gets the part of speech. Returns String."""
        try:
            if self.is_valid and self.english not in self.proper_nouns:
                return self.dictionary.dictionary[self.english.lower()]["part of speech"]
            elif len(self.english) > 0 and self.english in self.proper_nouns:
                return self.dictionary.dictionary[self.english]["part of speech"]
            else:
                return ""
        except KeyError:
            return ""

    def grade(self):
        """Gets the grade that the word first appears in. Returns String."""
        try:
            if self.is_valid and self.english not in self.proper_nouns:
                return self.dictionary.dictionary[self.english.lower()]["grade"]
            elif len(self.english) > 0 and self.english in self.proper_nouns:
                return self.dictionary.dictionary[self.english]["grade"]
            else:
                return 0
        except KeyError:
            return 0 

    def change_word(self):
        """Changes the word based on its part of speech. Returns None."""
        pos = self.part_of_speech()
        if pos == "noun":
            self.choose_different_word(self.common_nouns) 
        elif pos == "pronoun":
            self.choose_different_word(self.pronouns) 
        elif pos == "verb":
            self.choose_different_word(self.verbs) 
        elif pos == "adjective":
            self.choose_different_word(self.adjectives) 
        elif pos == "adverb":
            self.choose_different_word(self.adverbs) 
        elif pos == "auxverb":
            self.choose_different_word(self.auxverbs) 
        elif pos == "conjunction":
            self.choose_different_word(self.conjunctions) 
        elif pos == "interjection":
            self.choose_different_word(self.interjections)             
        elif pos == "preposition":
            self.choose_different_word(self.prepositions)            
        elif pos == "article":
            self.choose_different_word(self.articles)

    def choose_different_word(self, some_list): 
        """Chooses a different word from a list. Returns None."""
        copy = some_list[:]
        while self.english in copy:
            copy.remove(self.english)
        self.english = random.choice(copy)

    def base_verb(self):
        """Searches for the base form of a verb. Returns None."""
        for verb in self.verbs:
            for key, value in self.verb_forms.items():
                for k, v in value.items():
                    if v == self.english:
                        return key

    def base_noun(self):
        """Finds the base form of the noun. Returns String."""
        noun = self.english
        if noun in self.dictionary.dictionary.keys() and self.dictionary.dictionary[noun]["part of speech"] == "noun":
            print("FOUND IT == ", noun)
            return noun
        else:
            print("Not found, beginning base noun search.")

        if len(noun) >= 3:
            if noun in self.lists.irregular_nouns:
                print("irregular")
            elif noun in self.lists.same_as_singular:
                print("same as singular")
            elif noun[-2:] == "es":
                if noun[-3] == "v":
                    print("v to f =", noun[:-3])
                    return noun[:-3] + "f"
                elif noun[-3] == "i":
                    print("i to y= ", noun[:-3])
                    return noun[:-3] + "y"
                elif noun[-3] not in self.lists.vowels:
                    print("[-3] not in vowels= ", noun[-3])
                    return noun[:-2]
                elif noun[-3] == "s":
                    print("[-3] is s= ", noun[-3])
                    return noun[:-2]
                elif noun[-3] in self.lists.consonants:
                    return noun[:-1]
                    print("[-3] in consonants= ", noun[-3])
            elif noun[-1] == "s":
                print("noun ends in s", noun)
                return noun[:-1]
        else:
            return ""
            
if __name__ == "__main__":
    word = Word("cats")
    print(word.base_noun())
