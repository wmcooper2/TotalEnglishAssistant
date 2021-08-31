"""Break up jhswords.py into text files named after their pages"""
# custom
from typing import Text
import jhsdict as jhs

words = jhs.jhswords


def save_to(grade: Text, word: Text, num: Text) -> None:
    """Saves 'word' to the file with name 'num'. Returns None."""
    file_name = "pages/grade" + grade + "/" + num + ".txt"
    with open(file_name, "a+") as f:
        f.write(word+"\n")
    return None

for word, details in words.items():
    if details["grade"] not in ["1", "2", "3"]:
        print(word, "not in any grade")
    else:
        save_to(details["grade"], word, details["page"])
