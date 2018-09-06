#!/usr/bin/python3
import sys
if "./data" not in sys.path:
    sys.path.append("./data")

import json
import random
import tkinter as tk
from tkinter import ttk
from pathlib import Path

class Dictionary():
    """Creates an instance of the chosen dictionary, returns none."""
    default_dict_path = "./src/data/totalenglish123.json" 
    default_dict_name = "totalenglish123"
    default_dict = "totalenglish123.json"
    default_entry = {"not found":"not found"}
    new_dictionary_name = ""
    
    def __init__(self):
        """Prepares word list of the dictionary, returns None."""
        self.dictionary = {}
        self.load_dictionary()
        self.words = []
        self.sort_words()
        self.size = len(self.words)

    def save_dictionary(self, save_this, file_path):
        """Saves the dictionary to a user-specified location, returns None."""
        dump_here = open(file_path, "w+")
        json.dump(save_this, dump_here)
        dump_here.close()

    def load_dictionary(self):
        """Loads the dictionary from the path set in the instance, returns None."""
        with open(self.default_dict_path) as file_object:
            self.dictionary = json.load(file_object)

    def edit_entry(self, key, entry):
        """Edits an entry in the dictionary, returns None."""
        self.dictionary[key] = entry
        self.save_dictionary(self.dictionary, self.default_dict_path)

    def get_entry(self, word):
        """Sets a single entry, returns None."""
        if word.lower() in self.dictionary:
            return self.dictionary[word]
        else:
            try:
                return self.dictionary[word]
            except KeyError:
                return self.default_entry

    def sort_words(self):
        """Sorts the 'words' list, returns None."""
        for key in self.dictionary.keys():
            self.words.append(key)
        self.words = sorted(self.words)

    def get_size(self):
        """Gets the number of entries in the dictionary, returns String."""
        return self.size

    def filter_words_by_grade(self, grade):
        """Filters the 'words' list by user-specified student grade level,
            returns String."""
        words = []
        for word in self.words:
            if grade == int(self.dictionary[word]["grade"]):
                words.append(word)
        return len(words)

    def filter_words_by_punctuation(self):
        """Filters the 'words' list of words with punctutation, returns List."""
        list_ = []
        for word in self.words:
            if "'" in word:
                list_.append(word)
        return list_

    def new_dictionary(self):
        """Makes a new, custom dictionary, returns None."""
        print("make a new dictionary")
        
if __name__ == "__main__":
    d = Dictionary()
#    print(d.get_entry("well"))
    print(d.dictionary_name)
