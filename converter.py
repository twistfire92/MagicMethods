class Celsius:

    def __init__(self, value=0.0):
        self.value = value

    def __get__(self, obj, owner):
        return self.value

    def __set__(self, obj, value):
        self.value = float(value)


class Fahrenheit:

    def __get__(self, obj, owner):
        return (obj.celsius * 9 / 5) + 32

    def __set__(self, obj, value):
        obj.celsius = (float(value) - 32) * 5 / 9


class Kelvin:

    def __get__(self, obj, owner):
        return obj.celsius + 273.15

    def __set__(self, obj, value):
        obj.celsius = value - 273.15


class Converter:
    celsius = Celsius()
    fahrenheit = Fahrenheit()
    kelvin = Kelvin()

    def __str__(self):
        return "\n".join(
            [
                f"°C{self.celsius:.>10.2f}",
                f"°F{self.fahrenheit:.>10.2f}",
                f"°K{self.kelvin:.>10.2f}"
            ]
        )
