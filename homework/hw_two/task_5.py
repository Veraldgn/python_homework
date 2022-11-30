# Task 5
rating = [7, 5, 3, 3, 2]
elem = int(input('Введите новый элемент рейтинга: '))
rating.append(elem)
rating.sort(reverse=True)
print(f'Новый рейтинг: {rating}')
