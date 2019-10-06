

def convertCelsiusToKelvin(self, celsius):
    k = celsius + 273.15
    return round(k, 2)


def convertCelsiusToFahrenheit(self, celsius):

    f = (celsius * 1.8) + 32
    return round(f, 2)

def convertFahrenheitToCelsius(self, fahrenheit):

    c = (fahrenheit - 32) / 1.8
    return round(c, 2)

def convertFahrenheitToKelvin(self, fahrenheit):

    k = (fahrenheit + 459.67) * (5/9)
    return round(k, 2)

def convertKelvinToCelsius(self, kelvin):

    c = kelvin - 273.15
    return round(c, 2)

def convertKelvinToFahrenheit(self, kelvin):

    f = (kelvin - 273.15) * (9/5) + 32
    return round(f, 2)
