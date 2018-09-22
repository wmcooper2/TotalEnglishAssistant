#!/usr/bin/python3
from pathlib import Path
import sys

class DirectorySetup():

    main_dir = "./"
    test_dir = "VocabularyTests"
    image_dir = "Images"
    dict_dir = "Dictionaries"
    directories = [test_dir, image_dir, dict_dir]
    main_path = Path(main_dir) 

    def make_directories(self):
        """Creates subdirectories within the program's root directory.
            Returns None."""
        for directory in self.directories:
            if Path(self.main_dir,directory).exists():
                pass
            else:
                Path(self.main_dir,directory).mkdir()           

    def _check(self):
        """Checks to see the directories were installed properly, returns None."""
        for directory in self.directories:
            if Path(self.main_dir,directory) in self.main_path.iterdir():
                print("'{0}' directory already exists".format(directory))
            else:
                print("'{0}' directory could not be made".format(directory))

    def make_dirs(self):
        """Creates the needed directories for the program, returns None."""
        self.make_directories()

if __name__ == "__main__":
    new = DirectorySetup()
    new.make_dirs()
    dict_ = (new.main_path,new.dict_dir)
