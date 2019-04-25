#!/usr/bin/env python3.7
"""Module for doing stuff."""

# stand lib

# 3rd party
from tabulate import tabulate

# custom
from sentutil import get_results_cli

header = {"given":"Word", "grade":"Grade", "page":"Page", "verb":"Verb", "noun":"Noun"}

while True:
    try:
        original = input("Input a sentence: ")
        print("\n", tabulate(get_results_cli(original), headers=header,
              tablefmt="fancy_grid"))
    except KeyboardInterrupt:
        print("Stopped manually.")
        break
