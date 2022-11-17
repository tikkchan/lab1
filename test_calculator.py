import sys

import pytest
import main
import func
import func2


def test_add():
    num1 = 2
    num2 = 2
    res = func.add(num1, num2)
    assert res == 4


def test_subtract():
    num1 = 2
    num2 = 2
    res = func.subtract(num1, num2)
    assert res == 0


def test_multiply():
    num1 = 2
    num2 = 3
    res = func.multiply(num1, num2)
    assert res == 6


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


def test_exponent():
    num1 = 2
    power = 3
    res = func2.exponent(num1, power)
    assert res == 8


def test_sqrt():
    num = 4
    res = func2.sqrt(num)
    assert res == 2


def test_sqrt_exception():
    num = -4
    res = func2.sqrt(num)
    assert res == "Только рациональные числа"


def test_cbrt():
    num = 8
    res = func2.cbrt(num)
    assert res == 2


def test_cbrt2():
    num = -8
    res = func2.cbrt(num)
    assert res == -2.0


def test_fact():
    num = 5
    res = func2.fact(num)
    assert res == 120


def test_sign():
    num = 0
    res = func2.sign(num)
    assert res == 0


def test_solve_qube2():
    res = func2.solve_qube2(12, 4, 8, 5)
    assert res == (
    -1.8623879412594293, (0.13119397062971466 + 1.1275887015236796j), (0.13119397062971452 - 1.1275887015236796j))


def test_sum_1():
    select = 1
    res = main.select_func(select)
    assert res == 4

def test_show_number(monkeypatch):

    def mocked_show_number(num: int):
        print('Mocked func')
        return 2

    def mocked_show_number_2(num: int):
        print('Mocked func')
        return 2

    monkeypatch.setattr(sys.modules[__name__], 'show_number', mocked_show_number, mocked_show_number_2)
    assert main.select_func(1) == 4