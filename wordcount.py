
def word_count(filename):
	with open(filename, 'r') as file:
		file_contents = file.read()
		print('Total words:   ', len(file_contents.split()))

def sentence_count(filename):
	with open(filename, 'r') as file:
		file_contents = file.read()
		print('total sentences:    ', file_contents.count('.')+file_contents.count('!')+file_contents.count('?'))

def character_count(filename):
	with open(filename, 'r') as file:
		file_contents = file.read()

		letter_counter = 0

		total_words = len(file_contents.split())

		for i in range(total_words):
				letter_counter+= 1

		print('total characters   ', letter_counter)

if __name__ == '__main__':
	word_count('../texts/alice.txt')
	sentence_count('../texts/alice.txt')
	character_count('../texts/alice.txt')

