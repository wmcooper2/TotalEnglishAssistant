#!/usr/bin/env python3
"""This module checks and sets up the directories."""

#stand lib
import sys
from pathlib import Path

#custom
from constants import *

def make_dirs():
    """Creates subdirectories within the program's root directory.
        Returns None."""
    for directory in DIRECTORIES:
        if Path(ROOTDIR,directory).exists():
            pass
        else:
            Path(ROOTDIR,directory).mkdir()

def dict_exists():
    """Checks if dictionary exists in 
        '~/TotalEnglishAssistant/Dictionaries/'.
    Returns Boolean. """
    if not os.path.exists(USERDICT):
        return False
    else:
        return True
