"""Tests textedit functionality on the pool_of_tears.txt file"""


from textedit.review import readability 
from textedit.review import wordcount 
from textedit.edit import spacing
from textedit.edit import replace


test_file = '/Users/vboykis/Desktop/python_packaging/textedit/textedit/texts/pool_of_tears.txt'

# Count words
alice = wordcount.WC(test_file)

print(wordcount.WC.word_count(alice))
print(wordcount.WC.character_count(alice))
print(wordcount.WC.sentence_count(alice))

# Readability Index

print(readability.colman_liau(test_file))

# Change Spacing

sp = spacing.Spacing(test_file)
spacing.Spacing.spacing_check(sp)
print('Spaces replaced')

# Replace Words

replace.Replace(test_file, "Alice", "Dora the Explorer")
print('Words replaces')





