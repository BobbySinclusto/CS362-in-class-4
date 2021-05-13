import unittest
import wordcount

class TestCaseWordcount(unittest.TestCase):
    def test_wordcount_good(self):
        self.assertEqual(wordcount.wordcount('This sentence has five words.'), 5)
        self.assertEqual(wordcount.wordcount('       This   one has 4.     '), 4)
        self.assertEqual(wordcount.wordcount('don\'t count apostrophes?'), 3)
        self.assertEqual(wordcount.wordcount('tabs?\tlet\'s see'), 3)
    
    def test_wordcount_fail(self):
        self.assertEqual(wordcount.wordcount('this sentence definitely doesn\'t have 50 words'), 50)
    
    def test_wordcount_exceptions(self):
        self.assertRaises(TypeError, wordcount.wordcount, 234)

if __name__ == '__main__':
    unittest.main()