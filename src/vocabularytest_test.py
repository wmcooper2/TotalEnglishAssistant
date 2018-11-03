#!/usr/bin/python3

#stand lib
import unittest

#custom
from vocabularytest import VocabularyTest

class TestMakerUnittest(unittest.TestCase):
    def test_set_words_in_grade_3(self): 
        vocabulary_test = VocabularyTest()
        vocabulary_test.student_grade_level = 3
        vocabulary_test.filter_by_selections()
        test_word = vocabulary_test.words_in_grade[0]
        self.assertEqual(
            int(vocabulary_test.dictionary.dictionary[test_word]["grade"]), 
                vocabulary_test.student_grade_level)

    def test_set_words_in_range__greater_equal(self):
        vocabulary_test = VocabularyTest()
        vocabulary_test.from_page = 0
        vocabulary_test.until_page = 50
        vocabulary_test.filter_by_selections()
        test_word = vocabulary_test.words_in_range[0]
        self.assertGreaterEqual(
            int(vocabulary_test.dictionary.dictionary[test_word]["page"]), 
                vocabulary_test.from_page)

    def test_set_words_in_range__less_equal(self):
        vocabulary_test = VocabularyTest()
        vocabulary_test.from_page = 0
        vocabulary_test.until_page = 50
        vocabulary_test.filter_by_selections()
        test_word = vocabulary_test.words_in_range[0]
        self.assertLessEqual(
            int(vocabulary_test.dictionary.dictionary[test_word]["page"]), 
                vocabulary_test.until_page)

if __name__ == "__main__":
    unittest.main()
    
