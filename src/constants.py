"""Global constants module for the Total English Assistant program."""
#stand lib
from pathlib import Path
import string

#custom
import data.jhsdict as dict_
from data2.verbforms import verb_forms as VERBFORMS
from data2.irregularnouns import irregular_nouns as IRRNOUNS

ALPHABET        = string.ascii_uppercase + string.ascii_lowercase
DATA            = str(Path.cwd())+"/data2/"
DEFAULTENTRY    = "not found"
DICT            = dict_.jhswords
DICTDIR         = "Dictionaries/"

#DICTFILE        = DATA+"dictionarywords.py"
DICTNAME        = "Total English 1, 2 and 3"
GOODPUNCT       = ["'", "-", " "]
JHSWORDS        = DATA+"jhsengvocab.txt"
MAXGRADE        = 3
MINGRADE        = 1
NUMBERS         = string.digits
SMALLINPUT      = 6
UPPERCASE       = string.ascii_uppercase

#for directories.py
ROOTDIR         = "../"
MAINPATH       = Path(ROOTDIR)
VOCABDIR        = "VocabularyTests/"
DIRECTORIES     = [VOCABDIR, DICTDIR]
USERDICT        = Path(ROOTDIR, DICTDIR)

ADJECTIVES      = DATA+"adjectives.txt"
ADVERBS         = DATA+"adverbs.txt"
ARTICLES        = DATA+"articles.txt"
AUXVERBS        = DATA+"auxverbs.txt"
BOLDED          = DATA+"bolded.txt"
CONJUNCTIONS    = DATA+"conjunctions.txt"
ENGLISHVOCAB    = DATA+"englishvocab.txt"
INTERJECTIONS   = DATA+"interjections.txt"
IRRNOUNS2       = DATA+"irregularnouns.txt"
JAPANESEVOCAB   = DATA+"japanesevocab.txt"
NOUNS           = DATA+"nouns.txt"
PREPOSITIONS    = DATA+"prepositions.txt"
PRONOUNS        = DATA+"pronouns.txt"
PROPERNOUNS     = DATA+"propernouns.txt"
VERBS           = DATA+"verbs.txt"

#for sentencestab.py
MAXSENTLEN      = 20
SENTWIDGETLEN   = 39

#for vocabularytab.py
MAXQPERTEST     = 100
MINQPERTEST     = 10
MAXTESTAMT      = 50
MINTESTAMT      = 1
MAXPAGE         = 300
MINPAGE         = 0
JAPANESE        = "日本語"
BOTHLANG        = "English/" + JAPANESE
