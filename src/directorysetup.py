#!/usr/bin/python3
from pathlib import Path
import sys

class DirectorySetup():
    main_dir    = "./"
    test_dir    = "VocabularyTests"
    image_dir   = "Images"
    dict_dir    = "Dictionaries"
    directories = [test_dir, image_dir, dict_dir]
    main_path   = Path(main_dir) 

    def make_directories(self):
        """Creates subdirectories in root dir. Returns None."""
        for d in self.directories:
            if Path(self.main_dir, d).exists(): pass
            else: Path(self.main_dir, d).mkdir()           

    def _check(self):
        """Checks to see the directories were created. Returns None."""
        for d in self.directories:
            if Path(self.main_dir, d) in self.main_path.iterdir():
                print("'{0}' directory already exists".format(d))
            else:
                print("'{0}' directory could not be made".format(d))

    def make_dirs(self):
        """Creates directories for the program. Returns None."""
        self.make_directories()

if __name__ == "__main__":
    new = DirectorySetup()
    new.make_dirs()
    dict_ = (new.main_path,new.dict_dir)
