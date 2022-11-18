import sys

import pytest
import main
import func
import func2
from func import add


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

