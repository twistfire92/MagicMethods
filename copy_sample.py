from copy import copy
from uuid import uuid4


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._id = uuid4()

    def __str__(self):
        return f'{self.name}, {self.age}, id: {self._id}'

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        result._id = uuid4()
        return result


user1 = User('Vasya', 25)

user2 = copy(user1)

if __name__ == '__main__':
    print(user1, user2, sep='\n')
