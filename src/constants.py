"""Global constants module for the Total English Assistant program."""
# stand lib
from pathlib import Path
import string

# custom
from data.jhsdict import jhswords as DICT
from data.verbforms import verb_forms as VERBFORMS
# from data.irregularnouns import irregular_nouns as IRRNOUNS

ALPHABET = string.ascii_uppercase + string.ascii_lowercase
DATA = str(Path.cwd())+"/src/data/"
# DEFAULT_ENTRY = "not found"
DICT_DIR = "Dictionaries/"
DICT_NAME = "Total English 1, 2 and 3"
GOOD_PUNCT = ["'", "-", " "]
JHS_WORDS = DATA+"jhsengvocab.txt"
# MAX_GRADE = 3
# MIN_GRADE = 1
NUMBERS = string.digits
SMALL_INPUT = 6
UPPERCASE = string.ascii_uppercase

# for directories.py
ROOT_DIR = "./"
# MAIN_PATH = Path(ROOT_DIR)
VOCAB_DIR = "VocabularyTests/"
DIRECTORIES = [VOCAB_DIR, DICT_DIR]
USER_DICT = Path(ROOT_DIR, DICT_DIR)

# raw data files
ADJECTIVES = DATA + "adjectives.txt"
ADVERBS = DATA + "adverbs.txt"
ARTICLES = DATA + "articles.txt"
AUXVERBS = DATA + "auxverbs.txt"
BOLDED = DATA + "bolded.txt"
CONJUNCTIONS = DATA + "conjunctions.txt"
ENGLISH_VOCAB = DATA + "englishvocab.txt"
INTERJECTIONS = DATA + "interjections.txt"
IRR_NOUNS = DATA + "irregularnouns.txt"
JAP_VOCAB = DATA + "japanesevocab.txt"
NOUNS = DATA + "nouns.txt"
PREPOSITIONS = DATA + "prepositions.txt"
PRONOUNS = DATA + "pronouns.txt"
PROP_NOUNS = DATA + "propernouns.txt"
VERBS = DATA + "verbs.txt"

# for sentencestab.py
MAX_SENT_LEN = 20
SENT_WIDGET_LEN = 39

# for vocabularytab.py
MAX_Q_PER_T = 100
MIN_Q_PER_T = 10
MAX_T_AMT = 50
MIN_T_AMT = 1
MAX_PAGE = 300
MIN_PAGE = 0
JAPANESE = "日本語"
BOTH_LANG = "English/" + JAPANESE
