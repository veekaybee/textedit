#!/usr/bin/env python

"""Replaces an instance of one word with another in a copy of 
the original file called new_filename. 

Argv:  filename, word1, word2

Command Line example: 
"""

import sys
import os

# importing relative directories
from review.wordcount import WC


class Replace(object):
    """Replaces one phrase with another"""

    def __init__(self, old_filename, initial_word, replacement_word):
        self.filename = old_filename
        self.initial_word = initial_word
        self.replacement_word = replacement_word

    def replace_words(self, filename, initial_word, replacement_word):
        with open(filename, 'r') as input:
            with open('../texts/new_%s' % self.filename, 'w') as output:
                for line in input:
                    line = line.rstrip()
                    newline = line.replace(initial_word, replacement_word)
                    output.write(newline)


if __name__ == '__main__':
    # Read command line inputs
    old_filename = sys.argv[1]
    base = os.path.basename(old_filename)

    old_word = sys.argv[2]
    new_word = sys.argv[3]

    Replace(old_filename, old_word, new_word)

    # Check wordcount
    old_file_count = WC(sys.argv[1])

    new_filename = '../texts/new_%s' % base
    new_file_count = WC(new_filename)

    # Output stats - optional
    print("Old Wordcount", old_file_count.word_count())
    print("WC __name__:", WC.__name__)
    print("New Wordcount", new_file_count.word_count())
    print("replacefile __name__:", __name__)
