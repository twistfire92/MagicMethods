from measures.temperature import Celsius, Fahrenheit, Kelvin
from measures.distance import Meter, Inch


class Temperature:
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


class Distance:
    meter = Meter()
    inch = Inch()

    def __str__(self):
        return "\n".join(
            [
                f"m{self.meter:.>10.2f}",
                f'"{self.inch:.>10.2f}'
            ]
        )


class Converter:
    temperature = Temperature()
    distance = Distance()
