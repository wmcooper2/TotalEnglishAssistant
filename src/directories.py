#!/usr/bin/env python3
"""This module checks and sets up the directories."""
# stand lib
import sys
from pathlib import Path

# custom
from constants import *


def make_dirs() -> None:
    """Creates subdirectories in root dir. Returns None."""
    for d in DIRECTORIES:
        if not Path(ROOT_DIR, d).exists():
            Path(ROOT_DIR, d).mkdir()
    return None


def dict_exists() -> bool:
    """Checks for dict in '<rootdir>/Dictionaries/'. Returns Boolean."""
    if not Path(USER_DICT).exists():
        return False
    else:
        return True
