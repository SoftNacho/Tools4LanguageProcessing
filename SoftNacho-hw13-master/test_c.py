#!/usr/bin/python3


import unittest
import nltk
from d import Vocabulary
from c import Conditional
from c import create_vocab

class TestConditional(unittest.TestCase):

    def setUp(self):
        self.english_tokens = nltk.word_tokenize("All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.")
        self.spanish_tokens = nltk.word_tokenize("Todos los seres humanos nacen libres e iguales en dignidad y derechos y, dotados como están de razón y conciencia, deben comportarse fraternalmente los unos con los otros.")

        self.e_v = create_vocab(self.english_tokens)
        self.f_v = create_vocab(self.spanish_tokens)

    def test_create_english_vocab(self):
        """Assert that an initialized English vocabulary contains the expected values"""
        self.assertEqual(self.e_v.size(), 26)
        
        for token in self.english_tokens:
            i = self.e_v.get_int(token)
            t = self.e_v.get_word(i)

            self.assertEqual(t, token)
            self.assertGreaterEqual(i, 0)
            self.assertLess(i, len(self.english_tokens))


    def test_create_spanish_vocab(self):
        """Assert that an initialized English vocabulary contains the expected values"""
        self.assertEqual(self.f_v.size(), 26)
        
        for token in self.spanish_tokens:
            i = self.f_v.get_int(token)
            t = self.f_v.get_word(i)

            self.assertEqual(t, token)
            self.assertGreaterEqual(i, 0)
            self.assertLess(i, len(self.spanish_tokens))


    def test_conditional_get(self):
        """Assert that a conditional distribution initialized to zero has zero for all values"""
        c = Conditional("c", self.e_v, self.f_v, 0.0)

        self.assertEqual(self.e_v.size(), 26)
        self.assertEqual(self.f_v.size(), 26)

        for e in self.e_v.words():
            e_i = self.e_v.get_int(e)
            for f in self.f_v.words():
                f_i = self.f_v.get_int(f)
                v = c.get(e_i, f_i)
                self.assertEqual(v, 0.0)


    def test_conditional_set(self):
        """Assert that set works for a conditional distribution"""
        c = Conditional("c", self.e_v, self.f_v, 0.0)

        self.assertEqual(self.e_v.size(), 26)
        self.assertEqual(self.f_v.size(), 26)

        for e in self.e_v.words():
            e_i = self.e_v.get_int(e)
            for f in self.f_v.words():
                f_i = self.f_v.get_int(f)
                v = e_i * (1.0/(f_i+1))
                c.set(e_i, f_i, v)

        for e in self.e_v.words():
            e_i = self.e_v.get_int(e)
            for f in self.f_v.words():
                f_i = self.f_v.get_int(f)
                v = e_i * (1.0/(f_i+1))
                self.assertEqual(c.get(e_i, f_i), v)


    def test_string(self):
        """Test the __str__ method of Conditional"""

        e_v = create_vocab(["a", "b", "c"])
        f_v = create_vocab(["y", "z"])
        c = Conditional("c", e_v, f_v, -1.7)

        s = """c[a | y] = -1.7
c[a | z] = -1.7
c[b | y] = -1.7
c[b | z] = -1.7
c[c | y] = -1.7
c[c | z] = -1.7
"""

        self.assertEqual(str(c), s)




if __name__ == '__main__':
    unittest.main()
