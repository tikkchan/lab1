import sys

import func
import func2


def main():
    while True:
        # Taking input from the user
        try:
            select = int(input("Please select operation -\n"
                               "1. Сложение\n"
                               "2. Вычитание\n"
                               "3. Умножение\n"
                               "4. Деление\n"
                               "5. Возведение в степень\n"
                               "6. Квадратный корень\n"
                               "7. Кубический корень\n"
                               "8. Факториал\n"
                               "9. Найти корни кубиечского уравнения\n"
                               "10. Выход\n"))
            if select <= 5:
                num1 = int(input("Введите число 1: "))
                num2 = int(input("Введите число 2: "))
                num3 = 0
                num4 = 0
            elif select <= 8:
                num1 = int(input("Введите число: "))
                num2 = 0
                num3 = 0
                num4 = 0
            elif select == 9:
                num1 = int(input("Введите коэффициент 1: "))
                num2 = int(input("Введите коэффициент 2: "))
                num3 = int(input("Введите коэффициент 3: "))
                num4 = int(input("Введите коэффициент 4: "))

        except ValueError as e:
            print(f'{e} Error,\n Invalid Option...')
            continue
        select_func(select, num1, num2, num3, num4)


def select_func(select, num1, num2, num3, num4):
    if select == 1:
        return (func.add(num1, num2))

    elif select == 2:
        return (func.subtract(num1, num2))

    elif select == 3:
        return (func.multiply(num1, num2))

    elif select == 4:
        return (func.divide(num1, num2))

    elif select == 5:
        return (func2.exponent(num1, num2))

    elif select == 6:
        return (func2.sqrt(num1))

    elif select == 7:
        return (func2.cbrt(num1))

    elif select == 8:
        return (func2.fact(num1))

    elif select == 9:
        return (func2.solve_qube2(num1, num2, num3, num4))

    elif select == 10:
        print("До встречи!")
        exit(0)

    else:
        print("Invalid input!")


if __name__ == "__main__":
    main()
