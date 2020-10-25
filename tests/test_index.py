from io import StringIO

from book_index.index import do_it


def test_do_it():
    stream = StringIO("Foo Foo Foo")
    assert do_it(stream) == "Foo    1,1; 1,5; 1,9"
