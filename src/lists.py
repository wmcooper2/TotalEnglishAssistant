#!/usr/bin/python3
import sys
if "./data" not in sys.path:
    sys.path.append("./data")
from dictionaries import Dictionary
import string
import verbforms 
import extranouns 
import extragrammar 
import irregularnouns 
import extracategories 
import targetsentences 
import extraforeignwords 

class Lists():
    """Container-class for commonly used categories of words, returns None."""
    dictionary = Dictionary()
    alphabet = string.ascii_letters
    punctuation = string.punctuation
    good_punctuation = extragrammar.good_punctuation
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase

    book_1_target_sentences = targetsentences.book_1
    book_2_target_sentences = targetsentences.book_2
    book_3_target_sentences = targetsentences.book_3

    vowels = extragrammar.vowels
    consonants = extragrammar.consonants
    plural_be_verbs = extragrammar.plural_be_verbs
    singular_be_verbs = extragrammar.singular_be_verbs
    be_verbs = extragrammar.be_verbs
    plural_pronouns = extragrammar.plural_pronouns
    singular_pronouns = extragrammar.singular_pronouns
    possessive_pronoun_objects = extragrammar.possessive_pronoun_objects
    parts_of_speech = extragrammar.parts_of_speech
    demonstrative_adjectives = extragrammar.demonstrative_adjectives
    possessive_adjectives = extragrammar.possessive_adjectives

    foreign_words = extraforeignwords.foreign_words
    
    irregular_nouns = irregularnouns.irregular_nouns
    
    pets = extranouns.pets
    animals = extranouns.animals
    desserts = extranouns.desserts
    verb_forms = verbforms.verb_forms
    vegetables = extranouns.vegetables
    common_nouns = extranouns.common_nouns
    literary_nouns = extranouns.literary_nouns
    parts_of_school = extranouns.parts_of_school
    countable_nouns = extranouns.countable_nouns
    burnable_things = extranouns.burnable_things
    everyday_objects = extranouns.everyday_objects
    same_as_singular = extranouns.same_as_singular
    musical_instruments = extranouns.musical_instruments
    country_foods = extranouns.country_foods
    unique_objects = extranouns.unique_objects
    
    occupations = extracategories.occupations
    tangible_things = extracategories.tangible_things
    foods = extracategories.foods
    fruit = extracategories.fruit
    beverages = extracategories.beverages
    languages = extracategories.languages
    work_locations = extracategories.work_locations
    names = extracategories.names
    days_of_the_week = extracategories.days_of_the_week
    countries = extracategories.countries
    tv_programs = extracategories.tv_programs
    school_events = extracategories.school_events
    school_clubs = extracategories.school_clubs
    school_subjects = extracategories.school_subjects
    sports = extracategories.sports
    seasons = extracategories.seasons
    months = extracategories.months
    person_subjects = extracategories.person_subjects
    ordinal_numbers = extracategories.ordinal_numbers
    feelings = extracategories.feelings    
    personalities = extracategories.personalities

    nouns = []
    verbs = []
    adverbs = []
    auxverbs = []
    articles = []
    pronouns = []
    adjectives = []
    proper_nouns = []    
    conjunctions = []
    prepositions = []
    interjections = []
    
    def __init__(self):
        self.initialize_nouns()
        self.initialize_verbs()
        self.initialize_adverbs()
        self.initialize_auxverbs()
        self.initialize_articles()
        self.initialize_pronouns()
        self.initialize_adjectives()
        self.initialize_proper_nouns()
        self.initialize_conjunctions()
        self.initialize_prepositions()
        self.initialize_interjections()

    def initialize_nouns(self):
        """Filters the nouns into an easy to access list, returns None."""
        for word in self.dictionary.dictionary.keys():
            if self.dictionary.dictionary[word]["part of speech"] == "noun":
                self.nouns.append(word)
                
    def initialize_verbs(self):
        """Filters the verbs into an easy to access list, returns None."""
        for word in self.dictionary.dictionary.keys():
            if self.dictionary.dictionary[word]["part of speech"] == "verb":
                self.verbs.append(word)
                
    def initialize_adverbs(self):
        """Filters the adverbs into an easy to access list, returns None."""
        for word in self.dictionary.dictionary.keys():
            if self.dictionary.dictionary[word]["part of speech"] == "adverb":
                self.adverbs.append(word)

    def initialize_auxverbs(self):
        """Filters the auxilary verbs into an easy to access list, returns None."""
        for word in self.dictionary.dictionary.keys():
            if self.dictionary.dictionary[word]["part of speech"] == "auxverb":
                self.auxverbs.append(word)

    def initialize_articles(self):
        """Filters the articles into an easy to access list, returns None."""
        for word in self.dictionary.dictionary.keys():
            if self.dictionary.dictionary[word]["part of speech"] == "article":
                self.articles.append(word)

    def initialize_pronouns(self):
        """Filters the pronouns into an easy to access list, returns None."""
        for word in self.dictionary.dictionary.keys():
            if self.dictionary.dictionary[word]["part of speech"] == "pronoun":
                self.pronouns.append(word)
                
    def initialize_adjectives(self):
        """Filters the adjectives into an easy to access list, returns None."""
        for word in self.dictionary.dictionary.keys():
            if self.dictionary.dictionary[word]["part of speech"] == "adjective":
                self.adjectives.append(word)

    def initialize_proper_nouns(self):
        """Filters the proper nouns into an easy to access list, returns None."""
        for word in self.dictionary.dictionary.keys():
            if word[0] in self.uppercase:
                self.proper_nouns.append(word)
                
    def initialize_conjunctions(self):
        """Filters the conjunctions into an easy to access list, returns None."""
        for word in self.dictionary.dictionary.keys():
            if self.dictionary.dictionary[word]["part of speech"] == "conjunction":
                self.conjunctions.append(word)

    def initialize_prepositions(self):
        """Filters the prepositions into an easy to access list, returns None."""
        for word in self.dictionary.dictionary.keys():
            if self.dictionary.dictionary[word]["part of speech"] == "preposition":
                self.prepositions.append(word)    

    def initialize_interjections(self):
        """Filters the interjections into an easy to access list, returns None."""
        for word in self.dictionary.dictionary.keys():
            if self.dictionary.dictionary[word]["part of speech"] == "interjection":
                self.interjections.append(word)
    
if __name__ == "__main__":
    lists = Lists()
    print(lists.auxverbs)
