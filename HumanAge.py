class App:
    def check_age(self, age, planet):
        if age < 0:
            raise Exception
        ratio = age / 31557600
        if planet == 'Ziemia':
            return round(ratio * 100) / 100.0
        elif planet == 'Merkury':
            return round(ratio / 0.2408467 * 100) / 100.0
        elif planet == 'Wenus':
            return round(ratio / 0.61519726 * 100) / 100.0
        elif planet == 'Mars':
            return round(ratio / 1.8808158 * 100) / 100.0
        elif planet == 'Jowisz':
            return round(ratio / 11.862615 * 100) / 100.0
        elif planet == 'Saturn':
            return round(ratio / 29.447498 * 100) / 100.0
        elif planet == 'Uran':
            return round(ratio / 84.016846 * 100) / 100.0
        elif planet == 'Neptun':
            return round(ratio / 164.79132 * 100) / 100.0
        else:
            raise Exception


import unittest


class HumanAgeTest(unittest.TestCase):
    def setUp(self):
        self.temp = App()

    def test_age_for_earth(self):
        age = self.temp.check_age(1000000000, 'Ziemia')
        self.assertEqual(age, 31.69)

    def test_age_for_mercury(self):
        age = self.temp.check_age(2134835688, 'Merkury')
        self.assertEqual(age, 280.88)

    def test_age_for_venus(self):
        age = self.temp.check_age(1134883228, 'Wenus')
        self.assertEqual(age, 58.46)

    def test_age_for_mars(self):
        age = self.temp.check_age(5134853688, 'Mars')
        self.assertEqual(age, 86.51)

    def test_age_for_jupiter(self):
        age = self.temp.check_age(6134245688, 'Jowisz')
        self.assertEqual(age, 16.39)

    def test_age_for_saturn(self):
        age = self.temp.check_age(7134865688, 'Saturn')
        self.assertEqual(age, 7.68)

    def test_age_for_uranus(self):
        age = self.temp.check_age(4135835688, 'Uran')
        self.assertEqual(age, 1.56)

    def test_age_is_wrong(self):
        self.assertRaises(Exception, self.temp.check_age, -1, 'Ziemia')

    def test_planet_is_wrong(self):
        self.assertRaises(Exception, self.temp.check_age, 10000000, 'Z2iemia')

    def tearDown(self):
        self.temp = None
