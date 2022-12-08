# Task 2
"""Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""


def user_data(name, lastname, birth_year, city, e_mail, phone):
    return print(f'{name}, {lastname}, {birth_year} года рождения, '
                 f'из города {city}, {e_mail}, {phone}')


user_data(name=input('Имя: '), lastname=input('Фамилия: '),
          birth_year=int(input('Год рождения: ')), city=input('Город: '),
          e_mail=input('E-mail: '), phone=int(input('Номер телефона: ')))
