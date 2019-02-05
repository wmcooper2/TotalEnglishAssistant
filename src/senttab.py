"""GUI Sentences Tab."""
#stand lib
import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import Menu

#custom
from sentutil import *

class SentenceTab():
    """Creates the 'Sentence' tab in the GUI, returns None."""
    original_sent   = []
    no_punct_sent   = []
    result_labels   = []
    results_rows    = []
    results_dict    = {}

    def __init__(self, tab_control):
        """Draws the widgets in the 'Sentences' tab. Returns None."""
        self.sentence_tab = ttk.Frame(tab_control)
        tab_control.add(self.sentence_tab, text = "Sentences")
        tab_control.grid()
        
        self.from_page = tk.IntVar()
        self.until_page = tk.IntVar()
        self.student_grade_level = tk.IntVar()

        input_frame = ttk.LabelFrame(self.sentence_tab, 
            text="Enter any sentence")
        input_frame.grid(column=0, row=1, padx=6, pady=6)		
        self.sent_input = ttk.Entry(input_frame, 
            width=SENTWIDGETLEN)
        self.sent_input.grid(column=0, row=0, columnspan=2, 
            padx=6, pady=6)
        
        check_sentence_button = ttk.Button(input_frame, text="Check", 
            command=self.results)
        check_sentence_button.grid(column=0, row=1, padx=6, pady=6)

        reset_button = ttk.Button(input_frame, text="Reset", 
            command=self.reset_choices)
        reset_button.grid(column=1, row=1, padx=6, pady=6)

        self.draw_res_fr()

    def quit_(self):
        """Quits the program. Returns None."""
        win.quit()
        win.destroy()

    def results(self):
        """Shows results of input sentence in the GUI. Returns None."""
        self.reset_res_fr()
        self.draw_res_fr()
#        self.break_up_original_sent()
#        self.break_up_no_punct_sent()
        self.original_sent = self.sent_input.get()
        self.results_rows = get_results(self.res_fr, self.original_sent)
        self.draw_results_labels()
        self.draw_results_rows()

    def draw_results_rows(self):
        """Draws the result/button groups to the GUI. Returns None."""
        counter = 1
        for group in self.results_rows:
            group["result"].grid(column=counter, row=0, padx=6, pady=6)
            group["grade"].grid(column=counter, row=1, padx=6, pady=6)
            group["page"].grid(column=counter, row=2, padx=6, pady=6)
            group["verb"].grid(column=counter, row=3, padx=6, pady=6)
            group["noun"].grid(column=counter, row=4, padx=6, pady=6)
            counter = counter + 1

    def draw_results_labels(self):
        """Draws the row labels for the results widget. Returns None."""
        ttk.Label(self.res_fr, text="given word:").grid(column=0, 
            row=0, padx=6, pady=6, sticky=tk.E)
        ttk.Label(self.res_fr, text="grade:").grid(column=0, 
            row=1, padx=6, pady=6, sticky=tk.E)
        ttk.Label(self.res_fr, text="page:").grid(column=0, row=2, 
            padx=6, pady=6, sticky=tk.E)
        ttk.Label(self.res_fr, text="base verb:").grid(column=0, 
            row=3, padx=6, pady=6, sticky=tk.E)
        ttk.Label(self.res_fr, text="singular noun:").grid(column=0, 
            row=4, padx=6, pady=6, sticky=tk.E)

    def reset_res_fr(self):
        """Removes the results frame from the GUI. Returns None."""
        self.res_fr.grid_forget()

    def draw_res_fr(self):
        """Draws the results frame to the GUI. Returns None."""
        self.res_fr = ttk.LabelFrame(self.sentence_tab, 
            text="Results" )
        self.res_fr.grid(column=0, row=2, padx=6, pady=6)        

    def break_up_no_punct_sent(self):
        """Adds no-punct words to self.user_sentence. Returns None."""
        self.no_punct_sent = []  #clear the stored values
        for word in self.sent_input.get().split(" "):
            self.no_punct_sent.append(remove_punctuation(word))
    
    def break_up_original_sent(self):
        """Breaks up user's sentence by spaces. Returns None."""
        self.original_sent = []
        for word in self.sent_input.get().split(" "):
            self.original_sent.append(word)
        
    def reset_choices(self):
        """Clears user's input/results from widgets. Returns None."""
        self.sent_input.delete(0, "end")
        self.reset_res_fr()

class Sentence():
    def __init__(self, sentence):
        self.sentence   = sentence
        self.words      = []
        self.set_words()

    def __str__(self):
        return "A Sentence Object: {}.".format(self.sentence)

    def set_words (self):
        """Sets up the word list from the sentence. Returns None."""
        for element in self.sentence.split(): self.words.append(element)
    
    def change_word(self, word):
        pass

    def change_all_words(self):
        """Changes words randomly. Returns None."""
        for element in self.words:
            word_index = self.words.index(element)
            word = Word(element)
            word.change_word()
            self.words[word_index] = word.english

if __name__ == '__main__':
    win             = tk.Tk()
    win.title("Test of Sentence Tab only")
    tab_control     = ttk.Notebook(win)
    menu_bar        = Menu(win)
    win.config(menu=menu_bar)
    sentence_tab    = SentenceTab(tab_control)
    file_menu       = Menu(menu_bar, tearoff = 0)
    file_menu.add_command(label="Exit", command=sentence_tab.quit_)
    menu_bar.add_cascade(label="File", menu=file_menu)
    win.mainloop()
