import sys
import os

# importing relative directories
from review.wordcount import WC


def replace_words(words):
	with open(words, 'r') as input:
		with open('../texts/new_alice.txt', 'w')as output:
			for line in input:
				line = line.rstrip()
				newline = line.replace("Alice", "Dora the Explorer")
				output.write(newline)

if __name__ == '__main__':
	replace_words('../texts/alice.txt')
	alice = WC('../texts/alice.txt')
	new_alice = WC('../texts/new_alice.txt')
	print("Old Wordcount",alice.word_count())
	print("WC __name__:", WC.__name__)
	print("New Wordcount",new_alice.word_count())
	print("parsefile __name__:", __name__)