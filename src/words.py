"""Module for altering individual words and getting lists of words from the base text files.
    * Does NOT rely on dictionaries.py
"""
#stand lib
import random

#custom
from wordsutil import *

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
        
def make_plural(word):
    """Makes word plural if it's a noun or verb. Returns None."""
    #special
    if word == "I":                 return add_s(word)
    elif is_foreign_origin(word):   return add_s(word)
    elif is_irregular_noun(word):   return IRRNOUNS.get(word) 

    # common
    elif final_es(word):            return word
    elif (final_x(word) or final_o(word)) and not is_vowel(word[-2]):
                                    return add_es(word)
    elif final_x(word):             return add_es(word)
    elif sock_stew(word):           return add_es(word)
    elif final_y(word) and not is_vowel(word[-2]):
                                    return y_to_ies(word)

    # f endings
    # sofa -> soves ?
    elif double_f_end(word):        return add_s(word)
    elif special_f_end(word):       return add_s(word)
    elif final_f1(word) and not special_f_end(word): 
                                    return add_ves(word[:-1])
    elif final_f2(word):            return add_ves(word[:-2])

    else:                           return add_s(word)

def remove_punctuation(word):
    """Removes punctuation from the word. Returns String."""
    no_punct = []
    [no_punct.append(char) for char in word if is_good_char(char)]
    return ''.join(no_punct)

def remove_numbers(word):
    """Removes all numbers from the word. Returns String."""
    no_nums = []
    [no_nums.append(char) for char in word if not is_number(char)]
    return ''.join(no_nums)

def base_verb(verb):
    """Gets base form of verb. Returns String."""
    for base, nested in VERBFORMS.items():
        for form, value in nested.items():
            if value == verb:
                return base
    return " "

def base_noun(word):
    """Gets base noun of word. Returns String."""
    for noun in get_nouns():
        if is_irregular_noun(word): return get_base_irregular_noun(word)
#        if is_foreign_origin(word): return get_base_foreign_noun(word)
        if word == noun: return word
        if make_plural(noun) == word: return noun
#    return "'{}' not in book.".format(word)
#    return "###"
    return " "

def get_irregular_nouns():
    """Gets list of irregular nouns. Returns List."""
    temp = []
    with open(IRRNOUNS2, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp

def get_base_irregular_noun(word):
    """Gets base irregular noun. Returns String."""
    for noun in get_irregular_nouns():
        if word == make_plural(noun):
            return noun

#unecessary?
def get_base_foreign_noun(word):
    """Gets base foreign noun. Returns String."""
    pass

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

def get_japanese_words():
    """Gets Japanese words. Returns List."""
    temp = []
    with open(JAPANESEVOCAB, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp

def get_english_words():
    """Gets English words. Returns List."""
    temp = []
    with open(ENGLISHVOCAB, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp

def get_english_japanese():
    """Gets English and Japanese words. Returns List."""
    return get_english_words() + get_japanese_words()

def get_words_in_language(lang):
    """Gets words in lang. Returns List."""
    return {
        "english"           : get_english_words(),
        "japanese"          : get_japanese_words(),
        "english_japanese"  : get_english_japanese(),
    }.get(lang)

def get_lang_func(lang):
    """Gets the function that gets a list of words. Returns Function."""
    return {
        "english"           : get_english_words,
        "japanese"          : get_japanese_words,
        "english_japanese"  : get_english_japanese,
    }.get(lang)






#move tests
def is_vowel(char):
    """Checks if char is a vowel. Returns Boolean."""
    return char in "aeiou"

def gt_zero(word):
    """Checks that word is greater than zero characters. Returns Boolean."""
    return len(word) > 0

def is_str(word):
    """Checks that word is a string. Returns Boolean."""
    return type(word) is str

def is_proper_noun(word):
    """Checks if word is proper noun. Returns Boolean."""
    return word[0] in UPPERCASE

def is_noun(word):
    """Checks if word is a noun. Returns Boolean."""
    nouns = []
    with open(NOUNS, "r") as f:
        [nouns.append(word.strip()) for word in f.readlines()]
    return word in nouns

def is_verb(word):
    """Checks if word is a verb. Returns Boolean."""
    verbs = []
    with open(VERBS, "r") as f:
        [verbs.append(word.strip()) for word in f.readlines()]
    return word in verbs

def is_bolded(word):
    """Checks if word is bolded in the books' dictionaries. 
        Returns Boolean."""
    bolded = []
    with open(BOLDED, "r") as f:
        [bolded.append(word.strip()) for word in f.readlines()]
    return word in bolded

def is_foreign_origin(word):
    """Checks if word is of foreign origin. Returns Boolean."""
    words = []
    with open(DATA+"foreignorigin.txt", "r") as f:
        [words.append(w.strip()) for w in f.readlines()]
    return word in words
   
def is_irregular_noun(word):
    """Checks if word is an irregular noun. Returns Boolean."""
    return word in IRRNOUNS.keys()

def is_good_char(char):             
    """Checks if char is a letter or acceptable punctuation. 
        Returns Boolean."""
    return ((char in ALPHABET) or (char in GOODPUNCT)) 

def is_number(char):
    """Checks if char is a number. Returns Boolean."""
    return char in NUMBERS
#
#def same_grade(grade_level, word):
#    """Checks if the word is in grade. Returns Boolean."""
#    return grade_level == int(grade(word))
#
#def within_grade_range(word, start, end):
#    """Gets word list within grade range. Returns Boolean."""
#    if int(grade(word))>=int(start) and int(grade(word))<=int(end):
#        return True
#    else: return False
#
#def within_page_range(word, start, end):
#    """Checks if a word exists within a page range. Returns Boolean."""
#    if int(page_number(word))>=int(start) and \
#       int(page_number(word))<=int(end):
#        return True
#    else: return False
