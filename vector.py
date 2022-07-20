class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector ({self.x:.3f}, {self.y:.3f})"

    def __abs__(self) -> float:
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 3)

    def __add__(self, other: "Vector"):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector"):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        raise Exception('Вектор можно умножить либо на число, либо на другой вектор!')

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        raise Exception('С присваиванием вектор можно умножить только на число!')
