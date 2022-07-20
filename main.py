from converter import Converter

if __name__ == '__main__':
    converter = Converter()

    converter.temperature.fahrenheit = 80
    print('80 градусов по Фаренгейту:', converter.temperature, sep='\n', end='\n\n')

    converter.distance.inch = 1
    print('1 дюйм:', converter.distance, sep='\n', end='\n\n')

    converter.distance.meter = 2
    print('2 метра:', converter.distance, sep='\n', end='\n\n')
