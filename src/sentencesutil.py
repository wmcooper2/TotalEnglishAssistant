#stand lib

#3rd party
import pytest

#custom
from constants import *
from dictionaries import *
from words import *

def get_pos_func(word):
    """Returns function that will get a word list matching 
        the part of speech 'word'. Returns Function."""
#    pos = get_pos(word)
#    if pos == "noun":
#        return choose_different_word(word, get_nouns()) 
#    elif pos == "pronoun":
#        return choose_different_word(word, get_pronouns()) 
#    elif pos == "verb":
#        return choose_different_word(word, get_verbs())
#    elif pos == "adjective":
#        return choose_different_word(word, get_adjectives())
#    elif pos == "adverb":
#        return choose_different_word(word, get_adverbs())
#    elif pos == "auxverb":
#        return choose_different_word(word, get_auxverbs())
#    elif pos == "conjunction":
#        return choose_different_word(word, get_conjunctions())
#    elif pos == "interjection":
#        return choose_different_word(word, get_interjections()) 
#    elif pos == "preposition":
#        return choose_different_word(word, get_prepositions())
#    elif pos == "article":
#        return choose_different_word(word, get_articles())
#
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


#def different_word(word, some_list): 
def different_word(word): 
    """Chooses a different word with the same part of speech. 
        Returns String."""
#    copy = some_list[:]
    temp = get_pos_func(word)()
#    print(len(temp), temp[:3])
    while word in temp:
        temp.remove(word)
    return random.choice(temp)


