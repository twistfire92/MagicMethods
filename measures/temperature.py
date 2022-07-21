from . import Measure


class Celsius(Measure, sign='°C'):

    def __init__(self, value=0.0):
        self.value = value

    def __get__(self, obj, owner):
        return self.value

    def __set__(self, obj, value):
        self.value = float(value)


class Fahrenheit(Measure, sign='°F'):

    def __get__(self, obj, owner):
        return (getattr(obj, Celsius.name) * 9 / 5) + 32

    def __set__(self, obj, value):
        setattr(obj, Celsius.name, (float(value) - 32) * 5 / 9)


class Kelvin(Measure, sign='°K'):

    def __get__(self, obj, owner):
        return getattr(obj, Celsius.name) + 273.15

    def __set__(self, obj, value):
        setattr(obj, Celsius.name, value - 273.15)


__all__ = ["Celsius", "Fahrenheit", "Kelvin"]
