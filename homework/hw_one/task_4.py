# Task 4
number = int(input('Введите целое положительное число:'))
big_num = 0
while number > 0:
    new_num = number % 10
    if new_num > big_num:
        big_num = new_num
    number //= 10
print(f'Самая большая цифра в числе:{big_num}')
