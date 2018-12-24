#!/usr/bin/python3

#stand lib
from pathlib import Path
import random
import sys
import string

#custom
from data2 import verbforms
from data2.irregularnouns import irregular_nouns as IRRNOUNS
import data.juniorhighenglishwords as JHSWORDS
from data2.verbforms import verb_forms as VERBFORMS
from wordsvalidation import *

ALPHABET        = string.ascii_uppercase + string.ascii_lowercase
DATA            = str(Path.cwd())+"/data2/"
DICT            = JHSWORDS.Junior_High_English_Words
GOODPUNCT       = ["'", "-"]
NUMBERS         = string.digits

ADJECTIVES      = DATA+"adjectives.txt"
ADVERBS         = DATA+"adverbs.txt"
ARTICLES        = DATA+"articles.txt"
AUXVERBS        = DATA+"auxverbs.txt"
CONJUNCTIONS    = DATA+"conjunctions.txt"
INTERJECTIONS   = DATA+"interjections.txt"
NOUNS           = DATA+"nouns.txt"
PREPOSITIONS    = DATA+"prepositions.txt"
PROUNOUNS       = DATA+"pronouns.txt"
VERBS           = DATA+"verbs.txt"
#VERBFORMS       = DATA+"verbforms.txt"

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
    return word in IRRNOUNS.keys()
        
def make_plural(word):
    """Makes word plural if it's a noun or verb. Returns None."""
    #special
    if foreign_origin(word):
        return add_s(word)
    elif irregular_noun(word): 
        return IRRNOUNS.get(word) 

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
    return ((char in ALPHABET) or (char in GOODPUNCT))

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
    # what if word is not in dictionary?
    return DICT[word][value]

def japanese(word):
    """Gets the Japanese definition. Returns String."""
    if is_valid(word):
        return dict_value(word, "japanese")

def page_number(word):
    """Gets page number of word. Returns String."""
    if is_valid(word):
        return dict_value(word, "page")

def grade(word):
    """Gets grade level of word. Returns String."""
    if is_valid(word):
        return dict_value(word, "grade")

def get_pos(word):
    """Gets part of speech for word. Returns String."""
    if is_valid(word):
        return dict_value(word, "part of speech")

def get_nouns():
    """Gets a list of nouns. Returns List."""
    temp = []
    with open(NOUNS, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp

def get_pronouns():
    """Gets a list of pronouns. Returns List."""
    temp = []
    with open(PRONOUNS, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp

def get_verbs():
    """Gets a list of verbs. Returns List."""
    temp = []
    with open(VERBS, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp

def base_verb(verb):
    """Gets base form of verb. Returns String."""
#    for verb in get_verbs(): 
    for baseverb, nested_dict in VERBFORMS.items():
        for form, value in nested_dict.items():
            if value == verb:
                return baseverb
    #if not found
    return verb+" not in book."

def get_adjectives():
    """Gets a list of adjectives. Returns List."""
    temp = []
    with open(ADJECTIVES, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp

def get_adverbs():
    """Gets a list of adverbs. Returns List."""
    temp = []
    with open(ADVERBS, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp

def get_auxverbs():
    """Gets a list of auxverbs. Returns List."""
    temp = []
    with open(AUXVERBS, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp

def get_conjunctions():
    """Gets a list of conjunctions. Returns List."""
    temp = []
    with open(CONJUNCTIONS, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp

def get_interjections():
    """Gets a list of interjections. Returns List."""
    temp = []
    with open(INTERJECTIONS, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp

def get_prepositions():
    """Gets a list of prepositions. Returns List."""
    temp = []
    with open(PREPOSITIONS, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp

def get_articles():
    """Gets a list of articles. Returns List."""
    temp = []
    with open(ARTICLES, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp

def change_word(word):
    """Changes the word based on its part of speech. Returns String."""
    pos = get_pos(word)
    if pos == "noun":
        return choose_different_word(word, get_nouns()) 
    elif pos == "pronoun":
        return choose_different_word(word, get_pronouns()) 
    elif pos == "verb":
        return choose_different_word(word, get_verbs())
    elif pos == "adjective":
        return choose_different_word(word, get_adjectives())
    elif pos == "adverb":
        return choose_different_word(word, get_adverbs())
    elif pos == "auxverb":
        return choose_different_word(word, get_auxverbs())
    elif pos == "conjunction":
        return choose_different_word(word, get_conjunctions())
    elif pos == "interjection":
        return choose_different_word(word, get_interjections()) 
    elif pos == "preposition":
        return choose_different_word(word, get_prepositions())
    elif pos == "article":
        return choose_different_word(word, get_articles())

def choose_different_word(word, some_list): 
    """Chooses a different word from some_list. Returns String."""
    copy = some_list[:]
    while word in copy:
        copy.remove(word)
    return random.choice(copy)

def within_page_range(word, start, end):
    """Checks if a word exists within a page range. Returns Boolean."""
    if int(page_number(word))>=int(start) and \
       int(page_number(word))<=int(end):
        return True
    else: return False

def get_words_in_page_range(start, end):
    """Gets word list within page range. Returns List."""
    temp = []
    for word in DICT:
        if within_page_range(word, start, end):
            temp.append(word)
    return temp
        
def within_grade_range(word, start, end):
    """Gets word list within grade range. Returns Boolean."""
    if int(grade(word))>=int(start) and int(grade(word))<=int(end):
        return True
    else: return False

def get_words_in_grade_range(start, end):
    """Gets word list within grade range. Returns List."""
    temp = []
    [temp.append(w) for w in DICT if within_grade_range(w, start, end)]
    return temp

def get_japanese_words():
    """Gets Japanese words. Returns List."""
    temp = []
    [temp.append(v["japanese"]) for k, v in DICT.items()]
    return temp

def get_english_words():
    """Gets English words. Returns List."""
    temp = []
    [temp.append(k) for k in DICT.keys()]
    return temp

def get_words_in_language(language):
    """Gets words of language. Returns List."""
    if language == "english":
        return get_english_words()
    elif language == "japanese":
        return get_japanese_words()
    else:
        return get_english_words() + get_japanese_words()
        











class Word():
    """The Word class. Return None."""

    def __init__(self, word):
        """Initializes Word() instance with default attributes. 
        Returns None."""
        self.english = word

    def base_noun(self):
        """Finds the base form of the noun. Returns String."""
        noun = self.english
        if noun in self.dictionary.dictionary.keys() and self.dictionary.dictionary[noun]["part of speech"] == "noun":
            print("FOUND IT == ", noun)
            return noun
        else:
            print("Not found, beginning base noun search.")

        if len(noun) >= 3:
            if noun in self.lists.IRRNOUNS:
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
