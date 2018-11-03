def is_valid(word):
    """Validates a word. Returns Boolean."""
    if len(word.english) > 0 \
       and type(word.english) is str \
       and exists(word):
        return True
    else:
        return False

def exists(word):
    """Checks if the word exists in the dictionary. Returns Boolean."""
    test = word.english
    if len(test) > 0 and test not in word.proper_nouns:
        return test.lower() in word.dictionary.words
    elif len(test) > 0 and test in word.proper_nouns:
        return test in word.dictionary.words
    else:
        return False

def is_verb(word):
    """Checks if the word is a verb. Returns Boolean."""
    try:
        if is_valid(word) and word.english not in word.proper_nouns:
            return word.dictionary.dictionary[word.english.lower()]["part of speech"] == "verb"
        elif len(word.english) > 0 and word.english in word.proper_nouns:
            return word.dictionary.dictionary[word.english]["part of speech"] == "verb"
        else:
            return False
    except KeyError:
        return False

def is_noun(word):
    """Checks if the word is a noun. Returns Boolean."""
    try:
        if is_valid(word) and word.english not in word.proper_nouns:
            return word.dictionary.dictionary[word.english.lower()]["part of speech"] == "noun"
        elif len(word.english) > 0 and word.english in word.proper_nouns:
            return word.dictionary.dictionary[word.english]["part of speech"] == "noun"
        else:
            return False
    except KeyError:
        return False

def is_proper_noun(word):
    """Checks if the word is a proper noun. Returns Boolean."""
    if is_valid(word) and len(word.english) > 0:
        return word.english in word.proper_nouns

def is_important(word):
    """Checks if the word is 'important'. Returns Boolean."""
    try:
        if is_valid(word) and word.english not in word.proper_nouns:
            return word.dictionary.dictionary[word.english.lower()]["important"]
        elif len(word.english) > 0 and word.english in word.proper_nouns:
            return word.dictionary.dictionary[word.english]["important"]
        else:
            return False
    except KeyError:
        return False
