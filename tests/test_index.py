from io import StringIO

from book_index.index import do_it


def test_do_it():
    stream = StringIO("Foo Foo Foo")
    do_it(stream)

    x = 1 + 1
    assert x == 2
