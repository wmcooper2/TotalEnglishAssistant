#!/usr/bin/env python3.7
# constants.py
"""Global constants module for the Total English Assistant program."""

# stand lib
from pathlib import Path
import string

# custom
# from data.jhsdict import jhswords as DICT

ALPHABET = string.ascii_uppercase+string.ascii_lowercase
DATA = str(Path.cwd())+"/data/"
DICT_DIR = "Dictionaries/"
DICT_NAME = "Total English 1, 2 and 3"
GOOD_PUNCT = ["'", "-", " "]
JHS_WORDS = DATA+"jhsengvocab.txt"
NOT_FOUND = "Not in dictionary."
SMALL_INPUT = 6
UPPERCASE = string.ascii_uppercase
VOCAB_DIR = "VocabularyTests/"

# for directorysetup.py
DIRECTORIES = [VOCAB_DIR, DICT_DIR]

# raw data files
ADJECTIVES = DATA+"adjectives.txt"
ADVERBS = DATA+"adverbs.txt"
ARTICLES = DATA+"articles.txt"
AUXVERBS = DATA+"auxverbs.txt"
BOLDED = DATA+"bolded.txt"
CONJUNCTIONS = DATA+"conjunctions.txt"
ENGLISH_VOCAB = DATA+"englishvocab.txt"
INTERJECTIONS = DATA+"interjections.txt"
IRR_NOUNS = DATA+"irregularnouns.txt"
JAP_VOCAB = DATA+"japanesevocab.txt"
NOUNS = DATA+"nouns.txt"
PREPOSITIONS = DATA+"prepositions.txt"
PRONOUNS = DATA+"pronouns.txt"
PROP_NOUNS = DATA+"propernouns.txt"
VERBS = DATA+"verbs.txt"
FILES = {
        "adjective": ADJECTIVES,
        "adverb": ADVERBS,
        "article": ARTICLES,
        "auxverb": AUXVERBS,
        "bolded": BOLDED,
        "conjunction": CONJUNCTIONS,
        "english": ENGLISH_VOCAB,
        "interjection": INTERJECTIONS,
        "irregular_nouns": IRR_NOUNS,
        "japanese": JAP_VOCAB,
        "noun": NOUNS,
        "preposition": PREPOSITIONS,
        "pronoun": PRONOUNS,
        "proper_nouns": PROP_NOUNS,
        "verb": VERBS,
        }

# for sentences tab
MAX_SENT_LEN = 20
SENT_WIDGET_LEN = 39
SENT_INSTR = "'Input any sentence' must be greater than 0 and less than {0} characters."
VALIDATION_TITLE = "Data Validation"

# for vocabulary tab
MAX_Q_PER_T = 100
MIN_Q_PER_T = 10
MAX_T_AMT = 50
MIN_T_AMT = 1
MAX_PAGE = 300
MIN_PAGE = 0
JAPANESE = "日本語"
BOTH_LANG = "English/"+JAPANESE
