# ✏️ Text Edit in Wonderland ✏️


<img src="alice_pig.jpg" alt="Alice with Pig" style="width: 200px;"/>

The mini text editor for people who want to focus on learning Python packaging. This text editor lets you:

+ Count the number of words, sentences, and characters in a file
+ Determine the [Colman-Liau readabilty index](https://readable.io/content/the-coleman-liau-index/)
+ Replace a phrase or string with another phrase
+ Change spacing between sentences from single space period to double space/period and backwards

and not much else.


## Installing

These directions are for OSX/Linux-based systems. Windows will be slightly different.

1. You'll need at least Python 3.5 to run Text Edit.
2. `git clone https://gitlab.com/veekaybee/textedit.git`
3. `cd textedit`
4. Run `pip install .`
5. That's it! You're ready to use textedit.
6. If you encounter any issues, `export PYTHONPATH="${PYTHONPATH}:/texteditpath"` to your `~/.bashrc` or Windows equivalent.
7. Running tests: `python -m unittest discover` to test basic wordcount functionality.

### Prerequisites

```
Python 3.5
```

### Using the Package API

To import into your Python code:

`import textedit`

You can run the code interactively:
```
#Replace

python replace.py ../texts/alice.txt "Vicki" "Dora the Explorer"
Old Wordcount ('Words:', 274)
WC __name__: WC
New Wordcount ('Words:', 281)
parsefile __name__: __main__

#WordCount

mbp-vboykis:review vboykis$ python wordcount.py "../texts/alice.txt"
('Words:', 274)
('Sentences:', 7)
('Letters:', 1120)

# Readability

mbp-vboykis:review vboykis$ python readability.py "../texts/alice.txt"
('Reading Grade Level of Text:', 7)
```

Or, you can import it and use on a text file:

```
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

```

## Deployment

None! This is not a production-ready package. Install on your local machine and test it out and break things.

## Built With
Love and Alice in Wonderland.

## Authors

* **Vicki Boykis**  - [On GitHub](https://github.com/veekaybee)


## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means. No guarantees, batteries sold separately.
