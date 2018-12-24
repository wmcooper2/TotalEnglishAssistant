#stand lib

#custom
from constants import *

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

def in_dictionary(word):
    """Checks if word in books' dictionaries. Returns Boolean."""
    dictionary = []
    with open(JHSWORDS, "r") as f:
        [dictionary.append(word.strip()) for word in f.readlines()]
    return word in dictionary

def exists(word):
    """Checks if word exists in book's dictionary. Returns Boolean."""
    if gt_zero(word):
        if not is_proper_noun(word):
            return in_dictionary(word.lower())
        elif is_proper_noun(word):
            return in_dictionary(word)

def is_valid(word):
    """Validates a word. Returns Boolean."""
    return gt_zero(word) and is_str(word) and in_dictionary(word)

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
