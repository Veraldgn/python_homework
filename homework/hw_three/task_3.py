"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func(*args):
    return sum(sorted(args)[1:])


print(my_func(int(input('Первое число: ')),
              int(input('Второе число: ')),
              int(input('Третье число: '))))
