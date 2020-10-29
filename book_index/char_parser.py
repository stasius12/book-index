from collections import defaultdict
from typing import DefaultDict


SEPARATOR_LIST = [" ", ".", "\n", "\0", ""]


class CharParser:
    def __init__(self):
        self.result: DefaultDict = defaultdict(list)
        self._next_word_index = 0

    def parse_lines(self, all_lines: list):
        for row_number, line in enumerate(all_lines, 1):
            self._parse_line(line, row_number)

    def _parse_line(self, line: str, row_number: int):
        self._next_word_index = 0
        for col_number, char_ in enumerate(line):
            if char_ in SEPARATOR_LIST:
                self._handle_separator(line, col_number, row_number)
            if col_number == len(line) - 1:
                self._handle_end_of_line(line, col_number, row_number)

    def _handle_separator(self, line: str, col_number: int, row_number: int):
        word = line[self._next_word_index : col_number]
        self._save_word_to_result(word, row_number, self._next_word_index)
        self._next_word_index = col_number + 1

    def _handle_end_of_line(self, line: str, col_number: int, row_number: int):
        word = line[self._next_word_index : col_number + 1]
        self._save_word_to_result(word, row_number, self._next_word_index)

    def _save_word_to_result(self, word, row_number, col_number):
        self.result[word].append((row_number, col_number + 1))
