#!/usr/bin/env python3.7
# directorysetup.py
"""Directory setup module."""

# stand lib
from pathlib import Path
import sys
from typing import List
from typing import Text


def make_directories(dirs: List[Text]) -> None:
    """Creates subdirectories in root dir. Returns None."""
    for d in dirs:
        if Path(d).exists():
            pass
        else:
            Path(d).mkdir()
    return None
