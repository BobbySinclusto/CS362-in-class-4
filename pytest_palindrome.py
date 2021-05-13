import palindrome
import pytest

def test_palindrome_good():
    assert palindrome.is_palindrome('testing') == False
    assert palindrome.is_palindrome('bob') == True
    assert palindrome.is_palindrome('racecar') == True
    assert palindrome.is_palindrome('pot top') == True

def test_palindrome_fail():
    assert palindrome.is_palindrome('this is definitely not a palindrome') == True

def test_palindrome_exceptions():
    with pytest.raises(TypeError):
        assert palindrome.is_palindrome(234)