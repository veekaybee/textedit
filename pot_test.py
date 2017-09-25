"""Tests textedit functionality of the textedit module on the pool_of_tears.txt file"""


from textedit.review import readability  #import everything in the file
from textedit.review.wordcount import WC #import classes specifically
from textedit.edit.spacing import Spacing
from textedit.edit.replace import Replace


test_file = '/Users/vboykis/Desktop/python_packaging/textedit/textedit/texts/pool_of_tears.txt'

# Count words

print("Wordcount.py")
alice = WC(test_file)
WC.counts(alice)
print("\n")

# Readability Index
print("readability.py")
print(readability.colman_liau(test_file))
print("\n")

# Change Spacing
print("spacing.py")
sp = Spacing(test_file)
Spacing.spacing_check(sp)
print("Spaces replaced")
print("\n")

# Replace Words
print("replace.py")
Replace(test_file, "Alice", "Dora the Explorer")
print("Words replaced")
print("\n")





