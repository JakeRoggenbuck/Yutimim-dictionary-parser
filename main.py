from plrs import Lexer, is_part_numeric

with open("./dict.txt") as file:
    lines = file.readlines()

    for line in lines:
        print(line)
