# Task 2
time = int(input('Введите время в секундах:'))
hour = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60
print(f'{hour:02}:{minutes:02}:{seconds:02}')