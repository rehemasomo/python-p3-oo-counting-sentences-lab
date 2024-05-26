#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError("Value must be a string")
        self._value = new_value

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        sentences = [sentence.strip() for sentence in self._value.split('.') if sentence.strip()]
        sentences += [sentence.strip() for sentence in self._value.split('?') if sentence.strip()]
        sentences += [sentence.strip() for sentence in self._value.split('!') if sentence.strip()]
        return len(sentences)

