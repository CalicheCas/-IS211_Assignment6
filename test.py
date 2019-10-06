import unittest
import conversions


class Test(unittest.TestCase):

    #############################################################
    #                   CELSIUS TO KELVIN                       #
    #############################################################

    def test_convertCelsiusToKelvin_when_celsius_is_0(self):

        print('test_convertCelsiusToKelvin_when_celsius_is_0')

        # :given
        celsius = 0

        # :when
        expected = 273.15
        actual = conversions.convertCelsiusToKelvin(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    def test_convertCelsiusToKelvin_when_celsius_is_negative(self):

        print('test_convertCelsiusToKelvin_when_celsius_is_negative')

        # :given
        celsius = -32

        # :when
        expected = 241.15
        actual = conversions.convertCelsiusToKelvin(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    def test_convertCelsiusToKelvin_when_celsius_is_positive(self):

        print('test_convertCelsiusToKelvin_when_celsius_is_positive')

        # :given
        celsius = 32

        # :when
        expected = 305.15
        actual = conversions.convertCelsiusToKelvin(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    def test_convertCelsiusToKelvin_when_exception_raised(self):

        print('test_convertCelsiusToKelvin_when_exception_raised')

        # :given
        celsius = 'someString'

        # :when
        with self.assertRaises(TypeError):
            conversions.convertCelsiusToKelvin(self, celsius)

    def test_convertCelsiusToKelvin_when_fraction(self):

        print('test_convertCelsiusToKelvin_when_fraction')
        # :given
        celsius = 33.21

        # :when
        expected = 306.36
        actual = conversions.convertCelsiusToKelvin(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    #############################################################
    #               CELSIUS TO FAHRENHEIT                       #
    #############################################################

    def test_convertCelsiusToFahrenheit_when_celsius_is_0(self):
        print('test_convertCelsiusToFahrenheit_when_celsius_is_0')

        # :given
        celsius = 0

        # :when
        expected = 32.00
        actual = conversions.convertCelsiusToFahrenheit(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    def test_convertCelsiusToFahrenheit_when_celsius_is_negative(self):

        print('test_convertCelsiusToFahrenheit_when_celsius_is_negative')
        # :given
        celsius = -30

        # :when
        expected = -22.00
        actual = conversions.convertCelsiusToFahrenheit(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    def test_convertCelsiusToFahrenheit_when_celsius_is_positive(self):

        print('test_convertCelsiusToFahrenheit_when_celsius_is_positive')

        # :given
        celsius = 18

        # :when
        expected = 64.4
        actual = conversions.convertCelsiusToFahrenheit(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    def test_convertCelsiusToFahrenheit_when_exception_raised(self):

        print('test_convertCelsiusToFahrenheit_when_exception_raised')

        # :given
        celsius = 'someString'

        # :when
        with self.assertRaises(TypeError):
            conversions.convertCelsiusToFahrenheit(self, celsius)

    def test_convertCelsiusToFahrenheit_when_fraction(self):

        print('test_convertCelsiusToFahrenheit_when_fraction')

        # :given
        celsius = 33.21

        # :when
        expected = 91.78
        actual = conversions.convertCelsiusToFahrenheit(self, celsius)

        # :then
        self.assertEqual(expected, actual)

    #############################################################
    #               FAHRENHEIT TO CELSIUS                       #
    #############################################################

    def test_convertFahrenheitToCelsius_when_fahrenheit_is_0(self):

        print('test_convertFahrenheitToCelsius_when_fahrenheit_is_0')

        # :given
        fahrenheit = 0

        # :when
        expected = -17.78
        actual = conversions.convertFahrenheitToCelsius(self, fahrenheit)

        # :then
        self.assertEqual(expected, actual)

    def test_convertFahrenheitToCelsius_when_fahrenheit_is_negative(self):

        print('test_convertFahrenheitToCelsius_when_fahrenheit_is_negative')

        # :given
        fahrenheit = -32

        # :when
        expected = -35.56
        actual = conversions.convertFahrenheitToCelsius(self, fahrenheit)

        # :then
        self.assertEqual(expected, actual)

    def test_convertFahrenheitToCelsius_when_fahrenheit_is_positive(self):

        print('test_convertFahrenheitToCelsius_when_fahrenheit_is_positive')

        # :given
        fahrenheit = 32

        # :when
        expected = 0
        actual = conversions.convertFahrenheitToCelsius(self, fahrenheit)

        # :then
        self.assertEqual(expected, actual)

    def test_convertFahrenheitToCelsius_when_exception_raised(self):

        print('test_convertFahrenheitToCelsius_when_exception_raised')

        # :given
        fahrenheit = 'someString'

        # :when
        with self.assertRaises(TypeError):
            conversions.convertFahrenheitToCelsius(self, fahrenheit)

    def test_convertFahrenheitToCelsius_when_fraction(self):

        print('test_convertFahrenheitToCelsius_when_fraction')
        # :given
        fahrenheit = 33.21

        # :when
        expected = 0.67
        actual = conversions.convertFahrenheitToCelsius(self, fahrenheit)

        # :then
        self.assertEqual(expected, actual)

    #############################################################
    #               FAHRENHEIT TO KELVIN                        #
    #############################################################

    def test_convertFahrenheitToKelvin_when_fahrenheit_is_0(self):
        print('test_convertFahrenheitToKelvin_when_fahrenheit_is_0')

        # :given
        fahrenheit = 0

        # :when
        expected = 255.37
        actual = conversions.convertFahrenheitToKelvin(self, fahrenheit)

        # :then
        self.assertEqual(expected, actual)

    def test_convertFahrenheitToKelvin_when_fahrenheit_is_negative(self):

        print('test_convertFahrenheitToKelvin_when_fahrenheit_is_negative')
        # :given
        fahrenheit = -30

        # :when
        expected = 238.71
        actual = conversions.convertFahrenheitToKelvin(self, fahrenheit)

        # :then
        self.assertEqual(expected, actual)

    def test_convertFahrenheitToKelvin_when_fahrenheit_is_positive(self):

        print('test_convertFahrenheitToKelvin_when_fahrenheit_is_positive')

        # :given
        fahrenheit = 18

        # :when
        expected = 265.37
        actual = conversions.convertFahrenheitToKelvin(self, fahrenheit)

        # :then
        self.assertEqual(expected, actual)

    def test_convertFahrenheitToKelvin_when_exception_raised(self):

        print('test_convertFahrenheitToKelvin_when_exception_raised')

        # :given
        fahrenheit = 'someString'

        # :when
        with self.assertRaises(TypeError):
            conversions.convertFahrenheitToKelvin(self, fahrenheit)

    def test_convertFahrenheitToKelvin_when_fraction(self):

        print('test_convertFahrenheitToKelvin_when_fraction')

        # :given
        fahrenheit = 33.21

        # :when
        expected = 273.82
        actual = conversions.convertFahrenheitToKelvin(self, fahrenheit)

        # :then
        self.assertEqual(expected, actual)

    #############################################################
    #               KELVIN TO CELSIUS                           #
    #############################################################

    def test_convertKelvinToCelsius_when_celsius_is_0(self):

        print('test_convertKelvinToCelsius_when_celsius_is_0')

        # :given
        kelvin = 0

        # :when
        expected = -273.15
        actual = conversions.convertKelvinToCelsius(self, kelvin)

        # :then
        self.assertEqual(expected, actual)

    def test_convertKelvinToCelsius_when_celsius_is_negative(self):

        print('test_convertKelvinToCelsius_when_celsius_is_negative')

        # :given
        kelvin = -32

        # :when
        expected = -305.15
        actual = conversions.convertKelvinToCelsius(self, kelvin)

        # :then
        self.assertEqual(expected, actual)

    def test_convertKelvinToCelsius_when_celsius_is_positive(self):

        print('test_convertKelvinToCelsius_when_celsius_is_positive')

        # :given
        kelvin = 32

        # :when
        expected = -241.15
        actual = conversions.convertKelvinToCelsius(self, kelvin)

        # :then
        self.assertEqual(expected, actual)

    def test_convertKelvinToCelsius_when_exception_raised(self):

        print('test_convertKelvinToCelsius_when_exception_raised')

        # :given
        kelvin = 'someString'

        # :when
        with self.assertRaises(TypeError):
            conversions.convertKelvinToCelsius(self, kelvin)

    def test_convertKelvinToCelsius_when_fraction(self):

        print('test_convertKelvinToCelsius_when_fraction')
        # :given
        kelvin = 33.21

        # :when
        expected = -239.94
        actual = conversions.convertKelvinToCelsius(self, kelvin)

        # :then
        self.assertEqual(expected, actual)

    #############################################################
    #               KELVIN  TO FAHRENHEIT                       #
    #############################################################

    def test_convertKelvinToFahrenheit_when_celsius_is_0(self):
        print('test_convertKelvinToFahrenheit_when_celsius_is_0')

        # :given
        kelvin = 0

        # :when
        expected = -459.67
        actual = conversions.convertKelvinToFahrenheit(self, kelvin)

        # :then
        self.assertEqual(expected, actual)

    def test_convertKelvinToFahrenheit_when_celsius_is_negative(self):

        print('test_convertKelvinToFahrenheit_when_celsius_is_negative')
        # :given
        kelvin = -30

        # :when
        expected = -513.67
        actual = conversions.convertKelvinToFahrenheit(self, kelvin)

        # :then
        self.assertEqual(expected, actual)

    def test_convertKelvinToFahrenheit_when_celsius_is_positive(self):

        print('test_convertKelvinToFahrenheit_when_celsius_is_positive')

        # :given
        kelvin = 18

        # :when
        expected = -427.27
        actual = conversions.convertKelvinToFahrenheit(self, kelvin)

        # :then
        self.assertEqual(expected, actual)

    def test_convertKelvinToFahrenheit_when_exception_raised(self):

        print('test_convertKelvinToFahrenheit_when_exception_raised')

        # :given
        kelvin = 'someString'

        # :when
        with self.assertRaises(TypeError):
            conversions.convertKelvinToFahrenheit(self, kelvin)

    def test_convertKelvinToFahrenheit_when_fraction(self):

        print('test_convertKelvinToFahrenheit_when_fraction')

        # :given
        kelvin = 33.21

        # :when
        expected = -399.89
        actual = conversions.convertKelvinToFahrenheit(self, kelvin)

        # :then
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

