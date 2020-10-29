from io import StringIO

import pytest

from book_index.index import (
    find_all_words_in_text_with_char_parser,
)


@pytest.mark.parametrize(
    "txt,result",
    [
        (["ala ma kota"], {"ala": [(1, 1)], "ma": [(1, 5)], "kota": [(1, 8)]}),
        (
            ["ala ma kota", "pies ma psa"],
            {
                "ala": [(1, 1)],
                "ma": [(1, 5), (2, 6)],
                "kota": [(1, 8)],
                "pies": [(2, 1)],
                "psa": [(2, 9)],
            },
        ),
    ],
)
def test_find_all_words_in_text_with_char_parser(txt: list, result: dict):
    assert find_all_words_in_text_with_char_parser(txt) == result
