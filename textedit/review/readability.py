#!/usr/bin/env python

"""Computes the Colman-Liau index for any given file. 
Returns the grade level reading ability of the file. 

More on The Colman-Liau Index 
https://readable.io/content/the-coleman-liau-index:

Formula: 

L = average number of letters per 100 words and;
S = average number of sentences per 100 words.
0.0588L – 0.296S – 15.8

"""
from review.wordcount import WC
import sys

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
	print(colman_liau(sys.argv[1]))





