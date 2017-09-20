'''
Colman-Liau Index

The Colman-Liau Index 
https://readable.io/content/the-coleman-liau-index/

L = average number of letters per 100 words and;

S = average number of sentences per 100 words.

The formula is as follows:

0.0588L – 0.296S – 15.8


'''

import wordcount

WORD_INCREMENT = 100

def get_letters(filename):

	L = wordcount.character_count(filename) /  wordcount.word_count(filename) * 100 
	return L

def get_sentences(filename):

	S = wordcount.sentence_count(filename)/ wordcount.word_count(filename) * 100 
	return S


def colman_liau(filename):
	index = 0.0588 * get_letters(filename) - 0.296 * get_sentences(filename) - 15.8
	return("Reading Grade Level of Text:", round(index))


if __name__ == '__main__':
	print(colman_liau('../texts/alice.txt'))





