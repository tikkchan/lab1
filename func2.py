def exponent(num, power):
    '''возведение числа в степень'''
    exponent = num ** power
    print(exponent)
    return exponent


def sqrt(num):
    '''квадратный корень'''
    if num >= 0:
        sqrt = num ** 0.5
        print(sqrt)
        return sqrt
    else:
        print("Только рациональные числа")
        return "Только рациональные числа"


def cbrt(num):
    '''кубический корень'''
    if num < 0:
        num = abs(num)
        cbrt = -1 * (num ** (1 / 3))
    else:
        cbrt = num ** (1 / 3)
    print(cbrt)
    return cbrt


def recurse_factor(n):
    # recursive function to find factorial
    if n == 1:
        return n
    else:
        return n * recurse_factor(n - 1)


def fact(num):
    '''факториал числа'''
    if num <= 0:
        print("Факториал не существует для отрицательных чисел" if num < 0 else 'Факториал 0 равен 1')
    else:
        print(recurse_factor(num))
        return recurse_factor(num)


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def dicho(f, a, b, eps=1.0e-14):  # Дихотомия
    fa = f(a)
    fb = f(b)
    while True:
        c = 0.5 * (a + b)
        if abs(b - a) < eps:
            return c
        fc = f(c)
        if abs(fc) <= eps:
            return c
        if sign(fa) * sign(fc) < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc


def div_poly(p, a):  # делим исходный полином на (x-a) и получаем квадратный
    r = [0, 0, 0]  # трехчлен, поставляющий два недостающих корня
    r[2] = p[3]
    r[1] = p[2] + a * p[3]
    r[0] = (p[1] + a * (p[2] + a * p[3]))
    return tuple(r)


def solve_qube(p):
    q = max(p)
    left = -abs(q) / abs(p[3])  # границы вещественного корня
    right = -left
    x1 = dicho(lambda x: p[3] * x ** 3 + p[2] * x ** 2 + p[1] * x + p[0], left, right)
    (c, b, a) = div_poly(p, x1)
    d = b ** 2 - 4 * a * c
    x2 = (-b + d ** 0.5) / (2 * a)
    x3 = (-b - d ** 0.5) / (2 * a)
    return (x1, x2, x3)


def solve_qube2(a1, b1, c1, d1):
    print(solve_qube([a1, b1, c1, d1]))
    return (solve_qube([a1, b1, c1, d1]))
