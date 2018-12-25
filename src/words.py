#!/usr/bin/python3

#stand lib
import random

#custom
from wordsvalidation import *

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
#    print(word)
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
    for base, nested in VERBFORMS.items():
        for form, value in nested.items():
            if value == verb:
                return base
#    return "'{}' not in book.".format(verb)
#    return "###"
    return " "

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
    if language == "english": return get_english_words()
    elif language == "japanese": return get_japanese_words()
    else: return get_english_words() + get_japanese_words()
        
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
