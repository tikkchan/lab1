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
        except ValueError as e:
            print(f'{e} Error,\n Invalid Option...')
            continue
        select_func(select)


def select_func(select):
    if select == 1:
        print("Вы выбрали функцию сложения")
        num1 = int(input("Введите число 1: "))
        num2 = int(input("Введите число 2: "))
        return(func.add(num1, num2))

    elif select == 2:
        num1 = int(input("Введите число 1: "))
        num2 = int(input("Введите число 2: "))
        func.subtract(num1, num2)

    elif select == 3:
        num1 = int(input("Введите число 1: "))
        num2 = int(input("Введите число 2: "))
        func.multiply(num1, num2)

    elif select == 4:
        num1 = int(input("Введите число 1: "))
        num2 = int(input("Введите число 2: "))
        func.divide(num1, num2)

    elif select == 5:
        num = int(input("Введите число, которое хотите возвести в степень: "))
        power = int(input("Введите степень числа: "))
        func2.exponent(num, power)

    elif select == 6:
        num = int(input("Введите число, из которого хотите извлечь квадратный корень: "))
        func2.sqrt(num)

    elif select == 7:
        num = int(input("Введите число, из которого хотите извлечь кубический корень: "))
        func2.cbrt(num)

    elif select == 8:
        num = int(input("Введите число, факториал которого вы хотите найти: "))
        func2.fact(num)

    elif select == 9:
        a1 = int(input("Введите коэффициент 1: "))
        b1 = int(input("Введите коэффициент 2: "))
        c1 = int(input("Введите коэффициент 3: "))
        d1 = int(input("Введите коэффициент 4: "))
        func2.solve_qube2(a1, b1, c1, d1)

    elif select == 10:
        print("До встречи!")
        sys.exit()

    else:
        print("Invalid input!")

if __name__ == "__main__":
    main()
