#!/usr/bin/python3

#stand lib
import datetime
from pathlib import Path
import random
from tkinter import filedialog

#custom
#import directories
#import vocabularytabvalidation as check
from words import *
from dictionaries import *

def make_name(save_location, test_number):
    """Formats the name of the save file. Returns String."""
    name = "{0}_{1}_{2}_{3}".format(
        datetime.datetime.now().strftime('%Y_%m_%d'), 
        language_choice.title(),
        "Grade" + str(student_grade_level),
        "Test" + str(test_number))
    return name

def unique_words():
    """Filters out any duplicates in test_words. Returns None."""
    words_copy = test_words[:]
    temp = []
    for word in test_words:
        if word not in temp:
            temp.append(word)
    temp.sort()
    test_words = temp[:] 

def save_test():
    """Saves test to '~/TotalEnglishAssistant/VocabularyTests'.
       Returns None."""
    save_path = directories.ROOTDIR + directories.VOCABDIR
    tests = test_amount
    answer = True
    if answer:
        for counter in range(tests):
            test_number = "_" + str(counter + 1)
            test = Path(make_name(save_path, test_number))
            test_path = (save_path/test)
            print("test path = ", test_path)
            if tests is 1:
                single_test(test_path)
            elif tests > 1:
                multiple_tests(test_path)
            else:         
                print("You need to make 1 or more tests.")
    else:
        check.didnt_write_test()

def single_test(test):
    """Makes a single test. Returns None."""
    unique_words()
    with open(test, "w+", encoding = "utf-8") as file:
        try:
            for word in test_words:
                file.write(word)
                file.write("\n")
        except:
            print("ran out of words")

def multiple_tests(test):
    """Makes multiple tests with random word order. Returns None."""
    unique_words()
    vocabulary_copy = test_words[:]
    with open(test, "w+", encoding = "utf-8") as file:
        try:
            for counter in range(len(test_words)):
                random_word = random.choice(vocabulary_copy)
                file.write(random_word)
                file.write("\n")
                vocabulary_copy.remove(random_word)
        except:
            print("ran out of more words")

