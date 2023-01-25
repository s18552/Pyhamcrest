import string

alphabet = set(string.ascii_lowercase)


class App:
    def is_panagram(self, str):
        if any(i.isdigit() for i in str) or str.__len__() < 1:
            raise Exception
        return sum(1 for i in set(str) if 96 < ord(i) <= 122) == 26


import unittest


class PanagramTest(unittest.TestCase):
    def setUp(self):
        self.temp = App()

    def test_is_panagram(self):
        result = self.temp.is_panagram('The quick brown fox jumps over the lazy dog')
        self.assertEqual(result, True)

    def test_is_panagram2(self):
        result = self.temp.is_panagram('Sex prof gives back no quiz with mild joy.')
        self.assertEqual(result, True)

    def test_is_not_panagram(self):
        result = self.temp.is_panagram('abcdefghjiklop')
        self.assertEqual(result, False)

    def test_is_not_panagram2(self):
        result = self.temp.is_panagram('abcdefghjiklopsdfgsdfsdfs')
        self.assertEqual(result, False)

    def test_arg_has_digit(self):
        self.assertRaises(Exception, self.temp.is_panagram, 'the quick brown fox jumps ov2er the lazy dog')

    def test_arg_is_empty(self):
        self.assertRaises(Exception, self.temp.is_panagram, '')

    def tearDown(self):
        self.temp = None
