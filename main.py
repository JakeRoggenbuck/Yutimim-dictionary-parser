from plrs import Lexer, is_part_numeric
from dataclasses import dataclass
from typing import List


@dataclass
class Word:
    word: str
    defs: List[str]


with open("./dict.txt") as file:
    lines = file.readlines()

    words = []
    current_word = None

    for line in lines:
        if len(line) < 2:
            continue

        parts = line.split()

        if not is_part_numeric(parts[0]):
            words.append(current_word)
            current_word = Word(parts[0], [])
        else:
            current_word.defs.append(" ".join(parts[1:]))

    words.append(current_word)

    for word in words:
        print(word)
