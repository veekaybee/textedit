#!/usr/bin/env python

"""Replaces an instance of one word with another in a copy of 
the original file called new_filename. 

Sysargs:  filename, word1, word2
"""


import sys
import os

# importing relative directories
from review.wordcount import WC

class Replace(object):
	"""Replaces one phrase with another"""
	
	def __init__(self, filename, initial_word, replacement_word):
		self.filename = filename
		self.initial_word = initial_word
		self.replacement_word = replacement_word

	def replace_words(self, filename, initial_word, replacement_word):
		with open(filename, 'r') as input:
			with open('../texts/new_%s.txt' % self.filename , 'w') as output:
				for line in input:
					line = line.rstrip()
					newline = line.replace(initial_word, replacement_word)
					output.write(newline)

if __name__ == '__main__':
	# Read command line inputs
	filename = sys.argv[1]
	old_word = sys.argv[2]
	new_word = sys.argv[3]

	Replace(filename, old_word, new_word)

	# Check wordcount 
	alice = WC(sys.argv[1])
	new_alice = WC('../texts/new_alice.txt')

	# Output stats - optional
	print("Old Wordcount",alice.word_count())
	print("WC __name__:", WC.__name__)
	print("New Wordcount",new_alice.word_count())
	print("replacefile __name__:", __name__)