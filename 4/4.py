"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
"""




def my_func(x, y):
    bedingung = 1
    result = 1 / x
    while bedingung < abs(y):
        result = result * (1 / x)
        bedingung += 1
    return result

print(my_func(float(input("Введите действительное число: ")), int(input("Введите отрицательное число: "))))