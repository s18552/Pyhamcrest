class Car:
    # def __init__(self, year, model):
    #     self.__year = year
    #     self.__model = model
    #     self.__speed = 0

    def __init__(self):
        self.__model = None
        self.__year = None
        self.__speed = 0.0

    def accelarate(self):
        self.__speed += 5.0

    def brake(self):
        self.__speed -= 5.0

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

    def get_filled_array(self):
        car1 = Car()
        car2 = Car()
        arr = {car1, car2}
        return arr


import unittest

from hamcrest import *


class CarTest(unittest.TestCase):
    def setUp(self):
        self.temp = Car()

    def test_check_year_of_production(self):
        self.temp.set_year(2018)

        assert_that(self.temp.get_year(), equal_to(2018))

    def test_instance(self):
        assert_that(self.temp, is_(Car))

    def test_instance_2(self):
        assert_that(self.temp, instance_of(Car))

    def test_check_invalid_year_of_production(self):
        assert_that(calling(self.temp.set_year).with_args('Audi'), raises(Exception))

    def test_check_negative_year_of_production(self):
        assert_that(calling(self.temp.set_year).with_args(-81), raises(Exception))


    def test_check_model(self):
        self.temp.set_model('BMW')

        assert_that(self.temp.get_model(), has_string('BMW'))

    def test_check_invalid_model(self):
        assert_that(calling(self.temp.set_model).with_args(1), raises(Exception))

    def test_check_speed(self):
        self.temp.accelarate()
        self.temp.accelarate()
        self.temp.accelarate()

        assert_that(self.temp.get_speed(), all_of(is_(15), greater_than(14)))

    def test_check_array(self):
        arr = self.temp.get_filled_array()
        arr.clear()

        assert_that(arr, has_length(0))

    def test_check_array2(self):
        arr = self.temp.get_filled_array()
        car= Car()
        arr.add(car)

        assert_that(arr, all_of(has_length(3), has_item(car)))

    def tearDown(self):
        self.temp = None
