# Task 5
revenue = int(input('Введите значение выручки:'))
costs = int(input('Введите значение издержек:'))
if revenue > costs:
    print('Финансовый результат фирмы: прибыль')
    profit = revenue - costs
    print(f'Рентабельность выручки:{round(profit / revenue * 100)}%')
    number_com = int(input('Введите численность сотрудников фирмы:'))
    print(f'Прибыль в расчете на сотрудника:{round(profit / number_com, 2)}')
else:
    print('Финансовый результат фирмы: убыток')
