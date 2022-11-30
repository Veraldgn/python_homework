qu_i = int(input('Сколько товаров вы хотите добавить?: '))
store = []
analytics = {'название': [], 'цена': [], 'количество': [], 'единица': []}
for i in range(1, qu_i + 1):
    store.append((i, {'название': input('Название?: '),
                      'цена': float(input('Цена?: ')),
                      'количество': int(input('Количество?: ')),
                      'единица': input('Ед.?: ')}))
for prod in store:
    for param in prod[1].keys():
        analytics[param].append(prod[1].get(param))
print(store)
print(analytics)
