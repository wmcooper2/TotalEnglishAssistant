#!/usr/bin/env python3
"""This module checks and sets up the directories."""

#stand lib
import sys
from pathlib import Path

#custom
from constants import *

def make_dirs():
    """Creates subdirectories in root dir. Returns None."""
    for d in DIRECTORIES:
        if Path(ROOT_DIR, d).exists(): pass
        else: Path(ROOT_DIR, d).mkdir()

def dict_exists():
    """Checks for dict in '<rootdir>/Dictionaries/'. Returns Boolean."""
    if not os.path.exists(USER_DICT): return False
    else: return True
