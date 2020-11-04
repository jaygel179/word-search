from unittest import TestCase

from ..models import Word


class TestWordModel(TestCase):
    def test_default_values(self):
        word = Word()

        assert word.text == ""
        assert word.start_x == 0
        assert word.start_y == 0
        assert word.end_x == 0
        assert word.end_y == 0
        assert word.found is False

    def test_setters_and_getters(self):
        word = Word("DOG")
        word.start_x = 1
        word.start_y = 1
        word.end_x = 3
        word.end_y = 1
        word.found = True

        assert word.text == "DOG"
        assert word.start_x == 1
        assert word.start_y == 1
        assert word.end_x == 3
        assert word.end_y == 1
        assert word.found is True

    def test_found(self):
        word = Word("DOG")
        word.start_x = 1
        word.start_y = 1
        word.end_x = 3
        word.end_y = 1
        word.found = True

        assert str(word) == "DOG(1,1)(3,1)"

    def test_not_found(self):
        word = Word("DOG")

        assert str(word) == "DOG not found"

    def test_insensitive_name(self):
        word = Word("dog")

        assert str(word) == "DOG not found"
