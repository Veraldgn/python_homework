# Task 3
# решение через список
month = int(input('Введите № месяца от 1 до 12: '))
seasons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето',
           'осень', 'осень', 'осень', 'зима']
print(seasons[month - 1])
# Кортеж
# month = int(input('Введите № месяца от 1 до 12: '))
# seasons = ('зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето',
#            'осень', 'осень', 'осень', 'зима')
# print(seasons[month - 1])

# решение через словарь
# month = int(input('Введите № месяца от 1 до 12: '))
# seasons = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна',
#            6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень',
#            11: 'осень', 12: 'зима'}
# print(seasons.get(month))
