# Book Index Kata

[[TOC]]

## Goal

Your goal is create an index of words in proposed format:

```
Word             Row,Col
AnotherWord      Row,Col; Row,Col
```

## Example

In example, if you have a text:

```
Foo bar
bar test
```

Then your program should return:

```
Foo     1,1
Bar     1,5; 2,1
Test    2,5
```

## What we have

### CLI

We have a very easy CLI for you:

```
python3 -m book_index FILE
```

or:

```
python3 -m book_index FILE --format html
```

this CLI executes `do_it(stream, format)` function from `book_index/index.py`

### Tests

we have a pytest environment:

```
pytest tests
```

### Install

TODO

## Proposed steps to achieve the goal

1. Make a list of words from text
2. Make a list of tuples, which each tuple has (word, row, col)
3. Use these tuples to aggregate words with list of positions
4. Think about non-words characters, and [conjunction](https://en.wikipedia.org/wiki/Conjunction_%28grammar%29) words
5. Think about another formats like html, CSV oraz latex (default is a text format)

## Protips

TODO
