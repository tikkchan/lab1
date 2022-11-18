[![code checks](https://github.com/tikkchan/lab1/actions/workflows/main.yml)](https://github.com/tikkchan/lab1/actions/workflows/main.yml)
#Тестирование приложения "Калькулятор" с помощью библиотеки pytest

__Pytest__ - это платформа тестирования программного обеспечения, основанная на языке программирования Python. Он может быть использован для написания различных типов тестов программного обеспечения, включая модульные тесты, интеграционные тесты, сквозные тесты и функциональные тесты.

##Было реализовано 24 теста:
___Тест 1.___
```python
def test_add():
    num1 = 2
    num2 = 2
    res = func.add(num1, num2)
    assert res == 4
```
Тест вызывает функцию __add__ и проверяет, что функция сложения работает корректно.
```python
def add(num1, num2):
    '''сложение двух чисел'''
    sumn = num1 + num2
    print(sumn)
    return sumn
```

___Тест 2.___
```python
def test_subtract():
    num1 = 2
    num2 = 2
    res = func.subtract(num1, num2)
    assert res == 0
```
Тест вызывает функцию __subtract__ и ппроверяет, что функция вычитания работает корректно.
```python
def subtract(num1, num2):
    '''вычитание двух чисел'''
    minn = num1 - num2
    print(minn)
    return minn
```
___Тест 3.___
```python
def test_multiply():
    num1 = 2
    num2 = 3
    res = func.multiply(num1, num2)
    assert res == 6
```
Тест вызывает функцию __multiply__ и проверяет, что функция умножения работает корректно.
```python
def multiply(num1, num2):
    '''умножение двух чисел'''
    umn = num1 * num2
    print(umn)
    return umn
```
___Тесты 4-5.___
```python
def test_divide_exception():
    try:
        func.divide(5, 0)
    except ZeroDivisionError as e:
        assert e

def test_divide():
    num1 = 2
    num2 = 2
    res = func.divide(num1, num2)
    assert res == 1
```
Тесты вызывают функцию __divide__ и проверяет, что функция деления работает корректно.
Отрицательный тест вызывает функцию __divide__ передавая в качестве параметров число, которое нужно разделить на ноль. Результат division by zero
```python
def divide(num1, num2):
    '''деление двух чисел'''
    try:
        delenie = num1 / num2
        print(delenie)
        return delenie
    except ZeroDivisionError as e:
        print(e)
```
___Тест 6.___
```python
def test_exponent():
    num1 = 2
    power = 3
    res = func2.exponent(num1, power)
    assert res == 8
```
Тест вызывает функцию __exponent__ и проверяет, что функция возведения в степень работает корректно.
```python
def exponent(num, power):
    '''возведение числа в степень'''
    exponent = num ** power
    print(exponent)
    return exponent
```
___Тесты 7-8.___
```python
def test_sqrt():
    num = 4
    res = func2.sqrt(num)
    assert res == 2

def test_sqrt_exception():
    num = -4
    res = func2.sqrt(num)
    assert res == "Только рациональные числа"
```
Тесты вызывают функцию __sqrt__ и проверяют, что функция квадратного корня работает корректно. Отрицательный тест вызывает функцию __sqrt__ передавая в качестве параметров отрицательное число. Результат - вывод сообщения "Только рациональные числа"
```python
def sqrt(num):
    '''квадратный корень'''
    if num >= 0:
        sqrt = num ** 0.5
        print(sqrt)
        return sqrt
    else:
        print("Только рациональные числа")
        return "Только рациональные числа"
```
___Тесты 9-10.___
```python
def test_cbrt():
    num = 8
    res = func2.cbrt(num)
    assert res == 2


def test_cbrt2():
    num = -8
    res = func2.cbrt(num)
    assert res == -2.0
```
Тесты вызывают функцию __cbrt__ и проверяют, что функция кубического корня работает корректно.
```python
def cbrt(num):
    '''кубический корень'''
    if num < 0:
        num = abs(num)
        cbrt = -1 * (num ** (1 / 3))
    else:
        cbrt = num ** (1 / 3)
    print(cbrt)
    return cbrt
```
___Тест 11.___
```python
def test_fact():
    num = 5
    res = func2.fact(num)
    assert res == 120
```
Тесты вызывают функцию __fact__ и проверяет, что функция поиска факториала работает корректно.
```python
def fact(num):
    '''факториал числа'''
    if num <= 0:
        print("Факториал не существует для отрицательных чисел" if num < 0 else 'Факториал 0 равен 1')
    else:
        print(recurse_factor(num))
        return recurse_factor(num)
```
___Тест 12.___
```python
def test_sign():
    num = 0
    res = func2.sign(num)
    assert res == 0
```
Тесты вызывают функцию __sign__ и проверяет, что функция проверки знака числа работает корректно.
```python
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
```
___Тест 13.___
```python
def test_solve_qube2():
    res = func2.solve_qube2(12, 4, 8, 5)
    assert res == (
        -1.8623879412594293, (0.13119397062971466 + 1.1275887015236796j), (0.13119397062971452 - 1.1275887015236796j)
```
Тесты вызывают функцию __solve_qube2__ и проверяет, что функция нахождения кофф. кубического уравнения работает корректно.
```python
def solve_qube2(a1, b1, c1, d1):
    print(solve_qube([a1, b1, c1, d1]))
    return (solve_qube([a1, b1, c1, d1]))
```
___Тесты 14-24.___
```python
def test_integr_add():
    assert main.select_func(1, 2, 2, 0, 0) == 4


def test_integr_subtract():
    assert main.select_func(2, 2, 2, 0, 0) == 0


def test_integr_multiply():
    assert main.select_func(3, 2, 3, 0, 0) == 6


def test_integr_divide():
    assert main.select_func(4, 2, 2, 0, 0) == 1


def test_integr_exponent():
    assert main.select_func(5, 2, 3, 0, 0) == 8


def test_integr_sqrt():
    assert main.select_func(6, 16, 0, 0, 0) == 4


def test_integr_cbrt():
    assert main.select_func(7, 27, 0, 0, 0) == 3


def test_integr_fact():
    assert main.select_func(8, 5, 0, 0, 0) == 120


def test_integr_solve_qube2():
    assert main.select_func(9, 12, 4, 8, 5) == (
        -1.8623879412594293, (0.13119397062971466 + 1.1275887015236796j), (0.13119397062971452 - 1.1275887015236796j))


def test_integr_divide_ex():
    try:
        main.select_func(4, 2, 0, 0, 0)
    except ZeroDivisionError as e:
        assert e

def test_integr_sqrt_ex():
    assert main.select_func(6, -4, 0, 0, 0) == "Только рациональные числа"
```
Тесты вызывают функцию __select_func__ и проверяют, что происходит вызов других функций внутри неё (возвращается верное значение).
```python
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
```
