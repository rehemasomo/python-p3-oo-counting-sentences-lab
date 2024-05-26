#!/usr/bin/env python3

import pytest
import io
import sys
from count_sentences import MyString

class TestMyString:
    '''Class MyString in count_sentences.py'''

    def test_class_exists(self):
        '''is a class with the name "MyString".'''
        assert(MyString)

    def test_value_string(self):
        '''prints "The value must be a string." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        string = MyString()
        with pytest.raises(ValueError):
            string.value = 123

    def test_value_string(self):
        '''prints "The value must be a string." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        string = MyString()
        with pytest.raises(ValueError):
            string.value = 123

    def test_is_sentence_method(self):
        '''contains a method called "is_sentence".'''
        assert(MyString().is_sentence)

    def test_is_question_method(self):
        '''contains a method called "is_question".'''
        assert(MyString().is_question)

    def test_is_exclamation_method(self):
        '''contains a method called "is_exclamation".'''
        assert(MyString().is_exclamation)

    def test_count_sentences_method(self):
        '''contains a method called "count_sentences".'''
        assert(MyString().count_sentences)
