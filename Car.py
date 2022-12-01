class Car:
    # def __init__(self, year, model):
    #     self.__year = year
    #     self.__model = model
    #     self.__speed = 0

    def __init__(self):
        self.__model = None
        self.__year = None
        self.__speed = 0

    def accelarate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def set_year(self, year):
        if type(year) == int and year > 0:
            self.__year = year
        else:
            raise Exception

    def set_model(self, model):
        if type(model) == int:
            raise Exception
        else:
            self.__model = model

    def get_year(self):
        return self.__year

    def get_model(self):
        return self.__model

    def get_speed(self):
        return self.__speed


import unittest


class CarTest(unittest.TestCase):
    def setUp(self):
        self.temp = Car()

    def test_check_year_of_production(self):
        self.temp.set_year(2018)

        self.assertEqual(2018, self.temp.get_year())

    def test_check_year_of_production2(self):
        self.temp.set_year(1995)

        self.assertEqual(1995, self.temp.get_year())

    def test_check_invalid_year_of_production(self):
        self.assertRaises(Exception, self.temp.set_year, 'Audi')

    def test_check_negative_year_of_production(self):
        self.assertRaises(Exception, self.temp.set_year, -81)

    def test_check_model(self):
        self.temp.set_model('BMW')

        self.assertEqual('BMW', self.temp.get_model())

    def test_check_model2(self):
        self.temp.set_model('Audi')

        self.assertEqual('Audi', self.temp.get_model())

    def test_check_invalid_model(self):
        self.assertRaises(Exception, self.temp.set_model, 1)

    def test_check_speed(self):
        self.temp.accelarate()
        self.temp.accelarate()
        self.temp.accelarate()

        self.assertEqual(15, self.temp.get_speed())

    def tearDown(self):
        self.temp = None
