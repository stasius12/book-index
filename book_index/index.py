from collections import defaultdict
from io import TextIOBase
from typing import DefaultDict


SEPERATOR_LIST = [" ", ".", "\n", "\0", ""]


def do_it(stream: TextIOBase, format_: str = "text"):
    txt = stream.readlines()
    print("THIS IS AN EXAMPLE!")
    print("your text has", len(txt), "lines")
    print("format is", format_)
    return find_all_words_in_text(txt)


def find_all_words_in_text(all_lines: list) -> DefaultDict:
    """
        result: {
            "ala": [(1,1), (2, 2)],
            ...
        }
    """
    result = defaultdict(list)
    start_idx = 1

    for row_number, line in enumerate(all_lines, 1):
        for col_number, char_ in enumerate(line, 1):
            if char_ in SEPERATOR_LIST:
                word = line[start_idx - 1 : col_number - 1]
                result[word].append((row_number, start_idx))
                start_idx = col_number + 1
        # result[word].append((row_number, start_idx))

    return result


def parse_line(line: str) -> dict:
    for col_number, char_ in enumerate(line):
        if char_ in SEPERATOR_LIST:
            pass
