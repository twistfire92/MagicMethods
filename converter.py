from measures import Measure
from measures import temperature, distance
from pydoc import locate


class PrintMixin:
    """
    Класс-миксин реализующий метод __str__ в наследниках
    Название может быть любым, суффикс Mixin не обязателен
    """
    def __str__(self):
        rows = []
        for attr in self.__dir__():
            if not attr.startswith("__"):
                value = getattr(self, attr)
                sign = Measure.measure_sign_mapper.get(attr)
                rows.append(f"{sign:.<4}{value:.>10.2f}")
        return '\n'.join(rows)


def create_worker_class(module):

    class Worker(PrintMixin):
        pass

    for class_name in module.__all__:
        cls = locate(f'{module.__name__}.{class_name}')
        setattr(Worker, cls.name, cls())

    return Worker()


class Converter:
    temperature = create_worker_class(temperature)
    distance = create_worker_class(distance)
