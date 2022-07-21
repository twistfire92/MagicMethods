from converter import Converter

if __name__ == '__main__':
    converter = Converter()
    converter.temperature.celsius = 36.6
    converter.distance.metre = 300

    print(
        converter.temperature,
        converter.distance,
        sep='\n\n'
    )
