from collections import defaultdict
from io import TextIOBase
from typing import DefaultDict

from book_index.char_parser import CharParser

SEPERATOR_LIST = [" ", ".", ",", "\n", "\0", ""]


def do_it(stream: TextIOBase, format_: str = "text"):
    txt = stream.readlines()
    print("your text has", len(txt), "lines")
    print("format is", format_)
    result = find_all_words_in_text_with_char_parser(txt)
    print(result)
    return result


def find_all_words_in_text_with_char_parser(all_lines: list) -> DefaultDict:
    char_parser = CharParser()
    char_parser.parse_lines(all_lines)
    return char_parser.result


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
            if col_number == len(line):
                word = line[start_idx - 1 : col_number]
                result[word].append((row_number, start_idx))
                start_idx = col_number + 1

    return result
