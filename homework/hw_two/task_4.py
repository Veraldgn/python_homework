# Task 4
text = input("Введите строку с пробелами: ").split()
for num, elem in enumerate(text, 1):
    if len(elem) > 10:
        print(num, elem[:10])
    else:
        print(num, elem)
