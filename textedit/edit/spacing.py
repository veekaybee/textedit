
def single_to_double(filename):
	try: 
		with open(filename, 'r') as input:
			with open('%s_double_spaced.txt',  'w') % filename as output:
				file_contents = input.read()
				output.write(file_contents.replace(r'\.\s{1}', r'\.\s{2}'))
	except AssertionError:
		print("Single space not found")

def double_to_single(filename):
	try: 
		with open(filename, 'r') as input:
			with open('%s_single_spaced.txt', 'w') % filename as output:
				file_contents = input.read()
				output.write(file_contents.replace(r'\.\s{2}', r'\.\s{1}'))
	except AssertionError:
		print("Double space not found")

if __name__ == '__main__':
	single_to_double("texts/alice.txt")