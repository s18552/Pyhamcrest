class FizzBuzz:

    def game(self, num):
        if (num % 5) == 0 and (num % 3) == 0:
            return 'FizzBuzz'
        elif (num % 5) == 0:
            return 'Buzz'
        elif (num % 3) == 0:
            return 'Fizz'
        else:
            raise Exception("Error in FizzBuzz")


import unittest


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.temp = FizzBuzz()

    def test_positive_for_Buzz(self):
        self.assertEqual('Buzz', self.temp.game(5))

    def test_positive_for_Fizz(self):
        self.assertEqual('Fizz', self.temp.game(3))

    def test_positive_for_FizzBuzz(self):
        self.assertEqual('FizzBuzz', self.temp.game(15))

    def test_Fizz_Buzz_Exceptions(self):
        self.assertRaises(Exception, self.temp.game, 7)

    def test_fizz_buzz_exceptions_for_wrong_type_arg(self):
        self.assertRaises(Exception, self.temp.game, "15")

    def test_fizz_buzz_exceptions_for_too_great_arg(self):
        self.assertRaises(Exception, self.temp.game, 135443543513451435351345463456345634563645634563456345634563464453212342134)

    def tearDown(self):
        self.temp = None

