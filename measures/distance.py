from . import Measure


class Metre(Measure, sign='m'):

    def __init__(self, value=0.0):
        self.value = value

    def __get__(self, obj, owner):
        return self.value

    def __set__(self, obj, value):
        self.value = float(value)


class Inch(Measure, sign='in'):

    def __get__(self, obj, owner):
        return getattr(obj, Metre.name) * 39.37

    def __set__(self, obj, value):
        setattr(obj, Metre.name, float(value) / 39.37)


class Centimetre(Measure):
    def __get__(self, obj, owner):
        return getattr(obj, Metre.name, ) * 100

    def __set__(self, obj, value):
        setattr(obj, Metre.name, float(value) / 100)


class Foot(Measure, sign='ft'):
    def __get__(self, obj, owner):
        return getattr(obj, Inch.name, ) / 12

    def __set__(self, obj, value):
        setattr(obj, Inch.name, float(value) * 12)


__all__ = ["Metre", "Inch", "Centimetre", "Foot"]
