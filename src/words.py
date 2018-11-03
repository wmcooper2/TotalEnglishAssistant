#!/usr/bin/python3

#stand lib
import random
import sys
import string

#custom
from lists import Lists
from data import verbforms
import wordsvalidation as check

class Word():
    """The Word class. Return None."""
    lists               = Lists() 
    vowels              = lists.vowels
    alphabet            = lists.alphabet
    consonants          = lists.consonants
    dictionary          = lists.dictionary
    numbers             = string.digits
    punctuation         = string.punctuation
    good_punctuation    = lists.good_punctuation
    uppercase           = string.ascii_uppercase
    names               = lists.names
    nouns               = lists.nouns
    verbs               = lists.verbs
    common_nouns        = lists.common_nouns
    proper_nouns        = lists.proper_nouns
    adverbs             = lists.adverbs
    auxverbs            = lists.auxverbs
    articles            = lists.articles
    pronouns            = lists.pronouns
    adjectives          = lists.adjectives
    conjunctions        = lists.conjunctions
    interjections       = lists.interjections
    prepositions        = lists.prepositions
    verb_forms          = lists.verb_forms

    def __init__(self, word):
        """Initializes Word() instance with default attributes. 
        Returns None."""
        self.english = word
        self.remove_punctuation()
        self.remove_numbers()
        self.student_grade_level = self.grade()

    def is_valid(self):
        """Checks if a word is valid. Returns Boolean."""
        return check.is_valid(self)

    def proper_noun(self):
        """Checks for proper noun. Returns Boolean"""
        return check.is_proper_noun(self)

    def __str__(self):
        """Returns the English form of the word. Returns String."""
        return self.english
            
    def base_word(self):
        """Checks if a word is a normal key in the dictionary. 
        Returns Boolean."""
        pass

    def is_verb(self):
        """Checks if word is a verb. Returns Boolean."""
        return check.is_verb(self)

    def is_noun(self):
        """Checks if word is a noun. Returns Boolean."""
        return check.is_noun(self)

    def remove_punctuation(self):
        """Removes punctuation from the word. Returns None."""
        no_punct = []
        for character in self.english:
            if character in self.alphabet or character in self.good_punctuation:
                no_punct.append(character)
        joined_word = ''.join(no_punct)
        self.english = joined_word

    def remove_numbers(self):
        """Removes all numbers from the word. Returns None."""
        no_nums = []
        for character in self.english:
            if character in self.numbers:
                continue
            else:
                 no_nums.append(character)
        joined_word = ''.join(no_nums)
        self.english = joined_word

    def japanese(self):
        """Gets the Japanese definition. Returns String."""
        if self.is_valid and self.english not in self.proper_nouns:
            return self.dictionary.dictionary[self.english.lower()]["japanese"]
        elif len(self.english) > 0 and self.english in self.proper_nouns:
            return self.dictionary.dictionary[self.english]["japanese"]
        else:
            return "" 
            
    def set_verb_form_attribute_(self):
        """Sets the verb attribute of the word. Returns String."""
        if self.is_valid and self.english not in self.proper_nouns:
            return self.english in self.verbs
        else:
            return "###"

    def page_number(self):
        """Gets the page number of a word. Returns String"""
        try:
            return self.dictionary.dictionary[self.english]["page"]
        except:
            try:
                return self.dictionary.dictionary[self.english.lower()]["page"]
            except:
                try:
                    return self.dictionary.dictionary[self.base_verb()]["page"]
                except:
                    try:
                        return self.dictionary.dictionary[self.base_noun()]["page"]
                    except:
                        return "" 
                                     
    def part_of_speech(self):
        """Gets the part of speech. Returns String."""
        try:
            if self.is_valid and self.english not in self.proper_nouns:
                return self.dictionary.dictionary[self.english.lower()]["part of speech"]
            elif len(self.english) > 0 and self.english in self.proper_nouns:
                return self.dictionary.dictionary[self.english]["part of speech"]
            else:
                return ""
        except KeyError:
            return ""

    def grade(self):
        """Gets the grade that the word first appears in. Returns String."""
        try:
            if self.is_valid and self.english not in self.proper_nouns:
                return self.dictionary.dictionary[self.english.lower()]["grade"]
            elif len(self.english) > 0 and self.english in self.proper_nouns:
                return self.dictionary.dictionary[self.english]["grade"]
            else:
                return 0
        except KeyError:
            return 0 

    def change_word(self):
        """Changes the word based on its part of speech. Returns None."""
        pos = self.part_of_speech()
        if pos == "noun":
            self.choose_different_word(self.common_nouns) 
        elif pos == "pronoun":
            self.choose_different_word(self.pronouns) 
        elif pos == "verb":
            self.choose_different_word(self.verbs) 
        elif pos == "adjective":
            self.choose_different_word(self.adjectives) 
        elif pos == "adverb":
            self.choose_different_word(self.adverbs) 
        elif pos == "auxverb":
            self.choose_different_word(self.auxverbs) 
        elif pos == "conjunction":
            self.choose_different_word(self.conjunctions) 
        elif pos == "interjection":
            self.choose_different_word(self.interjections)             
        elif pos == "preposition":
            self.choose_different_word(self.prepositions)            
        elif pos == "article":
            self.choose_different_word(self.articles)

    def choose_different_word(self, some_list): 
        """Chooses a different word from a list. Returns None."""
        copy = some_list[:]
        while self.english in copy:
            copy.remove(self.english)
        self.english = random.choice(copy)
        
    def make_plural(self):
        """Makes the word plural if it's a noun or verb. Returns None."""
        if self.english in Lists.foreign_words:
            self.english += "s"
        elif self.english in Lists.irregular_nouns:
            self.english  = Lists.irregular_nouns[self.english] 
        elif self.english[-2:] == "es":
            self.english = self.english
        elif self.english[-1] == "x" \
            or (self.english[-1] == "o" and (self.english[-2] not in self.vowels)):
            self.english += "es"
        elif self.english[-2:] == "ss" \
            or self.english[-2:] == "ch" \
            or self.english[-2:] == "sh" \
            or self.english[-2:] == "zz":
            self.english = self.english + "es"
        elif self.english[-1] == "y" \
            and self.english[-2] not in self.vowels:
            self.english = self.english[:-1]
            self.english += "ies"
        elif self.english[-1] == "f" \
            and self.english != "chef" \
            and self.english != "beef":
            self.english = self.english[:-1] + 'ves'
        elif self.english[-3:-1] == "ff" \
             or self.english [-2:] == "ff":
            self.english =self.english + "s"
        elif self.english[-1:] == "f":
            self.english = self.english[:-2] + "ves"
        else:
            self.english = self.english + "s"

    def base_verb(self):
        """Searches for the base form of a verb. Returns None."""
        for verb in self.verbs:
            for key, value in self.verb_forms.items():
                for k, v in value.items():
                    if v == self.english:
                        return key

    def base_noun(self):
        """Finds the base form of the noun. Returns String."""
        noun = self.english
        if noun in self.dictionary.dictionary.keys() and self.dictionary.dictionary[noun]["part of speech"] == "noun":
            print("FOUND IT == ", noun)
            return noun
        else:
            print("Not found, beginning base noun search.")

        if len(noun) >= 3:
            if noun in self.lists.irregular_nouns:
                print("irregular")
            elif noun in self.lists.same_as_singular:
                print("same as singular")
            elif noun[-2:] == "es":
                if noun[-3] == "v":
                    print("v to f =", noun[:-3])
                    return noun[:-3] + "f"
                elif noun[-3] == "i":
                    print("i to y= ", noun[:-3])
                    return noun[:-3] + "y"
                elif noun[-3] not in self.lists.vowels:
                    print("[-3] not in vowels= ", noun[-3])
                    return noun[:-2]
                elif noun[-3] == "s":
                    print("[-3] is s= ", noun[-3])
                    return noun[:-2]
                elif noun[-3] in self.lists.consonants:
                    return noun[:-1]
                    print("[-3] in consonants= ", noun[-3])
            elif noun[-1] == "s":
                print("noun ends in s", noun)
                return noun[:-1]
        else:
            return ""
            
if __name__ == "__main__":
    word = Word("cats")
    print(word.base_noun())
