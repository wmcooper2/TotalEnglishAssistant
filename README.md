## Total English Assistant

This is a GUI tool intended to be a supplement to the "Total English" book series currently (in 2018) taught in Japan's middle schools.
This tool will :
* create these directories in the programs's root directory "./TotalEnglishAssistant/"
  * "./TotalEnglishAssistant/Dictionaries/"
  * "./TotalEnglishAssistant/Images/"
  * "./TotalEnglishAssistant/VocabularyTests/"
* write files to the newly created directories.

### Features 

#### Vocabulary Tab
* make randonmized vocabulary tests
* select questions per test
* select amount of tests to make
* select a grade level
* select a language to write the tests in
* select a page range to get the words from
* select a save location and base file name (counter is suffixed to the name)

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



### TESTING
* module; saves a ".py" to the users desktop


### Bugs
* vocabulary tab makes a test with no suffix or suffix "0" that has no contents
* fix the intermittent bug in change_word in Word class in Words.py (run Test_Words.py several times to find the issue) 


### Naming Conventions (in the source code)
for methods ("..." means the name continues):
* set...	setting attributes within classes.
* get...	getting information from var-containers, entry widgets.
* erase...	removing widgets from the GUI.
* delete...	removing data from entry boxes.
* insert...	putting data (usually text or images) into widgets.
* show...	showing data or images in the widgets.
* draw...	drawing widgets to the GUI.
* save...	saving and writing to the disk_
* edit_		editing data in a file (.txt .json  etc).
* quit_		quitting the current window or program.
* make...	makes objects/lists/etc for use within classes.
* check...	outsourcing as much of the validation to the files that handle validation



#### Variable Naming
* student_grade_level == the grade level according to the Japanese system ("1" is 7th grade, "2" is 8th grade and "3" is 9th grade)




















English Program Website
----------------------

Written in HTML, CSS, and Javascript, there is no direct connection with python now. I am using this part of the whole project to teach myself about the internet and front-end design. The goal is to later use my knowledge of making interactive websites to make really nice templates in Django and then use Django as my foundation. I can use my knowledge of the front-end to work with Django templates and shift more of my focus back to Python.




Features
-------








Bugs
----




TODO
----
 - set up the functions for the images loaded into the browser such that they have the corresponding dictionary entry if there is one. That way they can pull different properties from the image such as Japanese if the user wants to load Japanese as the answer or vice-versa with English.
 - set up a webhost to put these files onto so the games and resources can be used through the browser in schools (to get around the security issue of using USB's and one's own computer in different schools)
 - convert some functionality of the Total English Assistant (Python GUI) to be used through the browser.










Installation
------------

Install $project by cloning:

- https://github.com/wmcooper2/Clean-Code-English-Tests.git

Contribute
----------

- Issue Tracker: github.com/wmcooper2/Clean-Code-English-Tests/issues


Support
-------

If you are having issues, please let me know.
Find me on GitHub: https://github.com/wmcooper2

License
-------

Licensed under the MIT license. 
