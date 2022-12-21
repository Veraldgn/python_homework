"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv

script_name, hours_product, rate_hour, bonus = argv

print('Имя скрипта: ', script_name)
print('Выработка в часах: ', hours_product)
print('Ставка в час: ', rate_hour)
print('Премия: ', bonus)
print('Зарплата: ', int(hours_product) * int(rate_hour) + int(bonus))
