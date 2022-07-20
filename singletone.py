class Singleton:
    _instance = None
    _counter = 0

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        cls._counter += 1
        print(f'Создано {cls._counter} экземпляров класса!')
        return cls._instance

    def __init__(self, param=None):
        if param:
            self.param = param


if __name__ == '__main__':
    s1 = Singleton(5)
    s2 = Singleton(7)
    s3 = Singleton(7)
    s4 = Singleton(7)
    s5 = Singleton(7)
    s6 = Singleton(3)

    print(
        s1.param,
        s2.param,
        id(s1),
        id(s2),
        s1 is s2,
        sep='\n'
    )

