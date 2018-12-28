"""GUI's Vocabulary Tab"""
#stand lib
from pprint import pprint
import random
import time
import tkinter as tk
from tkinter import ttk
from tkinter import Menu

#custom
from vocabutil import *

class VocabularyTab():
    def __init__(self, tab_control):
        self.vocab_tab = ttk.Frame(tab_control)
        tab_control.add(self.vocab_tab, text="Vocabulary")
        tab_control.grid()
        self.language   = tk.StringVar()
        self.test_amt   = tk.IntVar()
        self.q_per_test = tk.IntVar()
        self.std_grade  = tk.IntVar()
        self.lo         = tk.IntVar()
        self.hi         = tk.IntVar()
        self.vocab_list = []
        self.vocab_test = []

        options_frame = ttk.LabelFrame(self.vocab_tab)
        options_frame.grid(column=0, columnspan=2, row=0, padx=6, pady=6)
        
        grade_box = ttk.LabelFrame(options_frame, text="Grade level")
        grade_box.grid(column=0, row=0, padx=6, pady=6)
        self.std_grade_input = ttk.Entry(grade_box, 
            width=SMALLINPUT, textvariable=self.std_grade)
        self.std_grade_input.grid(column=0, row=0, pady=6, padx=6)
        self.std_grade_input.focus()

        page_range_box = ttk.LabelFrame(options_frame, text="Page range")
        page_range_box.grid(column=1, columnspan=2, row=0, padx=6, pady=6)
        from_label = ttk.Label(page_range_box, text="From: ")
        from_label.grid(column=0, row=0, padx=6, pady=6)
        self.from_page = ttk.Entry(page_range_box, 
            width=SMALLINPUT, textvariable=self.lo)
        self.from_page.grid(column=1, row=0, padx=6, pady=6)

        until_label = ttk.Label(page_range_box, text="Until: ")
        until_label.grid(column=2, row=0, sticky=tk.W, padx=6, pady=6)
        self.until_page = ttk.Entry(page_range_box, 
            width=SMALLINPUT, textvariable=self.hi)
        self.until_page.grid(column=3, row=0, padx=6, pady=6)

        language_text = ttk.LabelFrame(self.vocab_tab)
        language_text.grid(column=0, row=1, columnspan=2, pady=6, padx=6)
        english_language = ttk.Radiobutton(language_text, text="English",
            value='english', variable=self.language)
        english_language.grid(column=0, row=0, pady=6, padx=6)
        japanese_language = ttk.Radiobutton(language_text, 
            text=JAPANESE, value='japanese', variable=self.language)
        japanese_language.grid(column=1, row=0, pady=6, padx=6)
        english_and_japanese = ttk.Radiobutton(language_text, 
            text=BOTHLANG, value='english_japanese', 
            variable=self.language)
        english_and_japanese.grid(column=2, row=0, pady=6, padx=6)

        how_many_box = ttk.LabelFrame(self.vocab_tab)
        how_many_box.grid(column=0, columnspan=2, row=2, padx=6, pady=6)
        
        questions_text = ttk.Label(how_many_box,
            text="How many questions per test?")
        questions_text.grid(column=0, row=0, sticky=tk.W, pady=6, padx=6)
        self.q_per_test_input = ttk.Entry(how_many_box, 
            width=SMALLINPUT, textvariable=self.q_per_test)
        self.q_per_test_input.grid(column=1, row=0, pady=6, padx=6,
            sticky=tk.W)
        
        tests_text = ttk.Label(how_many_box, text="How many tests?")
        tests_text.grid(column=0, row=1, sticky=tk.W, pady=6, padx=6)
        self.test_amt_input = ttk.Entry(how_many_box, width=SMALLINPUT, 
            textvariable=self.test_amt)
        self.test_amt_input.grid(column=1, row=1, sticky=tk.W, 
            pady=6, padx=6)

        save_directory_box = ttk.LabelFrame(self.vocab_tab)
        save_directory_box.grid(column=0, columnspan=2, row=3, 
            padx=6, pady=6)
        save_button = ttk.Button(save_directory_box, 
            text="Make Test(s)", command=self.make_vocab_tests)
        save_button.grid(column=0, row=0, padx=6, pady=6)

        reset_button = ttk.Button(save_directory_box, text="Reset", 
            command=self.reset_choices)
        reset_button.grid(column=1, row=0, padx=6, pady=6)

    def valid_vocab_input(self):
        """Validates the user input. Returns Boolean."""
        if in_question_range(self.q_per_test) \
            and in_test_range(self.test_amt) \
            and within_grade_range(self.std_grade) \
            and lang_chosen(self.language) \
            and pages_chosen(self.lo, self.hi):
            return True
        else: return False

    def reset_choices(self):
        """Clears the user's input from the entry widgets. Returns None."""
        self.std_grade_input.delete(0, "end")
        self.from_page.delete(0, "end")
        self.until_page.delete(0, "end")
        self.test_amt_input.delete(0, "end")
        self.q_per_test_input.delete(0, "end")

    def make_vocab_tests(self):
        """Makes all of the vocabulary tests requested by the user.
            Returns None."""
        self.random_vocab()
        save(self.vocab_list, 
            dict(amt=self.test_amt.get(), 
            grade=self.std_grade.get(), 
            lang=self.language.get()))

    def random_vocab(self):
        """Makes a list of randomized words. Returns List."""
        self.reset_vocab()
        e_words    = self.word_filter()
        len_e_words= len(e_words)

        def limit():
            """Checks if amount of words per test reaches the most 
                limiting factor. Returns Boolean"""
            return len(self.vocab_list) >= int(self.q_per_test_input.get()) \
                or len(self.vocab_list) >= len_e_words

        def populate_vocab_list():
            """Populates the vocab list. Returns None."""
            while not limit(): 
                choice = random.choice(e_words)
                if self.language.get() == "english":
                    self.vocab_list.append(choice)
                if self.language.get() == "japanese":
                    self.vocab_list.append(japanese(choice))
                if self.language.get() == "english_japanese":
                    func = random.choice([None, japanese])
                    if func is not None:
                        self.vocab_list.append(japanese(choice))
                    else: self.vocab_list.append(choice)
                e_words.remove(choice)

        populate_vocab_list()
        return

    def reset_vocab(self):
        """Clears the vocab_list attribute. Returns None."""
        self.vocab_list = []

    def word_filter(self):
        """Filters words based on selections. Returns List."""
        words = grade_filter(self.std_grade.get(), DICT)
        return page_filter(self.lo.get(), self.hi.get(), words)

    def quit_(self):
        """Quits the program. Returns None."""
        win.quit()
        win.destroy()

if __name__ == '__main__':
        win = tk.Tk()
        win.title("Test of Vocabulary Tab only")
        tab_control = ttk.Notebook(win)
        menu_bar = Menu(win)
        win.config(menu = menu_bar)
        vocabulary_tab = VocabularyTab(tab_control)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=vocabulary_tab.quit_)
        menu_bar.add_cascade(label="File", menu=file_menu)
        win.mainloop()

