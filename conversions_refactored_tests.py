import unittest
import conversions_refactored as convert


class ConversionsRefactoredTest(unittest.TestCase):

    ################################
    # FROM MILES CONVERSIONS TESTS #
    ################################

    def test_convertThat_when_miles_to_meters(self):

        print('test_convertThat_when_miles_to_meters')

        fromUnit = 'miles'
        toUnit = 'meters'
        value = 3

        expected = 4828.03
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_miles_to_yards(self):

        print('test_convertThat_when_miles_to_yards')

        fromUnit = 'miles'
        toUnit = 'yards'
        value = 5

        expected = 8800
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_miles_to_miles(self):

        print('test_convertThat_when_miles_to_miles')

        fromUnit = 'miles'
        toUnit = 'miles'
        value = 3.6

        expected = 3.60
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_miles_to_celsius_exception(self):

        print('test_convertThat_when_miles_to_celsius_exception')

        fromUnit = 'miles'
        toUnit = 'celsius'
        value = 3.6

        with self.assertRaises(Exception):
            convert.convertThat(self, fromUnit, toUnit, value)

    ################################
    # FROM METER CONVERSIONS TESTS #
    ################################

    def test_convertThat_when_meter_to_miles(self):

        print('test_convertThat_when_meter_to_miles')

        fromUnit = 'meters'
        toUnit = 'miles'
        value = 3265.5

        expected = 2.03
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_meters_to_yards(self):

        print('test_convertThat_when_meters_to_yards')

        fromUnit = 'meters'
        toUnit = 'yards'
        value = 5

        expected = 5.47
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_meters_to_meters(self):

        print('test_convertThat_when_meters_to_meters')

        fromUnit = 'meters'
        toUnit = 'meters'
        value = 3.6

        expected = 3.60
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_meters_to_celsius_exception(self):

        print('test_convertThat_when_meters_to_celsius_exception')

        fromUnit = 'miles'
        toUnit = 'celsius'
        value = 3.6

        with self.assertRaises(Exception):
            convert.convertThat(self, fromUnit, toUnit, value)

    ################################
    # FROM YARDS CONVERSIONS TESTS #
    ################################

    def test_convertThat_when_yards_to_miles(self):

        print('test_convertThat_when_yards_to_miles')

        fromUnit = 'yards'
        toUnit = 'miles'
        value = 3265.5

        expected = 1.86
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_yards_to_meters(self):

        print('test_convertThat_when_yards_to_meters')

        fromUnit = 'yards'
        toUnit = 'meters'
        value = 5

        expected = 5.47
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_yards_to_yards(self):

        print('test_convertThat_when_yards_to_yards')

        fromUnit = 'yards'
        toUnit = 'yards'
        value = 3.6

        expected = 3.60
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_yards_to_celsius_exception(self):

        print('test_convertThat_when_yards_to_celsius_exception')

        fromUnit = 'yards'
        toUnit = 'celsius'
        value = 3.6

        with self.assertRaises(Exception):
            convert.convertThat(self, fromUnit, toUnit, value)

    ##################################
    # FROM CELSIUS CONVERSIONS TESTS #
    ##################################

    def test_convertThat_when_celsius_to_kelvin(self):

        print('test_convertThat_when_celsius_to_kelvin')

        fromUnit = 'celsius'
        toUnit = 'kelvin'
        value = 35.2

        expected = 308.35
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_celsius_to_fahrenheit(self):

        print('test_convertThat_when_celsius_to_fahrenheit')

        fromUnit = 'celsius'
        toUnit = 'fahrenheit'
        value = 35.2

        expected = 95.36
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_celsius_to_celsius(self):

        print('test_convertThat_when_yards_to_yards')

        fromUnit = 'celsius'
        toUnit = 'celsius'
        value = 28.32

        expected = 28.32
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_celsius_to_meters_exception(self):

        print('test_convertThat_when_yards_to_celsius_exception')

        fromUnit = 'celsius'
        toUnit = 'meters'
        value = 3.6

        with self.assertRaises(Exception):
            convert.convertThat(self, fromUnit, toUnit, value)

    #####################################
    # FROM FAHRENHEIT CONVERSIONS TESTS #
    #####################################

    def test_convertThat_when_fahrenheit_to_kelvin(self):

        print('test_convertThat_when_fahrenheit_to_kelvin')

        fromUnit = 'fahrenheit'
        toUnit = 'kelvin'
        value = 35.2

        expected = 274.93
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_fahrenheit_to_celsius(self):

        print('test_convertThat_when_fahrenheit_to_celsius')

        fromUnit = 'fahrenheit'
        toUnit = 'celsius'
        value = 35.2

        expected = 1.78
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_fahrenheit_to_fahrenheit(self):

        print('test_convertThat_when_fahrenheit_to_fahrenheit')

        fromUnit = 'fahrenheit'
        toUnit = 'fahrenheit'
        value = 28.32

        expected = 28.32
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_fahrenheit_to_meters_exception(self):

        print('test_convertThat_when_fahrenheit_to_meters_exception')

        fromUnit = 'fahrenheit'
        toUnit = 'meters'
        value = 3.6

        with self.assertRaises(Exception):
            convert.convertThat(self, fromUnit, toUnit, value)

    #################################
    # FROM KELVIN CONVERSIONS TESTS #
    #################################

    def test_convertThat_when_kelvin_to_fahrenheit(self):

        print('test_convertThat_when_kelvin_to_fahrenheit')

        fromUnit = 'kelvin'
        toUnit = 'fahrenheit'
        value = 35.2

        expected = -396.31
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_kelvin_to_celsius(self):

        print('test_convertThat_when_kelvin_to_celsius')

        fromUnit = 'kelvin'
        toUnit = 'celsius'
        value = 35.2

        expected = -237.95
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_kelvin_to_kelvin(self):

        print('test_convertThat_when_kelvin_to_kelvin')

        fromUnit = 'fahrenheit'
        toUnit = 'fahrenheit'
        value = 28.32

        expected = 28.32
        actual = convert.convertThat(self, fromUnit, toUnit, value)

        self.assertEqual(expected, actual)

    def test_convertThat_when_kelvin_to_meters_exception(self):

        print('test_convertThat_when_kelvin_to_meters_exception')

        fromUnit = 'kelvin'
        toUnit = 'meters'
        value = 3.6

        with self.assertRaises(Exception):
            convert.convertThat(self, fromUnit, toUnit, value)


if __name__ == '__main__':
    unittest.main()