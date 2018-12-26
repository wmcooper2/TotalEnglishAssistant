#3rd party
import pytest

#custom
from constants import *
from dictionaries import *
from words import *

def get_pos_func(word):
    """Returns function that will get a word list matching 
        the part of speech 'word'. Returns Function."""
    return {
        "noun"          : get_nouns,
        "pronoun"       : get_pronouns,
        "verb"          : get_verbs,
        "adjective"     : get_adjectives,
        "adverb"        : get_adverbs,
        "auxverb"       : get_auxverbs,
        "conjunction"   : get_conjunctions,
        "interjection"  : get_interjections,
        "preposition"   : get_prepositions,
        "article"       : get_articles,
    }.get(get_pos(word)) 

def different_word(word): 
    """Chooses a different word with the same part of speech. 
        Returns String."""
    temp = get_pos_func(word)()
    while word in temp:
        temp.remove(word)
    return random.choice(temp)
