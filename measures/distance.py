class Meter:
    def __init__(self, value=0.0):
        self.value = value

    def __get__(self, obj, owner):
        return self.value

    def __set__(self, obj, value):
        self.value = float(value)


class Inch:
    def __get__(self, obj, owner):
        return obj.meter * 39.37

    def __set__(self, obj, value):
        obj.meter = value / 39.37
