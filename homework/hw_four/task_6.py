""" Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите
внимание, что создаваемый цикл не должен быть бесконечным. Необходимо
предусмотреть условие его завершения. Например, в первом задании выводим целые
числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение
элементов списка будет прекращено."""

from itertools import count
from itertools import cycle

print('итератор, генерирующий целые числа, начиная с указанного')
for el in count(3):
    if el > 15:
        break
    else:
        print(el)

print('итератор, повторяющий элементы списка, определенного заранее')
lst = ['ABC', 1, 4]
i = 0
for elem in cycle(lst):
    if i > 10:
        break
    else:
        print(elem)
    i += 1
