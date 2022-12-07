from assertpy import add_extension


def is_5(self):
    if self.val != 5:
        return self.error(f'{self.val} is NOT 5!')
    return self


def is_even(self):
    if self.val % 2 != 0:
        return self.error(f'{self.val} is not even!')
    return self


def is_prime(self):
    num = self.val
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return self.error(f'{self.val} is not prime!')
        else:
            return self
    else:
        return self.error(f'{self.val} is not prime!')


add_extension(is_5)
add_extension(is_even)
add_extension(is_prime)

import unittest

from assertpy import *


class ClassTest(unittest.TestCase):

    def setUp(self):
        self.temp = None

    def test_number_is_5(self):
        assert_that(5).is_5()

    def test_number_is_even(self):
        assert_that(6).is_even()

    def test_number_is_prime(self):
        assert_that(2).is_prime()

    def tearDown(self):
        self.temp = None
