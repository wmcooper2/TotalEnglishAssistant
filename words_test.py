#!/usr/bin/python3
import string
import unittest
from words import Word

class WordTest(unittest.TestCase):
    
    def test_is_Word_instance(self):
        word = Word("cat")
        self.assertIsInstance(word, Word)

    def test_two_Word_instances_are_different(self):
        first_word = Word("cat")
        second_word = Word("cat")
        self.assertNotEqual(id(first_word), id(second_word))
            
    def test_is_word_string(self):
        word = Word("cat")
        self.assertEqual(type(word.english), str)

    def test_no_punctuation(self):
        word = Word("cat")
        has_punctuation = True
        for character in word.english:
            if character in word.punctuation:
                has_punctuation = True
        self.assertFalse(not has_punctuation)

    def test_at_least_one_vowel(self):
        word = Word("cat")
        has_vowel = False
        for character in word.english:
            if character in word.vowels:
                has_vowel = True
        self.assertTrue(has_vowel)

    def test_at_least_one_consonant(self):
        word = Word("cat")
        has_consonant = False
        for character in word.english:
            if character in word.consonants:
                has_consonant = True
        self.assertTrue(has_consonant)

    def test_is_all_lowercase(self):
        word = Word("cat")
        is_lowercase = True
        for character in word.english:
            is_lowercase = (character in string.ascii_lowercase)
        self.assertTrue(is_lowercase)

    def test_is_proper_noun(self):
        word = Word("Peru")
        self.assertEqual(word.proper_noun(), True)

    def test_length_greater_than_zero(self):
        word = Word("cat")
        self.assertGreater(len(word.english), 0)
        
    def test_length_less_than_fifty(self):
        word = Word("cat")
        self.assertLess(len(word.english), 50)

    def test_has_no_digits(self):
        word = Word("cat")
        has_numbers = []
        for character in word.english:
            if character in word.numbers:
                has_numbers.append(True)
            else:
                has_numbers.append(False)
        self.assertFalse(any(has_numbers))

    def test_remove_punctuation_from_end_of_word(self):
        word = Word("cats?!")
        word.remove_punctuation()
        self.assertEqual(word.english, "cats")

    def test_remove_punctuation_from_beginning_of_word(self):
        word = Word("!?cats")
        word.remove_punctuation()
        self.assertEqual(word.english, "cats")
        
    def test_remove_all_punctuation(self):
        word = Word('!"#$%&()*+,./:;<=>?@[\\]^_`{|}~')
        word.remove_punctuation()
        self.assertEqual(word.english, "")

    def test_change_word__noun(self):
        word = Word("cat")
        word.change_word()
        self.assertNotEqual(word.english, "cat")

    def test_change_word__pronoun(self):
        word = Word("I")
        new_word = ""
        word.change_word()
        self.assertNotEqual(word.english, "I")

    def test_change_word__verb(self):
        word = Word("swim")
        word.change_word()
        self.assertNotEqual(word.english, "swim")
        
    def test_change_word__adjective(self):
        word = Word("smart")
        word.change_word()
        self.assertNotEqual(word.english, "smart")

    def test_change_word__adverb(self):
        word = Word("clearly")
        word.change_word()
        self.assertNotEqual(word.english, "clearly")

    def test_change_word__auxverb(self):
        word = Word("may")
        word.change_word()
        self.assertNotEqual(word.english, "may")

    def test_change_word__conjunction(self):
        word = Word("or")
        word.change_word()
        self.assertNotEqual(word.english, "or")

    def test_change_word__interjection(self):
        word = Word("hi")
        word.change_word()
        self.assertNotEqual(word.english, "hi")

    def test_change_word__preposition(self):
        word = Word("under")
        word.change_word()
        self.assertNotEqual(word.english, "under")

    def test_change_word__article(self):
        word = Word("a")
        word.change_word()
        self.assertNotEqual(word.english, "a")

    def test_part_of_speech__exists(self):
        word = Word("cat")
        self.assertEqual(word.part_of_speech(), "noun")
    
    def test_part_of_speech__doesnt_exist(self):
        word = Word("potato")
        self.assertNotEqual(word.part_of_speech(), False)

    def test_set_word(self):
        word = Word("cat")
        self.assertEqual(word.english, "cat")

    def test_make__a_ending(self):
        word = Word("banana")
        word.make_plural()
        self.assertEqual(word.english, "bananas")

    def test_make_plural__e_ending(self):
        word = Word("tape")
        word.make_plural()
        self.assertEqual(word.english, "tapes")

    def test_make_plural_o_ending(self):
        word = Word("go")
        word.make_plural()
        self.assertEqual(word.english, "goes")

    def test_make_plural_x_ending(self):
        word = Word("box")
        word.make_plural()
        self.assertEqual(word.english, "boxes")

    def test_make_plural__f_ending(self):
        word = Word("calf")
        word.make_plural()
        self.assertEqual(word.english, "calves")

    def test_make_plural__fe_ending(self):
        word = Word("knife")
        word.make_plural()
        self.assertEqual(word.english, "knives")

    def test_make_plural__ss_ending(self):
        word = Word("pass")
        word.make_plural()
        self.assertEqual(word.english, "passes")

    def test_make_plural__sh_ending(self):
        word = Word("push")
        word.make_plural()
        self.assertEqual(word.english, "pushes")

    def test_make_plural__zz_ending(self):
        word = Word("buzz")
        word.make_plural()
        self.assertEqual(word.english, "buzzes")

    def test_make_plural__word_not_in_dictionary_doesnt_become_hashtags(self):
        word = Word("Taz")
        word.make_plural()
        self.assertNotEqual(word.english, "###")

    def test_make_plural_ch_ending(self):
        word = Word("lunch")
        word.make_plural()
        self.assertEqual(word.english, "lunches")

    def test_make_plural__consonant_and_y_ending(self):
        word = Word("party")
        word.make_plural()
        self.assertEqual(word.english, "parties")

    def test_make_plural__vowel_and_y_ending(self):
        word = Word("stay")
        word.make_plural()
        self.assertEqual(word.english, "stays")

    def test_make_plural__foreign_word(self):
        word = Word("piano")
        word.make_plural()
        self.assertEqual(word.english, "pianos")

    def test_plural__consonant_ending(self):
        word = Word("cat")
        word.make_plural()
        self.assertEqual(word.english, "cats")

    def test_make_plural__irregular_word(self):
        word = Word("beau")
        word.make_plural()
        self.assertEqual(word.english, "beaux")

    def test_make_plural__giraffe(self):
        word = Word("giraffe")
        word.make_plural()
        self.assertEqual(word.english, "giraffes")

    def test_base_noun__hamburgers(self):
        word = Word("hamburgers")
        self.assertEqual(word.base_noun(), "hamburger")

    def test_base_noun__cats(self):
        word = Word("cats")
        self.assertEqual(word.base_noun(), "cat")

    def test_base_noun__giraffes(self):
        word = Word("giraffes")
        self.assertEqual(word.base_noun(), "giraffe")

    def test_base_noun__lunches(self):
        word = Word("lunches")
        self.assertEqual(word.base_noun(), "lunch")

    def test_base_noun__flies(self):
        word = Word("flies")
        self.assertEqual(word.base_noun(), "fly")

    def test_base_noun__boxes(self):
        word = Word("boxes")
        self.assertEqual(word.base_noun(), "box")



if __name__ == "__main__":
    unittest.main()
