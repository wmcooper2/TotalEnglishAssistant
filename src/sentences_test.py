#!/usr/bin/python3
import copy
import unittest
from sentences import Sentence

class SentencesTest(unittest.TestCase):

    def test_change_all_words(self):
        new_sentence = Sentence("I like cats")
        old_sentence = copy.copy(new_sentence)
        booleans = []
        new_sentence.change_all_words()
        for word in old_sentence.words:
            booleans.append(word in new_sentence.words)
        self.assertTrue(any(booleans))

    def test_initialize_words(self):
        sentence = Sentence("I like cats")
        for word in sentence.words:
            self.assertTrue(type(word), object)

    

if __name__ == "__main__":
    unittest.main()
