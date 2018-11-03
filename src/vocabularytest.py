#!/usr/bin/python3

#stand lib
import datetime
from pathlib import Path
import random
from tkinter import filedialog

#custom
import directories
from lists import Lists
import vocabularytabvalidation as check

class VocabularyTest():
    """Filters the words down to a random selection within
        user-specified parameters, returns None."""
    lists                       = Lists()
    dictionary                  = lists.dictionary
    vocabulary_words            = dictionary.words

    questions_per_test          = 20
    student_grade_level         = 3
    language_choice             = "english"
    from_page                   = 0 
    until_page                  = 500
    test_amount                 = 0

    words_in_range              = [] 
    words_in_grade              = []    
    words_of_language_choice    = []
    test_words                  = []

    word_choice                 = ""
    word_page_number            = 0

    def __init__(self):
        pass

    def set_vocabulary_test_words(self):
        """Makes a single list of randomized words. Returns None."""
        self.filter_by_selections()
        while len(self.test_words) < self.questions_per_test:
            self.test_words.append(random.choice(self.words_of_language_choice))

    def filter_by_selections(self):
        """Filters the words down from page range, grade and language into
            one list. Returns None."""
        self._set_words_in_range()
        self._set_words_in_grade()
        self._set_words_of_language_choice()

    def _set_words_in_range(self):
        """Filters the words by page range. Returns None."""
        self.words_in_range = []
        for word in self.vocabulary_words:
            page_of_word = int(self.dictionary.dictionary[word]["page"])
            if page_of_word >= self.from_page and page_of_word <= self.until_page:
                self.words_in_range.append(word)

    def _set_words_in_grade(self):
        """Filters the words by student grade level. Returns None."""
        self.words_in_grade = []
        grade_level = self.student_grade_level
        for word in self.words_in_range:
            if grade_level == int(self.dictionary.dictionary[word]["grade"]):
                self.words_in_grade.append(word)

    def _set_words_of_language_choice(self):
        """Filters the words by language. Returns None."""
        self.words_of_language_choice = []
        if self.language_choice == "english":
            for word in self.words_in_grade:
                self.words_of_language_choice.append(word)
        elif self.language_choice == "japanese":
            for word in self.words_in_grade:
                self.words_of_language_choice.append(self.dictionary.dictionary[word]["japanese"])
        elif self.language_choice == "english_and_japanese":
            for word in self.words_in_grade:
                language = random.choice(["english", "japanese"])
                if language == "japanese":
                    self.words_of_language_choice.append(self.dictionary.dictionary[word][language])
                elif language == "english":
                    self.words_of_language_choice.append(word)

    def make_name(self, save_location, test_number):
        """Formats the name of the save file. Returns String."""
        name = "{0}_{1}_{2}_{3}".format(
            datetime.datetime.now().strftime('%Y_%m_%d'), 
            self.language_choice.title(),
            "Grade" + str(self.student_grade_level),
            "Test" + str(test_number))
        return name

    def unique_words(self):
        """Filters out any duplicates in self.test_words. Returns None."""
        words_copy = self.test_words[:]
        temp = []
        for word in self.test_words:
            if word not in temp:
                temp.append(word)
        temp.sort()
        self.test_words = temp[:] 

    def save_test(self):
        """Saves test to '~/TotalEnglishAssistant/VocabularyTests'.
           Returns None."""
        save_path = directories.ROOTDIR + directories.VOCABDIR
        tests = self.test_amount
        answer = True
        if answer:
            for counter in range(tests):
                test_number = "_" + str(counter + 1)
                test = Path(self.make_name(save_path, test_number))
                test_path = (save_path/test)
                print("test path = ", test_path)
                if tests is 1:
                    self.single_test(test_path)
                elif tests > 1:
                    self.multiple_tests(test_path)
                else:         
                    print("You need to make 1 or more tests.")
        else:
            check.didnt_write_test()

    def single_test(self, test):
        """Makes a single test. Returns None."""
        self.unique_words()
        with open(test, "w+", encoding = "utf-8") as file:
            try:
                for word in self.test_words:
                    file.write(word)
                    file.write("\n")
            except:
                print("ran out of words")

    def multiple_tests(self, test):
        """Makes multiple tests with random word order. Returns None."""
        self.unique_words()
        vocabulary_copy = self.test_words[:]
        with open(test, "w+", encoding = "utf-8") as file:
            try:
                for counter in range(len(self.test_words)):
                    random_word = random.choice(vocabulary_copy)
                    file.write(random_word)
                    file.write("\n")
                    vocabulary_copy.remove(random_word)
            except:
                print("ran out of more words")

