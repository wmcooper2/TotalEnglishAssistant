#!/usr/bin/python3
import random
from words import Lists
#import vocabularytab as vocabulary_tab
import sys
import tkinter as tk
from tkinter import ttk
import random

class Test():

    def __init__(self):
        self.narabikae_test = []
            
    def __init__(self):
        pass
    
    def narabiKaeMondai(datafile, write2file, beginning = 0, ending = 200):
        """INPUT: file to read from, file to write to, beginning page, ending page
                RETURN: NONE
                OUTPUT: Word jumbles for students to practice forming correct sentences.
        """
        #READ FROM FILE, REMOVE PUNCTUATION
        tempPrint = getLinesFromFile(datafile, beginning, ending) #put lines from file into a list, each line is an element
        sansPunct = removePunctuation(tempPrint) #remove punctuation from all the element-sentences
        
        #SPLIT, RANDOMIZE, ADD TO LIST, SHOW RESULTS IN TERMINAL
        for sentence in sansPunct:
                newSentence = splitSentence(sentence) #split each sentence into word-elements
                randomsentence = makeRandom(newSentence)#randomize the order of the word-elements
                randomizedSentenceList.append(randomsentence)
                narabikaeList.append(randomsentence)
                print('randomsentence: ', randomsentence)#write the randomized word-element-order sentences to a file
        return narabikaeList

    def narabiKaeMondai2(inputfile):
        """
                INPUT: TEXT FILE
                RETURN: LIST
                
                PURPOSE: load sentences from the text file, split those sentences, then add slashes between the words, and a bracket around the whole sentence.
        """
        bracketedsentenceList = []
        randomizedSentenceList = []
        randomized = []
        #READ FROM FILE, PUT INTO LIST, SHOW IN TERMINAL
        tempPrint = getLinesFromFile2(inputfile)
        listprint(tempPrint) #print to terminal	
        
        ##SPLIT, RANDOMIZE, ADD TO LIST
        for sentence in tempPrint:
                newsentence = sentence.split(' / ')
                randomsentence = makeRandom(newsentence) 
                randomizedSentenceList.append(randomsentence)
        ##ADD SLASHES AND BRACKETS, ASSEMBLE FINAL LIST
        for sentence in randomizedSentenceList:
                bracketedsentence = ' / '.join(sentence)
                firstbracket = '[ '
                firstbracket += bracketedsentence
                firstbracket += ' ]'
                bracketedsentenceList.append(firstbracket)
        return bracketedsentenceList

    def makeTests(self, Book1, Book2, Book3, questionEntryNum, testEntryNum, grade1Check, grade2Check, grade3Check):
        '''make the desired number of tests with the desired number of questions.'''
        tempWordList = []
        #print("Questions requested: " + str(questionEntryNum.get()))
        CHECKBOXCOUNTER = 1
        for _ in range(questionEntryNum.get()):
                try:
                        if grade1Check.get() == 1:
                                #print("grade1Check was entered " + str(CHECKBOXCOUNTER) + " times.")
                                with open(Book1, 'r') as Book1File_object:
                                        Book1VocabWordLine = Book1File_object.readlines()
                                        for word in Book1VocabWordLine:
                                                if str(word[:4]) == 'PAGE':
                                                        pass
                                                elif str(word[:4]) == '\n':
                                                        pass
                                                else:
                                                        tempWordList.append(word[:-1])
                        if grade2Check.get() == 1:
                                #print("grade2Check was entered " + str(CHECKBOXCOUNTER) + " times.")
                                with open(Book2, 'r') as Book2File_object:
                                        Book2VocabWordLine = Book2File_object.readlines()
                                        for word in Book2VocabWordLine:
                                                #print(word)
                                                if str(word[:4]) == 'PAGE':
                                                        pass
                                                elif str(word[:4]) == '\n':
                                                        pass
                                                else:
                                                        tempWordList.append(word[:-1])
                        if grade3Check.get() == 1:
                                #print("grade3Check was entered " + str(CHECKBOXCOUNTER) + " times.")
                                with open(Book3, 'r') as Book3File_object:
                                        Book3VocabWordLine = Book3File_object.readlines()
                                        for word in Book3VocabWordLine:
                                                #print(word)
                                                if str(word[:4]) == 'PAGE':
                                                        pass
                                                elif str(word[:4]) == '\n':
                                                        pass
                                                else:
                                                        tempWordList.append(word[:-1])
                        else:
                                mBox.showinfo("You forgot something.", "You need to select a grade level.")
                                #message box
                                
                        CHECKBOXCOUNTER += 1
                except IndexError:
                        print("There was an index error")
                        
        #print("The current tempWordList is: " + str(tempWordList))
        TESTNAMECOUNTER = 1	
        for x in range(testEntryNum.get()):
                #pull name from the student name file
                #load that name into the variable "studentName"
                
                studentName = 'bob' ###placeholder value
                testFileName = "/home/pi/Desktop/SchoolProgramming/Test_Files/" + studentName + "Test_" + str(TESTNAMECOUNTER) + ".txt"
                with open(testFileName , 'w+') as newTest:
                        localList = [] #local list to make sure no duplicate words in the file
                        for y in range(questionEntryNum.get()):
                                testWord = random.choice(tempWordList)
                                if testWord in localList:
                                        pass
                                else:
                                        newTest.write(testWord + "\n"*2)
                                        localList.append(testWord)
                TESTNAMECOUNTER += 1

    def saveTests(save_location, file_name, stuff):
        try:
            with open(save_location + file_name, "w+") as my_file:
                for line in stuff:
                    my_file.write(line)
            print("Making_Tests_class, saveTests(); Test creation successful")
        except IOError:
            print("Making_Tests_class, saveTests(); error with trying to write to a file")



