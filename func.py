def add(num1, num2):
    '''сложение двух чисел'''
    sumn = num1 + num2
    print(sumn)
    return sumn

def subtract(num1, num2):
    '''вычитание двух чисел'''
    minn = num1 - num2
    print(minn)
    return minn

def multiply(num1, num2):
    '''умножение двух чисел'''
    umn = num1 * num2
    print(umn)
    return umn

def divide(num1, num2):
    '''деление двух чисел'''
    try:
        delenie = num1 / num2
        print(delenie)
        return delenie
    except ZeroDivisionError as e:
        print(e)

''' def NTW(n=-1):
    if(n==-1):
        n = int(input("Введите число, которое вы хотите прочитать: "))
    units = ["", "Один", "Два", "Три", "Четыре",
            "Пять", "Шесть", "Семь", "Восемь", "Девять", "Десять", "Одиннадцать", "Двенадцать",
            "Тринадцать", "Четырнадцать", "Пятнадцать", "Шестнадцать", "Семнадцать",
            "Восемнадцать", "Девятнадцать" ]
    tens = ["","","Двадцать","Тридцать","Сорок","Пятьдесят","Шестьдесят","Семьдесят","Восемдесят","Девяностно"]
    if (n < 20):
        return units[n]
    if (n < 100):
        return tens[n//10]+(" " if (n % 10 != 0) else "")+units[n % 10]
    if (n < 1000):
        return units[n//100]+" Сто"+(" " if (n%100!= 0) else "")+NTW(n % 100)
    if (n < 100000):
        return NTW(n//1000) +" Тысяча"+(" " if (n % 10000 != 0) else "")+NTW(n % 1000)
    if (n < 10000000):
        return NTW(n//100000)+" Сто тысяч"+(" " if (n % 100000 != 0) else "")+NTW(n % 100000)
    return NTW(n//10000000)+" Десять миллионов"+(" " if (n % 10000000 != 0) else "")+NTW(n % 10000000) '''