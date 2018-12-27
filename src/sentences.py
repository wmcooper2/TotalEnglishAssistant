"""Sentence Module for senttab.py"""
#move this code into senttab.py

#custom
from sentencesutil import *

class Sentence():
    def __init__(self, sentence):
        self.sentence = sentence
        self.words = []
        self.set_words()

    def __str__(self):
        return "A Sentence Object: {}.".format(self.sentence)

    def set_words (self):
        """Sets up the word list from the sentence. Returns None."""
        for element in self.sentence.split():
            self.words.append(element)
            
    def change_all_words(self):
        """Changes each word in the word list randomly. Returns None."""
        for element in self.words:
            word_index = self.words.index(element)
            word = Word(element)
            word.change_word()
            self.words[word_index] = word.english

if __name__ == "__main__":
    sentence = Sentence("I like cats")
    sentence.change_all_words()
    for word in sentence.words:
        print(word)
    
    
