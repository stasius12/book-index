from io import TextIOBase


def do_it(stream: TextIOBase, format: str = "text"):
    txt = stream.readlines()
    print("THIS IS AN EXAMPLE!")
    print("your text has", len(txt), "lines")
    print("format is", format)
