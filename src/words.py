"""Module for altering individual words and getting lists of words from the base text files.
    * Does NOT rely on dictionaries.py
"""
# stand lib
from typing import List

# custom
from constants import *

add_s = lambda x: x + "s"
add_es = lambda x: x + "es"
add_ves = lambda x: x + "ves"
double_f_end = lambda x: x[-2:] == "ff"
final_es = lambda x: x[-2:] == "es" 
final_x = lambda x: x[-1] == "x"
final_o = lambda x: x[-1] == "o"
final_y = lambda x: x[-1] == "y"
final_f1 = lambda x: x[-1] == "f"
final_f2 = lambda x: x[-2] == "f"
# gt_zero = lambda x: len(x) > 0
# is_irr_noun = lambda x: x in IRRNOUNS.keys()
is_number = lambda x: x in NUMBERS
is_str = lambda x: type(x) is str
is_vowel = lambda x: x in "aeiou"
sock_stew = lambda x: x[-2:] in ["ss", "ch", "zz", "sh"]
special_f_end = lambda x: x in ["chef", "beef"]
y_to_ies = lambda x: x[:-1]+"ies"


def base_noun(word: str) -> str:
    """Gets base noun of word. Returns String."""
    for noun in get_nouns():
        if is_irr_noun(word):
            return get_base_irregular_noun(word)
#        if is_foreign_origin(word): return get_base_foreign_noun(word)
        elif word == noun:
            return word
        elif make_plural(noun) == word:
            return noun
    return " "


def base_verb(verb: str) -> str:
    """Gets base form of verb. Returns String."""
    for base, nested in VERBFORMS.items():
        for form, value in nested.items():
            if value == verb:
                return base
    return " "

 
# def get_adjectives() -> List[str]:
#     """Gets a list of adjectives. Returns List."""
#     temp = []
#     with open(ADJECTIVES, "r") as f:
# #         [temp.append(line.strip()) for line in f.readlines()]
#         for line in f.readlines():
#             temp.append(line.strip())
#     return temp
 

def word_list(somefile: str) -> List[str]:
    """Gets somefile's list of words. Returns List."""
    temp = []
    with open(somefile, "r") as file_:
        for line in file_.readlines():
            temp.append(line.strip())
    return temp

# def in_word_list(somefile: str, someword: str) -> bool:
#     """Checks if a word is in wordlist. Returns Boolean."""
#     return someword in wordlist(somefile)
#     return someword in temp






 
# def get_adverbs() -> List[str]:
#     """Gets a list of adverbs. Returns List."""
#     temp = []
#     with open(ADVERBS, "r") as f:
# #         [temp.append(line.strip()) for line in f.readlines()]
#         for line in f.readlines():
#             temp.append(line.strip())
#     return temp
 

# def get_articles() -> List[str]:
#     """Gets a list of articles. Returns List."""
#     temp = []
#     with open(ARTICLES, "r") as f:
# #         [temp.append(line.strip()) for line in f.readlines()]
#         for line in f.readlines():
#             temp.append(line.strip())
#     return temp
 

# def get_auxverbs() -> List[str]:
#     """Gets a list of auxverbs. Returns List."""
#     temp = []
#     with open(AUXVERBS, "r") as f:
# #         [temp.append(line.strip()) for line in f.readlines()]
#         for line in f.readlines():
#             temp.append(line.strip())
#     return temp
 

# def get_base_foreign_noun(word):
#     """Gets base foreign noun. Returns String."""
#     pass


def get_base_irregular_noun(word: str) -> str:
    """Gets base irregular noun. Returns String."""
    for noun in get_irregular_nouns():
        if word == make_plural(noun):
            return noun
    return " "


# def get_conjunctions() -> List[str]:
#     """Gets a list of conjunctions. Returns List."""
#     temp = []
#     with open(CONJUNCTIONS, "r") as f:
# #         [temp.append(line.strip()) for line in f.readlines()]
#         for line in f.readlines():
#             temp.append(line.strip())
#     return temp
 

def get_english_japanese() -> List[str]:
    """Gets English and Japanese words. Returns List."""
    return get_english_words() + get_japanese_words()


def get_english_words() -> List[str]:
    """Gets English words. Returns List."""
    temp = []
    with open(ENGLISH_VOCAB, "r") as f:
#         [temp.append(line.strip()) for line in f.readlines()]
        for line in f.readlines():
            temp.append(line.strip())
    return temp


# def get_interjections():
#     """Gets a list of interjections. Returns List."""
#     temp = []
#     with open(INTERJECTIONS, "r") as f:
# #         [temp.append(line.strip()) for line in f.readlines()]
#         for line in f.readlines():
#             temp.append(line.strip())
#     return temp


def get_irregular_nouns():
    """Gets list of irregular nouns. Returns List."""
    temp = []
    with open(IRR_NOUNS, "r") as f:
#         [temp.append(line.strip()) for line in f.readlines()]
        for line in f.readlines():
            temp.append(line.strip())
    return temp


def is_irr_noun(noun: str) -> bool:
    """Checks if noun is irregular. Returns Boolean."""
    return noun in get_irregular_nouns()


def get_japanese_words() -> List[str]:
    """Gets Japanese words. Returns List."""
    temp = []
    with open(JAP_VOCAB, "r") as f:
#         [temp.append(line.strip()) for line in f.readlines()]
        for line in f.readlines():
            temp.append(line.strip())
    return temp


def get_lang_func(lang):
    """Gets the function that gets a list of words. Returns Function."""
    return {
        "english"           : get_english_words,
        "japanese"          : get_japanese_words,
        "english_japanese"  : get_english_japanese,
    }.get(lang)


def get_nouns():
    """Gets a list of nouns. Returns List."""
    temp = []
    with open(NOUNS, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp


# def get_prepositions():
#     """Gets a list of prepositions. Returns List."""
#     temp = []
#     with open(PREPOSITIONS, "r") as f:
#         [temp.append(line.strip()) for line in f.readlines()]
#     return temp
 

# def get_pronouns():
#     """Gets a list of pronouns. Returns List."""
#     temp = []
#     with open(PRONOUNS, "r") as f:
#         [temp.append(line.strip()) for line in f.readlines()]
#     return temp


def get_verbs():
    """Gets a list of verbs. Returns List."""
    temp = []
    with open(VERBS, "r") as f:
        [temp.append(line.strip()) for line in f.readlines()]
    return temp


def get_words_in_language(lang):
    """Gets words in lang. Returns List."""
    return {
        "english"           : get_english_words(),
        "japanese"          : get_japanese_words(),
        "english_japanese"  : get_english_japanese(),
    }.get(lang)


# def is_bolded(word: str) -> bool:
#     """Checks if word is bolded. Returns Boolean."""
#     temp = []
#     with open(BOLDED, "r") as f:
#         [temp.append(word.strip()) for word in f.readlines()]
#     return word in temp
 
 
def is_foreign_origin(word):
    """Checks if word is of foreign origin. Returns Boolean."""
    words = []
    with open(DATA+"foreignorigin.txt", "r") as f:
        [words.append(w.strip()) for w in f.readlines()]
    return word in words


def is_good_char(char):             
    """Checks if char is a letter or acceptable punctuation. 
        Returns Boolean."""
    return ((char in ALPHABET) or (char in GOOD_PUNCT)) 


# def is_noun(word):
#     """Checks if word is a noun. Returns Boolean."""
#     nouns = []
#     with open(NOUNS, "r") as f:
#         [nouns.append(word.strip()) for word in f.readlines()]
#     return word in nouns


def is_proper_noun(word):
    """Checks if word is proper noun. Returns Boolean."""
    propernouns = []
    with open(PROP_NOUNS, "r") as f:
        [propernouns.append(word.strip()) for word in f.readlines()]
    return word in propernouns


# def is_verb(word):
#     """Checks if word is a verb. Returns Boolean."""
#     verbs = []
#     with open(VERBS, "r") as f:
#         [verbs.append(word.strip()) for word in f.readlines()]
#     return word in verbs


def make_plural(word):
    """Makes word plural if it's a noun or verb. Returns None."""
    #special
    if word == "I":
        return add_s(word)
    elif is_foreign_origin(word):
        return add_s(word)
    # fix this
#     elif is_irr_noun(word):   return IRRNOUNS.get(word) 

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
    # sofa -> soves ?
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
