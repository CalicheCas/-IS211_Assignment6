import unittest
import conversions


class Test(unittest.TestCase):

    def test_convertCelsiusToKelvin_when_celsius_is_0(self):

        # :given
        celsius = 0

        # :when
        expected = 273.15
        actual = conversions.convertCelsiusToKelvin(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    def test_convertCelsiusToKelvin_when_celsius_is_negative(self):

        # :given
        celsius = -32

        # :when
        expected = 241.15
        actual = conversions.convertCelsiusToKelvin(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    def test_convertCelsiusToKelvin_when_celsius_is_positive(self):

        # :given
        celsius = 32

        # :when
        expected = 305.15
        actual = conversions.convertCelsiusToKelvin(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    def test_convertCelsiusToKelvin_when_exception_raised(self):

        # :given
        celsius = 'someString'

        # :when
        with self.assertRaises(TypeError):
            conversions.convertCelsiusToKelvin(self, celsius)

    def test_convertCelsiusToKelvin_when_fraction(self):
        # :given
        celsius = 33.21

        # :when
        expected = 306.36
        actual = conversions.convertCelsiusToKelvin(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    def test_convertCelsiusToFahrenheit_when_celsius_is_0(self):

        # :given
        celsius = 0

        # :when
        expected = 32.00
        actual = conversions.convertCelsiusToFahrenheit(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    def test_convertCelsiusToFahrenheit_when_celsius_is_negative(self):

        # :given
        celsius = -30

        # :when
        expected = -22.00
        actual = conversions.convertCelsiusToFahrenheit(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    def test_convertCelsiusToFahrenheit_when_celsius_is_positive(self):

        # :given
        celsius = 18

        # :when
        expected = 64.4
        actual = conversions.convertCelsiusToFahrenheit(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    def test_convertCelsiusToFahrenheit_when_exception_raised(self):

        # :given
        celsius = 'someString'

        # :when
        with self.assertRaises(TypeError):
            conversions.convertCelsiusToFahrenheit(self, celsius)

    def test_convertCelsiusToFahrenheit_when_fraction(self):
        # :given
        celsius = 33.21

        # :when
        expected = 91.78
        actual = conversions.convertCelsiusToFahrenheit(self, celsius)

        # :then
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

