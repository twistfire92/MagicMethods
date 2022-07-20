from converter import Converter

if __name__ == '__main__':
    converter = Converter()

    converter.fahrenheit = 80
    print(
        '80 градусов по Фаренгейту:',
        f"{converter.celsius = }",
        f"{converter.fahrenheit = }",
        f"{converter.kelvin = }",
        sep='\n',
        end='\n\n'
    )

    converter.fahrenheit = 50
    print(
        '50 градусов по Цельсию:',
        f"{converter.celsius = }",
        f"{converter.fahrenheit = }",
        f"{converter.kelvin = }",
        sep='\n',
        end='\n\n'
    )

    converter.fahrenheit = 348
    print(
        '348 градусов по Кельвину:',
        f"{converter.celsius = }",
        f"{converter.fahrenheit = }",
        f"{converter.kelvin = }",
        sep='\n',
        end='\n\n'
    )

