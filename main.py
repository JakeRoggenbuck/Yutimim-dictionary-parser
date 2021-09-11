from plrs import Lexer, is_part_numeric
from dataclasses import dataclass
from typing import List


@dataclass
class Word:
    word: str
    defs: List[str]

    def __dict__(self):
        return {"word": self.word, "defs": self.defs}


with open("./dict.txt") as file:
    lines = file.readlines()

    words = []
    current_word = None

    for line in lines:
        # Check for close to empty lines
        if len(line) < 2:
            continue

        parts = line.split()

        # Check if the first part is not enumerated, like ['1.', 'that']
        # parts[0] is '1.' and is_part_numeric('1.') is True
        if not is_part_numeric(parts[0]):
            # Add the last word to the words list
            if current_word is not None:
                words.append(current_word)
            # Make a new word with empty defs
            current_word = Word(parts[0], [])
        else:
            # Add a definition to defs
            current_word.defs.append(" ".join(parts[1:]))

    # Add the last word because it's not caught
    words.append(current_word)

    for word in words:
        # print(dict(word))
        print(word.__dict__())
