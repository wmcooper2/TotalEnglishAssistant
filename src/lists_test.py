#!/usr/bin/python3

#stand lib
import unittest

#custom
from lists import Lists

class ListsTest(unittest.TestCase):
    lists = Lists()

    def test_has_dictionary(self):
        self.assertEqual(type(self.lists.dictionary.dictionary), dict)

    def test_can_find_dictionary_words(self):
        self.assertTrue(len(self.lists.dictionary.words) > 0)

    def test_has_alphabet_attribute(self):
        self.assertEqual(len(self.lists.alphabet), 52)

    def test_has_punctuation_attribute(self):
        self.assertEqual(len(self.lists.punctuation), 32)
        
    def test_has_uppercase_attribute(self):
        self.assertEqual(len(self.lists.uppercase), 26)
        self.assertTrue("A" in self.lists.uppercase)

    def test_has_lowercase_attribute(self):
        self.assertEqual(len(self.lists.lowercase), 26)
        self.assertTrue("a" in self.lists.lowercase)

    def test_has_nouns(self):
        self.assertTrue(len(self.lists.nouns) > 0)

    def test_has_verbs(self):
        self.assertTrue(len(self.lists.verbs) > 0)

    def test_has_adverbs(self):
        self.assertTrue(len(self.lists.adverbs) > 0)

    def test_has_auxverbs(self):
        self.assertTrue(len(self.lists.auxverbs) > 0)

    def test_has_articles(self):
        self.assertTrue(len(self.lists.articles) > 0)

    def test_has_pronouns(self):
        self.assertTrue(len(self.lists.pronouns) > 0)

    def test_has_adjectives(self):
        self.assertTrue(len(self.lists.adjectives) > 0)

    def test_has_proper_nouns(self):
        self.assertTrue(len(self.lists.proper_nouns) > 0)

    def test_has_conjunctions(self):
        self.assertTrue(len(self.lists.conjunctions) > 0)

    def test_has_prepositions(self):
        self.assertTrue(len(self.lists.prepositions) > 0)

    def test_has_interjections(self):
        self.assertTrue(len(self.lists.interjections) > 0)

    def test_has_book_1_target_sentences(self):
        self.assertTrue(len(self.lists.book_1_target_sentences) > 0)

    def test_has_book_2_target_sentences(self):
        self.assertTrue(len(self.lists.book_2_target_sentences) > 0)

    def test_has_book_3_target_sentences(self):
        self.assertTrue(len(self.lists.book_3_target_sentences) > 0)

    def test_has_pets(self):
        self.assertTrue(len(self.lists.pets) > 0)

    def test_has_animals(self):
        self.assertTrue(len(self.lists.animals) > 0)

    def test_has_desserts(self):
        self.assertTrue(len(self.lists.desserts) > 0)

    def test_has_verb_forms(self):
        self.assertTrue(len(self.lists.verb_forms) > 0)

    def test_has_vegetables(self):
        self.assertTrue(len(self.lists.vegetables) > 0)

    def test_has_common_nouns(self):
        self.assertTrue(len(self.lists.common_nouns) > 0)

    def test_has_literary_nouns(self):
        self.assertTrue(len(self.lists.literary_nouns) > 0)

    def test_has_parts_of_school(self):
        self.assertTrue(len(self.lists.parts_of_school) > 0)

    def test_has_countable_nouns(self):
        self.assertTrue(len(self.lists.countable_nouns) > 0)

    def test_has_burnable_things(self):
        self.assertTrue(len(self.lists.burnable_things) > 0)

    def test_has_everyday_objects(self):
        self.assertTrue(len(self.lists.everyday_objects) > 0)

    def test_has_irregular_nouns(self):
        self.assertTrue(len(self.lists.irregular_nouns) > 0)

    def test_has_musical_instruments(self):
        self.assertTrue(len(self.lists.musical_instruments) > 0)

if __name__ == "__main__":
    unittest.main()
