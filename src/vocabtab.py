"""GUI's Vocabulary Tab"""
# stand lib
from pprint import pprint
import random
import time
import tkinter as tk
from tkinter import ttk
from tkinter import Menu

# custom
from vocabutil import *


class VocabularyTab():
    def __init__(self, tab_control):
        self.vocab_tab = ttk.Frame(tab_control)
        tab_control.add(self.vocab_tab, text="Vocabulary")
        tab_control.grid()

        self.language = tk.StringVar()
        self.test_amt = tk.IntVar()
        self.q_per_test = tk.IntVar()
        self.std_grade = tk.IntVar()
        self.lo = tk.IntVar()
        self.hi = tk.IntVar()
        self.vocab = []
        self.vocab_test = []

        radio = ttk.Radiobutton

        # box 1
        options_frame = ttk.LabelFrame(self.vocab_tab)
        options_frame.grid(column=0, row=1, padx=6, pady=6)

        grade_box = ttk.LabelFrame(options_frame, text="Grade level")
        grade_box.grid(column=0, row=0, padx=6, pady=6)

        self.grade_input = ttk.Entry(grade_box, width=SMALL_INPUT,
                                     textvariable=self.std_grade)
        self.grade_input.grid(column=0, row=0, pady=6, padx=6)

        page_box = ttk.LabelFrame(options_frame, text="Page range")
        page_box.grid(column=1, columnspan=2, row=0, padx=6, pady=6)

        from_label = ttk.Label(page_box, text="From: ")
        from_label.grid(column=0, row=0, padx=6, pady=6)

        self.from_ = ttk.Entry(page_box, width=SMALL_INPUT,
                               textvariable=self.lo)
        self.from_.grid(column=1, row=0, padx=6, pady=6)

        until_label = ttk.Label(page_box, text="Until: ")
        until_label.grid(column=2, row=0, sticky=tk.W, padx=6, pady=6)

        self.until = ttk.Entry(page_box, width=SMALL_INPUT,
                               textvariable=self.hi)
        self.until.grid(column=3, row=0, padx=6, pady=6)

        # box 2
        lang_box = ttk.LabelFrame(self.vocab_tab)
        lang_box.grid(column=0, row=2, pady=6, padx=6)

        eng_lang = radio(lang_box, text="English", value='english',
                         variable=self.language)
        eng_lang.grid(column=0, row=0, pady=6, padx=6)

        jap_lang = radio(lang_box, text=JAPANESE, value='japanese',
                         variable=self.language)
        jap_lang.grid(column=1, row=0, pady=6, padx=6)

        eng_and_jap = radio(lang_box, text=BOTH_LANG,
                            value='english_japanese',
                            variable=self.language)
        eng_and_jap.grid(column=2, row=0, pady=6, padx=6)

        # box 3
        how_many_box = ttk.LabelFrame(self.vocab_tab)
        how_many_box.grid(column=0, row=3, padx=6, pady=6)

        questions_text = ttk.Label(how_many_box,
                                   text="How many questions per test?")
        questions_text.grid(column=0, row=0, sticky=tk.W, pady=6, padx=6)

        self.q_per_t = ttk.Entry(how_many_box, width=SMALL_INPUT,
                                 textvariable=self.q_per_test)
        self.q_per_t.grid(column=1, row=0, pady=6, padx=6, sticky=tk.W)

        tests_text = ttk.Label(how_many_box, text="How many tests?")
        tests_text.grid(column=0, row=1, sticky=tk.W, pady=6, padx=6)

        self.test_input = ttk.Entry(how_many_box, width=SMALL_INPUT,
                                    textvariable=self.test_amt)
        self.test_input.grid(column=1, row=1, sticky=tk.W, pady=6, padx=6)
        # box 4
        butt_box = ttk.LabelFrame(self.vocab_tab)
        butt_box.grid(column=0, row=4, padx=6, pady=6)

        save_button = ttk.Button(butt_box, text="Make Test(s)",
                                 command=self.make_vocab_tests)
        save_button.grid(column=0, row=0, padx=6, pady=6)

        reset_button = ttk.Button(butt_box, text="Reset",
                                  command=self.reset_gui)
        reset_button.grid(column=1, row=0, padx=6, pady=6)

        self.grade_input.focus()

    def valid_vocab_input(self) -> bool:
        """Validates the user input. Returns Boolean."""
        if in_question_range(self.q_per_test) \
            and in_test_range(self.test_amt) \
            and valid_grade(self.std_grade) \
            and valid_lang(self.language) \
            and pages_chosen(self.lo, self.hi):
            return True
        else:
            return False

    def reset_gui(self) -> None:
        """Clears selections from gui. Returns None."""
        self.grade_input.delete(0, "end")
        self.from_.delete(0, "end")
        self.until.delete(0, "end")
        self.test_input.delete(0, "end")
        self.q_per_t.delete(0, "end")

    def make_vocab_tests(self) -> None:
        """Makes vocabulary tests. Returns None."""
        # message to user, redraw label "making tests now, please wait."
        grade = self.std_grade.get()
        words = list(DICT.keys())
        lang = self.language.get()
        questions = self.q_per_test.get()
        test_amt = self.test_amt.get()
        lo_page = self.lo.get()
        hi_page = self.hi.get()

        by_grade = grade_filter(grade, words)
        by_page = page_filter(lo_page, hi_page, by_grade)

        if len(by_page) < questions:
            not_enough_words()
        else:
            vocab = vocabulary(by_page, questions, lang)

        for num in range(test_amt):
            file_ = test_name(num, grade, lang)
            save_random_order(vocab, file_)
        # message to user, "finished making tests, Check the Vocab dir"
        return None

    def quit_(self) -> None:
        """Quits the program. Returns None."""
        win.quit()
        win.destroy()
        return None


if __name__ == '__main__':
    win = tk.Tk()
    win.title("Test of Vocabulary Tab only")
    tab_control = ttk.Notebook(win)
    menu_bar = Menu(win)
    win.config(menu=menu_bar)
    vocabulary_tab = VocabularyTab(tab_control)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=vocabulary_tab.quit_)
    menu_bar.add_cascade(label="File", menu=file_menu)
    win.mainloop()
