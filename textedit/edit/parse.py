import sys
import os

sys.path.append(os.path.abspath("/Users/vboykis/Desktop/python_packaging/textedit/textedit/review"))

from wordcount import WC


def parse_file(words):
	with open(words, 'r') as input:
		with open('../texts/new_alice.txt', 'w')as output:
			for line in input:
				line = line.rstrip()
				newline = line.replace("Alice", "Dora the Explorer")
				output.write(newline)

if __name__ == '__main__':
	parse_file('../texts/alice.txt')
	alice = WC('../texts/alice.txt')
	new_alice = WC('../texts/new_alice.txt')
	print("Old Wordcount",alice.word_count())
	print("WC __name__:", WC.__name__)
	print("New Wordcount",new_alice.word_count())
	print("parsefile __name__:", __name__)