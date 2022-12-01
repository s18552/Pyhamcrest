class Employee:
    def __init__(self, lastname, firstname):
        self.__lastname = lastname
        self.__firstname = firstname

    def set_lastname(self, lastname):
        if any(i.isdigit() for i in lastname):
            raise Exception
        self.__lastname = lastname

    def set_firstname(self, firstname):
        if any(i.isdigit() for i in firstname):
            raise Exception
        self.__firstname = firstname

    def get_lastname(self):
        return self.__lastname

    def get_firstname(self):
        return self.__firstname


class ProductionWorker(Employee):
    # def __init__(self, change_number, pay_hour, lastname, firstname):
    #     super().__init__(lastname, firstname)
    #     self.__change_number = change_number
    #     self.__pay_hour = pay_hour

    def __init__(self):
        super().__init__(None, None)
        self.__change_number = None
        self.__pay_hour = None

    def set_change_number(self, change_number):
        if change_number > 1 or change_number < 0 or type(change_number) != int:
            raise Exception
        self.__change_number = change_number

    def get_pay_hour(self):
        return self.__pay_hour

    def set_pay_hour(self, pay_hour):
        if pay_hour < 0 or type(pay_hour) != int:
            raise Exception
        self.__pay_hour = pay_hour

    def get_change_number(self):
        return self.__change_number


import unittest


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.temp = ProductionWorker()

    def test_check_set_firstname(self):
        self.temp.set_firstname("Jan")

        self.assertEqual("Jan", self.temp.get_firstname())

    def test_check_set_firstname2(self):
        self.temp.set_firstname("Tomasz")

        self.assertEqual("Tomasz", self.temp.get_firstname())

    def test_check_set_invalid_firstname(self):
        self.assertRaises(Exception, self.temp.set_firstname, 0)

    def test_check_set_lastname(self):
        self.temp.set_lastname("Kowalski")

        self.assertEqual("Kowalski", self.temp.get_lastname())

    def test_check_set_lastname2(self):
        self.temp.set_lastname("Nowak")

        self.assertEqual("Nowak", self.temp.get_lastname())

    def test_check_set_invalid_lastname(self):
        self.assertRaises(Exception, self.temp.set_lastname, 0)

    def test_check_set_shift(self):
        self.temp.set_change_number(1)

        self.assertEqual(1, self.temp.get_change_number())

    def test_check_set_invalid_shift(self):
        self.assertRaises(Exception, self.temp.set_change_number, 2)

    def test_check_set_invalid_shift2(self):
        self.assertRaises(Exception, self.temp.set_change_number, "2")

    def test_check_set_pay_hour(self):
        self.temp.set_pay_hour(100)

        self.assertEqual(100, self.temp.get_pay_hour())

    def test_check_set_invalid_pay_hour(self):
        self.assertRaises(Exception, self.temp.set_pay_hour, -1)

    def test_check_set_invalid_pay_hour2(self):
        self.assertRaises(Exception, self.temp.set_pay_hour, "100")

    def tearDown(self):
        self.temp = None
