# ✏️ Text Edit in Wonderland ✏️ 


<img src="img/alice_pig.jpg" alt="Alice with Pig" style="width: 200px;"/>

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
3. Run `python setup.py install`
4. Run `pip -r requirements.txt`
5. That's it! You're ready to use textedit. 
6. If you encounter any issues, `export PYTHONPATH="${PYTHONPATH}:/my/other/path"` to your `~/.bashrc` or Windows equivalent file. 

### Prerequisites

```
Python 3.5
```

### Using the Package API

To import into your Python code: 

`import textedit`

Create a program that imports the package. 

#### WordCount

`python wordcount.py ../texts/alice.txt`

Or you can try a file in your current working directory


#### Replace

`python replace.py ../texts/alice.txt "Vicki" "Dora"`

#### Spacing

`python replace.py ../texts/alice.txt "Vicki" "Dora"`

#### Readability

`python replace.py ../texts/alice.txt "Vicki" "Dora"`


### Putting an entire file through the paces




## Deployment

None! This is not a production-ready package. 

## Built With
Love and Alice in Wonderland. 


## Authors

* **Vicki Boykis**  - [On GitHub](https://github.com/veekaybee)


## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.


