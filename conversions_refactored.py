
def convertThat(self, fromUnit, toUnit, value):

    # Distance Conversions
    while fromUnit.lower() == 'miles':
        if toUnit.lower() == 'meters':
            return round(value * 1609.34, 2)
        elif toUnit.lower() == 'yards':
            return round(value * 1760, 2)
        elif toUnit.lower() == 'miles':
            return value
        else:
            raise Exception('ConversionNotPossibleException')

    while fromUnit.lower() == 'yards':
        if toUnit.lower() == 'meters':
            return round(value / 0.9144, 2)
        elif toUnit.lower() == 'miles':
            return round(value / 1760, 2)
        elif toUnit.lower() == 'yards':
            return value
        else:
            raise Exception('ConversionNotPossibleException')

    while fromUnit.lower() == 'meters':
        if toUnit.lower() == 'miles':
            return round(value / 1609.344, 2)
        elif toUnit.lower() == 'yards':
            return round(value * 1.094, 2)
        elif toUnit.lower() == 'meters':
            return value
        else:
            raise Exception('ConversionNotPossibleException')

    # Temperature Conversions
    while fromUnit.lower() == 'kelvin':
        if toUnit.lower() == 'celsius':
            return round(value - 273.15, 2)
        elif toUnit.lower() == 'fahrenheit':
            return round((value - 273.15) * (9/5) + 32, 2)
        elif toUnit.lower() == 'kelvin':
            return value
        else:
            raise Exception('ConversionNotPossibleException')

    while fromUnit.lower() == 'celsius':
        if toUnit.lower() == 'kelvin':
            return round(value + 273.15, 2)
        elif toUnit.lower() == 'fahrenheit':
            return round((value * 9/5) + 32, 2)
        elif toUnit.lower() == 'celsius':
            return value
        else:
            raise Exception('ConversionNotPossibleException')

    while fromUnit.lower() == 'fahrenheit':
        if toUnit.lower() == 'kelvin':
            return round((value + 459.67) * (5/9), 2)
        elif toUnit.lower() == 'celsius':
            return round((value - 32) / 1.8, 2)
        elif toUnit.lower() == 'fahrenheit':
            return value
        else:
            raise Exception('ConversionNotPossibleException')
