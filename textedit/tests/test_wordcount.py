#!/usr/bin/env python

import unittest
import sys
import os

from review.wordcount import WC  # import wordcount from its relative path

WC_test = WC('../texts/alice.txt')


class Test(unittest.TestCase):
    wc = ('Words:', 274)
    sc = ('Sentences:', 7)
    cc = ('Letters:', 1120)

    def test_wc(self):
        self.assertCountEqual(WC_test.word_count(), self.wc)

    def test_sentences(self):
        self.assertEqual(WC_test.sentence_count(), self.sc)

    def test_characters(self):
        self.assertEqual(WC_test.character_count(), self.cc)


if __name__ == '__main__':
    unittest.main()
