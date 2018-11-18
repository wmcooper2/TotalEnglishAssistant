#!/usr/bin/env python3
"""This module checks and sets up the directories."""

#stand lib
import sys
from pathlib import Path

ROOTDIR = "./"
VOCABDIR = "VocabularyTests"
#IMAGEDIR = "Images"
DICTDIR = "Dictionaries"
#directories = [VOCABDIR, IMAGEDIR, DICTDIR]
directories = [VOCABDIR, DICTDIR]
main_path = Path(ROOTDIR)

def make_dirs():
    """Creates subdirectories within the program's root directory.
        Returns None."""
    for directory in directories:
        if Path(ROOTDIR,directory).exists():
            pass
        else:
            Path(ROOTDIR,directory).mkdir()

