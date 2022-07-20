from vector import Vector

if __name__ == '__main__':
    v1 = Vector(3, 4)
    v2 = Vector(1, 1)
    v3 = Vector(-2, 5)

    print('Базовая инфорамация о векторе:', v1, sep='\n', end='\n\n')

    # module = abs(v1)
    # print('Модуль (длина) вектора v1:', module, sep='\n', end='\n\n')
    #
    # new_vector = v1 + v2
    # print('Сумма векторов v1 v2:', new_vector, sep='\n', end='\n\n')
    #
    # new_vector = v3 - v2
    # print('Разность векторов v3 v2:', new_vector, sep='\n', end='\n\n')
    #
    # new_vector = v1 * 5
    # print('Умножение вектора v1 на число 5:', new_vector, sep='\n', end='\n\n')
    #
    # v2 *= 3
    # print('Умножение вектора 2 на число 3 c присваиванием:', v2, sep='\n', end='\n\n')
    #
    # scalar = v1 * v3
    # print('Скалярное произведение векторов v1 v3:', scalar, sep='\n', end='\n\n')
    #
    # print('Попытка умножить вектор v1 на строку:')
    # try:
    #     v1 * 'fsdfs'
    # except Exception as e:
    #     print(e, end='\n\n')
    #
    # print('Попытка умножить с присваиванием вектор v1 на вектор v2:')
    # try:
    #     v1 *= v2
    # except Exception as e:
    #     print(e, end='\n\n')
