from plrs import Lexer, is_part_numeric
from dataclasses import dataclass
from typing import List
import argparse
import json


@dataclass
class Word:
    word: str
    defs: List[str]

    def __dict__(self):
        return {"word": self.word, "defs": self.defs}


def parse(filename: str):
    words = []

    with open(filename, "r", encoding='utf-8-sig') as file:
        lines = file.readlines()

        current_word = None

        for line in lines:
            # Check for close to empty lines
            if len(line.replace(" ", "")) < 2:
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
                if current_word is not None:
                    # Add a definition to defs
                    current_word.defs.append(" ".join(parts[1:]))

        # Add the last word because it's not caught
        words.append(current_word)


    return words



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", help="Input filename", required=True)
    parser.add_argument("-o", "--outfile", help="Output filename")
    parser.add_argument("-v", "--verbose", help="Verbose", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    words = parse(args.infile)

    # Print all the words
    if args.verbose:
        for word in words:
            print(word.__dict__())

    # Write the output to json file
    if args.outfile:
        with open(args.outfile, "w") as file:
            json.dump([x.__dict__() for x in words], file)
        print(f"Wrote json to {args.outfile}!")
