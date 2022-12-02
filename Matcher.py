from datetime import datetime

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod


class IsGivenDayOfWeek(BaseMatcher):
    def __init__(self, day):
        self.day = day  # Monday is 0, Sunday is 6

    def _matches(self, item):
        if not hasmethod(item, "weekday"):
            return False
        return item.weekday() == self.day

    def describe_to(self, description):
        day_as_string = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        description.append_text("calendar date falling on ").append_text(
            day_as_string[self.day]
        )


def on_a_saturday():
    return IsGivenDayOfWeek(5)


class IsLeapYear(BaseMatcher):

    def _matches(self, item):
        var = item.year
        if (var % 400 == 0) and (var % 100 == 0):
            return True
        elif (var % 4 == 0) and (var % 100 != 0):
            return True
        else:
            return False

    def describe_to(self, description):
        description.append_text("must be leap")


def is_leap_year():
    return IsLeapYear()


class IsPrimeNumber(BaseMatcher):

    def _matches(self, item):
        num = item
        if num > 1:
            # Iterate from 2 to n / 2
            for i in range(2, int(num / 2) + 1):
                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if (num % i) == 0:
                    return False

            else:
                return True
        else:
            return False

    def describe_to(self, description):
        description.append_text("must be prime")


def is_prime_number():
    return IsPrimeNumber()


import unittest

from hamcrest import *


class MatcherHamcrest(unittest.TestCase):

    def setUp(self):
        self.temp = None

    def test_date_is_on_a_saturday(self):
        self.temp = datetime(2008, 4, 26)
        assert_that(self.temp, is_(on_a_saturday()))

    def test_date_is_not_on_a_saturday(self):
        self.temp = datetime(2008, 4, 27)
        assert_that(self.temp, is_not(on_a_saturday()))

    def test_year_is_leap(self):
        self.temp = datetime(2012, 4, 26)
        assert_that(self.temp, is_(is_leap_year()))

    def test_year_is_not_leap(self):
        self.temp = datetime(2013, 4, 26)
        assert_that(self.temp, is_not(is_leap_year()))

    def test_year_is_prime_number(self):
        self.temp = 2
        assert_that(self.temp, is_(is_prime_number()))

    def test_year_is_prime_number2(self):
        self.temp = 5
        assert_that(self.temp, is_(is_prime_number()))

    def test_year_is_not_prime_number(self):
        self.temp = 4
        assert_that(self.temp, is_not(is_prime_number()))

    def test_year_is_not_prime_number2(self):
        self.temp = 8
        assert_that(self.temp, is_not(is_prime_number()))
