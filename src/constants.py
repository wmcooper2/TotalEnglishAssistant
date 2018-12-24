#stand lib
from pathlib import Path
import string

#custom
import data.juniorhighenglishwords as JHSWORDSDICT
from data2.verbforms import verb_forms as VERBFORMS
from data2.irregularnouns import irregular_nouns as IRRNOUNS
from data.juniorhighenglishwords import jhswords as DEFAULTDICT

ALPHABET        = string.ascii_uppercase + string.ascii_lowercase
DATA            = str(Path.cwd())+"/data2/"
DEFAULTENTRY    = {"not found":"not found"}
DICT            = JHSWORDSDICT.jhswords
DICTDIR         = "Dictionaries"
DICTFILE        = DATA+"juniorhighenglishwords.py"
DICTNAME        = "Total English Dictionary; Books 1, 2 and 3"
JHSWORDS        = DATA+"juniorhighenglishwords.txt"
GOODPUNCT       = ["'", "-"]
NUMBERS         = string.digits
UPPERCASE       = string.ascii_uppercase

#for directories.py
ROOTDIR         = "./"
MAINPATH       = Path(ROOTDIR)
VOCABDIR        = "VocabularyTests"
DIRECTORIES     = [VOCABDIR, DICTDIR]
USERDICT        = Path(ROOTDIR, DICTDIR)

#for words.py, wordsvalidation.py
ADJECTIVES      = DATA+"adjectives.txt"
ADVERBS         = DATA+"adverbs.txt"
ARTICLES        = DATA+"articles.txt"
BOLDED          = DATA+"bolded.txt"
AUXVERBS        = DATA+"auxverbs.txt"
CONJUNCTIONS    = DATA+"conjunctions.txt"
INTERJECTIONS   = DATA+"interjections.txt"
IRRNOUNS2       = DATA+"irregularnouns.txt"
NOUNS           = DATA+"nouns.txt"
PREPOSITIONS    = DATA+"prepositions.txt"
PROUNOUNS       = DATA+"pronouns.txt"
VERBS           = DATA+"verbs.txt"

