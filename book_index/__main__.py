# BRO DON'T EDIT THIS FILE
import argparse
from book_index.index import do_it

parser = argparse.ArgumentParser(description='create a index of words')
parser.add_argument('FILE')
parser.add_argument('--format', default='text')

args = parser.parse_args()
with open(args.FILE) as stream:
    do_it(stream, args.format)
