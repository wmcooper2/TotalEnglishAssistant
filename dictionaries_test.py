#!/usr/bin/python3
import unittest
from dictionaries import Dictionary
class DictionaryTests(unittest.TestCase):

    dictionary = Dictionary()

    def test_is_dictionary_instance(self):
        self.assertIsInstance(self.dictionary, Dictionary)

    def test_size_unchanged(self):
        self.dictionary.sort_words()
        self.assertEqual(self.dictionary.size, 1450)

    def test_more_than_zero_entries(self):
        self.dictionary.sort_words()
        self.assertGreaterEqual(self.dictionary.size, 0)

    def test_word_in_dictionary__cat(self):
        self.assertTrue("cat" in self.dictionary.words)

    def test_filter_words_by_grade__1(self):
        word_count = self.dictionary.filter_words_by_grade(1)
        self.assertEqual(word_count, 610)
            
    def test_filter_words_by_grade__2(self):
        word_count = self.dictionary.filter_words_by_grade(2)
        self.assertEqual(word_count, 505)

    def test_filter_words_by_grade__3(self):
        word_count = self.dictionary.filter_words_by_grade(3)
        self.assertEqual(word_count, 335)

if __name__ == "__main__":
    unittest.main()
