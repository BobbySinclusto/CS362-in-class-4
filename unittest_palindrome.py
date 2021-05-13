import unittest
import palindrome

class TestCasePalindrome(unittest.TestCase):
    def test_palindrome_good(self):
        self.assertEqual(palindrome.is_palindrome('testing'), False)
        self.assertEqual(palindrome.is_palindrome('bob'), True)
        self.assertEqual(palindrome.is_palindrome('racecar'), True)
        self.assertEqual(palindrome.is_palindrome('pot top'), True)
    
    def test_palindrome_fail(self):
        self.assertEqual(palindrome.is_palindrome('this is definitely not a palindrome'), True)
    
    def test_palindrome_exceptions(self):
        self.assertRaises(TypeError, palindrome.is_palindrome, 234)

if __name__ == '__main__':
    unittest.main()