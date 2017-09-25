#!/usr/bin/env python

"""Takes a file as sys.arg[1] as input and returns a wordcount, 
character count, and sentence count.

Sysargs:  filename
"""

import re
import sys


class WC:
	"""Conducts character, word, and letter count of object"""

	def __init__(self, filename):

		self.filename = filename


	def open_file(self,filename):
		"""Opens a file object to be used across the class"""
		with open(filename,'r') as f:
			file_contents = f.read()
			return file_contents


	def word_count(self):
		"""Returns a file's word count"""

		wc_file = self.open_file(self.filename)
		self = len(wc_file.split())
		return("Words:",len(wc_file.split()))


	def sentence_count(self):
		"""Returns a file's word sentence count"""

		sc_file = self.open_file(self.filename)
		
		return("Sentences:", sc_file.count('.') + sc_file.count('!') + sc_file.count('?'))

	def letter_count(self):

		"""Returns a file's character count, excluding punctuation"""
		letter_counter = 0

		pattern = r'[\W]' # excluding all punctuation

		cc_file = self.open_file(self.filename)

		total_words = cc_file.split()

		for word in total_words: 
			for letter in word:
				if not re.search(pattern, letter):
					letter_counter += 1
		
		return("Letters:", letter_counter)

	def counts(self):
		print(self.word_count(),'\n',self.sentence_count(),'\n',self.letter_count())

if __name__ == '__main__':
	alice = WC(sys.argv[1])
	WC.counts(alice)



