from typing import Type
import wordcount
import pytest

def test_wordcount_good():
    assert wordcount.wordcount('This sentence has five words.') == 5
    assert wordcount.wordcount('       This   one has 4.     ') == 4
    assert wordcount.wordcount('don\'t count apostrophes?') == 3
    assert wordcount.wordcount('tabs?\tlet\'s see') == 3

def test_wordcount_fail():
    assert wordcount.wordcount('this sentence definitely doesn\'t have 50 words') == 50

def test_wordcount_exceptions():
    with pytest.raises(TypeError):
        assert wordcount.wordcount(234)