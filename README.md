# Total English Assistant
## Introduction

This is a GUI tool intended to be a supplement to the "Total English" book series currently (in 2018) taught in Japan's middle schools.

Official website for the books is unknown, but here is an [example from Rakuten][0].

## Description

The primary function of this tool is to make vocabulary tests.

Secondary functions include;
* looking up words in the books' indices (dictionary tab)
* inputting sentences to check that all words exist in the book (sentence tab), and
* saving a collection of images for use in a slideshow-like review (images tab) (unfinished)

#### Installation and Running

Install with:
```
git clone https://github.com/wmcooper2/TotalEnglishAssistant.git
```

Run from the program's root directory with:
```
./run
```


### Instructions 
#### Vocabulary Tab

The user can choose;
* a specific grade
* a page range (A -> B; includes both A and B in the search range)
* English, Japanese or both
* how many questions per test, and 
* how many tests to make (making more than one test automatically randomizes word order in subsequent tests)

#### Sentences Tab

* input is only accepted in English (for now).
* type any sentence that you want to use in your worksheets, and it will search for each word in the books. If it is not in the books at all, then it will display "###".
* when it searches, it does not remove apostrophes and hyphens (sometimes those are part of the word) 
* with this you can ensure that you only use the words found in the book so there is no mistake in making your own tests, and that the words are sure to be in the books
* Word replacements are chosen based on the current word's "part of speech" as determined by the original "Total English" book series indices

#### Dictionary Tab

* shows some quick stats about word counts at the top
* input only accepts English (for now)
* input a word to get that word's entry in the books' indices
* if you want to edit the word's entry, then click edit and you can change the word's entry-attributes (this edits a copy of the default dictionary)
* if you accidently make unwanted changes to the default dictionary, delete "TotalEnglishAssistant/Dictionaries/totalenglish123.json" and restart the program. It will always check that a copy exists in "TotalEnglishAssistant/Dictionaries/" 

#### Images Tab

* the images saved here will be loaded into the browser in simple games that can be used in the classroom (not yet implemented)
* choose a directory where you want to load images from, and the images will automatically start loading one-by-one
* input a category name, when the first picture loads, enter a picture name below the category name (dont change the category or else it will create a new one midway through ???) and click "Save and Load Another" to continue naming the images

# Developer Notes

### Changes to Directories

This tool will :
* create these directories in the programs's root directory "./TotalEnglishAssistant/";
  * "./TotalEnglishAssistant/Dictionaries/"
  * "./TotalEnglishAssistant/Images/"
  * "./TotalEnglishAssistant/VocabularyTests/"
* write files to the newly created directories.

### TESTING

* run "./Test" from the program's root directory.

### Known Bugs

* vocabulary tab makes a test with no suffix or suffix "0" that has no contents
* "Tests" script in the root dir cannot find the test files.
* Load and Edit dicitionary buttons in the dictionary tab are just placeholders for now
* Vocabulary tests are not written anywhere (supposed to go to root/VocabularyTests) since I moved things around.

#### Variable Naming

* studentgradelevel == the grade level according to the Japanese system 
  * "1" is 7th grade
  * "2" is 8th grade 
  * "3" is 9th grade

#### Contribute

Issue Tracker: github.com/wmcooper2/TotalEnglishAssitant/issues

If you are having issues, please let me know. Thank you.
Find me on GitHub: https://github.com/wmcooper2

### License

Licensed under the MIT license. 


[0]: https://item.rakuten.co.jp/learners/10000360/?scid=af_pc_etc&sc2id=af_113_0_10001868
