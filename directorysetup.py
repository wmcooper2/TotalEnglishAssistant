#!/usr/bin/python3
from pathlib import Path
import sys

class DirectorySetup():
    main_dir = "TotalEnglishAssistant"
    tests = "VocabularyTests"
    images = "Images"
    dictionaries = "Dictionaries"
    directories = [tests, images, dictionaries]
    home = Path.home()
    main_path = Path(home/main_dir) 

    def dir_count(self):
        """Counts the contents of the user's home directory, returns None."""
        print(sum(1 for x in self.home.iterdir()))
     
    def main_directory(self):
        """Creates the main directory in the user's home directory,
            returns None."""
        if self.main_path.exists():
            pass
        else:
            self.main_path.mkdir()

    def sub_directories(self):
        """Creates subdirectories within the main directory,
            returns None."""
        for directory in self.directories:
            if Path(self.home/self.main_dir/directory).exists():
                pass
            else:
                Path(self.home/self.main_dir/directory).mkdir()           
            
    def ask_to_remove(self):
        """Gives the user the option to remove the existing files to remake,
            returns None."""
        print("Ask to remove...")

    def check(self):
        """Checks to see the directories were installed properly, returns None."""
        def check_sub():
            for directory in self.directories:
                if Path(self.home/self.main_dir/directory) in self.main_path.iterdir():
                    print("'{0}' directory already exists".format(directory))
                else:
                    print("'{0}' directory could not be made".format(directory))
        if self.main_path  in self.home.iterdir():
            print("'{0}' directory already exists".format(self.main_dir))
            check_sub()
        else:
            print("'{0}' directory could not be made".format(self.main_dir))
            
    def category_dir(self, name):
        """Creates the sub-directory 'name', returns None."""
        category_dir = (self.main_path/self.images/name)
        if not Path(category_dir).exists():
            Path(category_dir).mkdir()
        return category_dir

    def make_dirs(self):
        """Creates the needed directories for the program, returns None."""
        self.main_directory()
        self.sub_directories()
        #self.check()

if __name__ == "__main__":
    new = DirectorySetup()
    new.make_dirs()
    dict_ = (new.main_path/new.dictionaries)
    dict_ = "/" + "/".join(dict_.parts[1:]) + "/"
    print(dict_)    
