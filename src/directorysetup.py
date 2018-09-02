#!/usr/bin/python3
from pathlib import Path
import sys

class DirectorySetup():
    main_dir = "../"
    test_dir = "VocabularyTests"
    image_dir = "Images"
    dict_dir = "Dictionaries"
    directories = [test_dir, image_dir, dict_dir]
#    home = Path.home()
    main_path = Path(main_dir) 

    def make_directories(self):
        """Creates subdirectories within the program's root directory.
            Returns None."""
        for directory in self.directories:
            if Path(self.main_dir,directory).exists():
                pass
            else:
                Path(self.main_dir,directory).mkdir()           
                print(Path(self.main_dir,directory))
            
    def ask_to_remove(self):
        """Gives the user the option to remove the existing files to remake,
            returns None."""
#        print("Ask to remove...")
        pass

    def _check(self):
        """Checks to see the directories were installed properly, returns None."""
        for directory in self.directories:
            if Path(self.main_dir,directory) in self.main_path.iterdir():
                print("'{0}' directory already exists".format(directory))
            else:
                print("'{0}' directory could not be made".format(directory))
            
    def category_dir(self, name):
        """Creates the sub-directory 'name', returns None."""
        category_dir = (self.main_path,self.image_dir,name)
        if not Path(category_dir).exists():
            Path(category_dir).mkdir()
        return category_dir

    def make_dirs(self):
        """Creates the needed directories for the program, returns None."""
        self.make_directories()
        #self._check()

if __name__ == "__main__":
    new = DirectorySetup()
    new.make_dirs()
    dict_ = (new.main_path,new.dict_dir)
