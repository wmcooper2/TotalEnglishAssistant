#!/usr/bin/env python3

#custom
from dictionaries import Dictionary

class DictFormat():
    dictionary              = Dictionary()
    max_word_length         = 0 
    max_inner_value_length  = 0
    max_inner_key_length    = 0
    max_page_length         = 6
    outer_key               = 0
    outer_value             = 0
    inner_key               = 0
    inner_value             = 0

    def total_counts(self):
        """Counts all the inner and outer, keys and values. Returns None."""
        for key, value in self.dictionary.dictionary.items():
            self.outer_key += 1
            self.outer_value += 1
            for k, v in value.items():
                self.inner_key += 1
                self.inner_value += 1

        print("ok=", self.outer_key, "ov=", self.outer_value, 
              "ik=", self.inner_key, "iv=", self.inner_value)

    def format_dict(self, path):
        """Formats first line to terminal. Returns None."""
        with open(path, "w+") as my_file:
            for word in self.dictionary.words: 
                word = word
                grade = self.dictionary.dictionary[word]["grade"]
                page = self.dictionary.dictionary[word]["page"]
                part_of_speech = self.dictionary.dictionary[word]["part of speech"]
                japanese = self.dictionary.dictionary[word]["japanese"]
                important = self.dictionary.dictionary[word]["important"]
                my_file.write("{0:<42}{1:^6}{2:>6}{3:>6}{4:^6}{5:<30}{6:<60}".format(str(word), str(grade), str(page), str(important), str(" "), str(part_of_speech), str(japanese)))

