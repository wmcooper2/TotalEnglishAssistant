# Total English Assistant
## Introduction
This is a GUI tool intended to be a supplement to the "Total English" book series currently (in 2018) taught in Japan's middle schools.
This tool will :
* create these directories in the programs's root directory "./TotalEnglishAssistant/"
  * "./TotalEnglishAssistant/Dictionaries/"
  * "./TotalEnglishAssistant/Images/"
  * "./TotalEnglishAssistant/VocabularyTests/"
* write files to the newly created directories.

Official website for the books is unknown, but here is a visual ([Rakuten][0]).

## Description
The primary function of this tool is to make vocabulary tests.

Secondary functions include;
* looking up words in the books' indices (dictionary tab)
* inputting sentences to check that all words exist in the book (sentence tab), and
[comment]: <> * saving a collection of images for use in a slideshow-like review (images tab) (unfinished)



### Features 
#### Vocabulary Tab
The user can choose;
* a specific grade
* a page range
* English, Japanese or both
* how many questions per test, and 
* how many tests to make


#### Sentences Tab
* input is only accepted in English.
* type any sentence that you want to use in your worksheets, and it will search for each word in the books. If it is not in the books at all, then it will display "###".
* When it searches, it does not remove apostrophes and hyphens. 
* with this you can ensure that you only use the words found in the book so there is no mistake in making your own tests, and that the words are sure to be in the books.
* Word replacements are chosen based on the current word's "part of speech" as determined by the original "Total English" book series indices.


#### Dictionary Tab
* shows some quick stats about word counts. 
* input a word to get that word's dictionary entry
* if you want to edit the word's entry, then click edit and you can change the word's entry-attributes


#### Images Tab
* this tab is meant to be a simple interface to add custom images and image-names to the file that the English Program Website will use. These images will be loaded into the browser in simple games that can be used in the classroom. 
* select a directory where you want to load images from, and the images will automatically start loading one-by-one.
* input a name in the entry field and click "Save and Load Another" to continue naming the images.
* the images will be saved in a default location (for now I have it set to my own preferences... see TODO)


# Developer Notes
### TESTING
* run "./Test" from the program's root directory.

### Known Bugs
* vocabulary tab makes a test with no suffix or suffix "0" that has no contents
* "Tests" script in the root dir cannot find the test files.

### Naming Conventions (in the source code)
for methods ("..." means the name continues):
* set   	setting attributes within classes.
* get   	getting information from var-containers, entry widgets.
* erase 	removing widgets from the GUI.
* delete	removing data from entry boxes.
* insert	putting data (usually text or images) into widgets.
* show  	showing data or images in the widgets.
* draw  	drawing widgets to the GUI.
* save  	saving and writing to the disk
* edit		editing data in a file (.txt .json  etc).
* quit		quitting the current window or program.
* make  	makes objects/lists/etc for use within classes.
* check 	outsourcing as much of the validation to the files that handle validation



#### Variable Naming
* student_grade_level == the grade level according to the Japanese system ("1" is 7th grade, "2" is 8th grade and "3" is 9th grade)


#### Installation

Install project by cloning:
https://github.com/wmcooper2/TotalEnglishAssistant.git

#### Contribute
Issue Tracker: github.com/wmcooper2/TotalEnglishAssitant/issues


### Support
If you are having issues, please let me know. Thank you.
Find me on GitHub: https://github.com/wmcooper2

### License
Licensed under the MIT license. 


[0]: https://item.rakuten.co.jp/learners/10000360/?scid=af_pc_etc&sc2id=af_113_0_10001868
