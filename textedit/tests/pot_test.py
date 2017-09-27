"""Tests textedit functionality of the textedit module on the pool_of_tears.txt file"""


from review import readability  #import everything in the file named readability
from review.wordcount import WC #import classes specifically
from edit.spacing import Spacing
from edit.replace import Replace


test_file = '../texts/pool_of_tears.txt'

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





