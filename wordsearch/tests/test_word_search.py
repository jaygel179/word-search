import os

from unittest import TestCase

from ..wordsearch import word_search


class TestWordSearch(TestCase):
    def test_file_exists(self):
        with self.assertRaises(Exception):
            word_search("wordsearch/tests/fixtures/not_exists.pzl")

    def test_file_extension(self):
        with self.assertRaises(Exception) as e:
            word_search("wordsearch/tests/fixtures/test.zxc")

        assert "Invalid file extension." in str(e.exception)

    def test_word_search_forward(self):
        word_search("wordsearch/tests/fixtures/animal.pzl")

        assert os.path.exists("wordsearch/tests/fixtures/animal.out")

        with open('wordsearch/tests/fixtures/animal.out') as output_file, open('wordsearch/tests/fixtures/animal.expected') as expected_file:
            for output_file_line, expected_file_line in zip(output_file, expected_file):
                assert output_file_line == expected_file_line

    def test_word_search_backward(self):
        word_search("wordsearch/tests/fixtures/suits.pzl")

        assert os.path.exists("wordsearch/tests/fixtures/suits.out")

        with open('wordsearch/tests/fixtures/suits.out') as output_file, open('wordsearch/tests/fixtures/suits.expected') as expected_file:
            for output_file_line, expected_file_line in zip(output_file, expected_file):
                assert output_file_line == expected_file_line

    def test_word_search_missing(self):
        word_search("wordsearch/tests/fixtures/lostDuck.pzl")

        assert os.path.exists("wordsearch/tests/fixtures/lostDuck.out")

        with open('wordsearch/tests/fixtures/lostDuck.out') as output_file, open('wordsearch/tests/fixtures/lostDuck.expected') as expected_file:
            for output_file_line, expected_file_line in zip(output_file, expected_file):
                assert output_file_line == expected_file_line

    def test_insensitive_data(self):
        word_search("wordsearch/tests/fixtures/insensitive.pzl")

        assert os.path.exists("wordsearch/tests/fixtures/insensitive.out")

        with open('wordsearch/tests/fixtures/insensitive.out') as output_file, open('wordsearch/tests/fixtures/insensitive.expected') as expected_file:
            for output_file_line, expected_file_line in zip(output_file, expected_file):
                assert output_file_line == expected_file_line
