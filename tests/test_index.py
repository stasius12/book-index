from io import StringIO

import pytest

from book_index.index import do_it, find_all_words_in_text, parse_line


def test_do_it():
    stream = StringIO("Foo Foo Foo")
    do_it(stream)

    x = 1 + 1
    assert x == 2


@pytest.mark.parametrize(
    "txt,result", [(["ala ma kota"], {"ala": [(1, 1)], "ma": [(1, 5)], "kota": [(1, 8)]})]
)
def test_find_all_words_in_text(txt: list, result: dict):
    assert find_all_words_in_text(txt) == result


@pytest.mark.parametrize(
    "line,result", [(["ala ma kota"], {"ala": [(1, 1)], "ma": [(1, 4)], "kota": [(1, 8)]})]
)
def test_parse_line(line: str, result: dict):
    assert parse_line(line) == result
