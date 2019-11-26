# -*- coding: utf-8 -*-

# unittest is an existing library in Python
import unittest

from spellchecker import SpellChecker

# good habit to put the word "test" followed by the function you want to test
class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.spellChecker = SpellChecker()
        self.spellChecker.load_words('spell.words')
# making sure the file has 53751 lines
    def test_dictionary_of_words(self):
        self.assertTrue(len(self.spellChecker.words) == 53751)
       
    def test_spell_checker(self):
        # Check the list of profanities word
        self.assertTrue(self.spellChecker.check_profanities(['fuck','shit']))
        # Check the word to see if it's true or false (assert)
        self.assertTrue(self.spellChecker.check_word('zygotic'))
        self.assertFalse(self.spellChecker.check_word('mistasdas'))
        # Looking at the failed words dict, should be 1 words mispelled
        # which means the len = 1
        self.assertTrue(len(self.spellChecker.check_words('zygotic mistasdas elementary')) == 1)
        # in below case, since everything's fine, failed words dict len = 0
        self.assertTrue(len(self.spellChecker.check_words('our first correct sentence')) == 0)
        self.assertTrue(len(self.spellChecker.check_words('Our first correct sentence.')) == 0)
        # Updating the failed wrds dict manually
        failed_words = self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary')
        # failed_profanities = self.spellChecker.check_profanities('naruto')
        # print(failed_profanities)
        # self.assertTrue(failed_profanities not in ['fuck','shit'])
        
        # re-testing said dict
        self.assertTrue(len(failed_words) == 2)
        self.assertTrue(failed_words[0]['word'] == 'mistasdas')
        self.assertTrue(failed_words[0]['line'] == 1)
        self.assertEquals(9, failed_words[0]['pos'])
        self.assertEquals('spelling', failed_words[0]['type'])
        self.assertTrue(failed_words[1]['word'] == 'spelllleeeing')
        self.assertTrue(failed_words[1]['line'] == 1)
        self.assertTrue(failed_words[1]['pos'] == 19)
        self.assertEquals('spelling', failed_words[1]['type'])
        #self.assertEquals(0,
        #    len(self.spellChecker.check_document('spell.words')))
        failed_profane_words = self.spellChecker.check_document('profanity.txt')
        self.assertEquals(3, len(failed_profane_words))
        self.assertEquals('profanity', failed_profane_words[0]['type'])

if __name__ == '__main__':
    unittest.main()
