#!/usr/bin/python3


import unittest
from d import Vocabulary


class TestVocabulary(unittest.TestCase):

    def test_empty(self):
        """Assert that a newly constructed vocabulary has size zero"""
        v = Vocabulary()
        self.assertEqual(v.size(), 0)

    def test_empty_list(self):
        """Assert that a newly constructed vocabulary contains an empty list"""
        v = Vocabulary()
        self.assertEqual(v.words(), list())

    def test_empty_word_index(self):
        """Assert that a newly constructed vocabulary does not associate any string with index zero"""
        v = Vocabulary()
        self.assertEqual(v.get_word(0), None)

    def test_negative_indices(self):
        """Assert that a newly constructed vocabulary returns None for negative numbers"""
        v = Vocabulary()
        for i in range(-1000,-1):
            self.assertEqual(v.get_word(i), None)

    def test_add_one_word(self):
        """Assert that adding a single word to a newly constructed Vocabulary works as expected"""
        v = Vocabulary()
        i = v.get_int("hello")
        self.assertEqual(i, 0)
        self.assertEqual(v.size(), 1)
        self.assertEqual(v.words(), ["hello"])
        self.assertEqual(v.get_int("hello"), i)
        self.assertEqual(v.get_word(0), "hello")


    def test_adding_words(self):
        """Assert that words are properly added to the vocabulary"""
        v = Vocabulary()
        tokens = "Four score and seven years ago".split()
        ints = list()
        for token in tokens:
            ints.append(v.get_int(token))

        self.assertEqual(v.words(), tokens)

        for token in tokens:
            i = v.get_int(token)
            self.assertNotEqual(i, None)
            t = v.get_word(i)
            self.assertEqual(t, token)

        for i in range(0, len(tokens)):
            self.assertNotEqual(i, None)
            t = v.get_word(i)
            self.assertEqual(t, tokens[i])


if __name__ == '__main__':
    unittest.main()
