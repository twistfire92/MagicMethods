from converter import Converter

if __name__ == '__main__':
    converter = Converter()

    converter.fahrenheit = 80
    print('80 градусов по Фаренгейту:', converter, sep='\n', end='\n\n')

    converter.celsius = 37
    print('37 градусов по Цельсию:', converter, sep='\n', end='\n\n')

    converter.kelvin = 400
    print('400 градусов по Кельвину:', converter, sep='\n', end='\n\n')
