"""Программа принимает действительное положительное число x и целое
отрицательное число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции
возведения числа в степень."""


def my_func(x, y):
    return x ** y


def my_func_2(x, y):
    result = 1
    for i in range(y, 0):
        result *= x
    result = 1 / result
    return result


print(my_func(int(input('Действительное положительное число: ')),
              int(input('Целое отрицательное число для степени: '))))

print(my_func_2(int(input('Действительное положительное число: ')),
                int(input('Целое отрицательное число для степени: '))))