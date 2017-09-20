#!/usr/bin/env python

"""Changes spacing from single to double space for a given file.
Outputs the new file as filename_double_spaced.txt or
filename_single_spaced.txt as needed. 
"""



def single_to_double(filename):
	"""Converts from single to double space after a period"""
	try: 
		with open(filename, 'r') as input:
			with open('%s_double_spaced.txt',  'w') % filename as output:
				file_contents = input.read()
				output.write(file_contents.replace(r'\.\s{1}', r'\.\s{2}'))
	except AssertionError:
		print("Single space not found")

def double_to_single(filename):
	"""Converts from double to single space after a period"""
	try: 
		with open(filename, 'r') as input:
			with open('%s_single_spaced.txt', 'w') % filename as output:
				file_contents = input.read()
				output.write(file_contents.replace(r'\.\s{2}', r'\.\s{1}'))
	except AssertionError:
		print("Double space not found")

if __name__ == '__main__':
	single_to_double("texts/alice.txt")