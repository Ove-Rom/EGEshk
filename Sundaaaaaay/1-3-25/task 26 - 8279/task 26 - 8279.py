with open("26_8279.txt") as f:
    t, n, m = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

base = []

for i in range(len(data)):  # выкидываем тех, кто ИМХО не сможет закупиться
    if data[i][-1] < m: base.append(data[i])

for time in range(t, 1440, t):  # время тикает
    visitors = []
    for j in base:  # смотрим очередь
        if j[0] <= time <= j[1] and j[2] < m:
            visitors.append(j)  # челики заходят в магазин
    if visitors:  # если в магазине есть покупатели
        visitors = sorted(visitors, key=lambda x: (x[2], -x[1]))
        guy = visitors[0]
        #   сортируем челов. 0 guy будет покупать
        base.remove(guy)  # чел вышел из очереди
        if len(guy) == 3:  # если чел ещё не покупал товар
            guy.append(1)  # количество купленных за сегодня +1
            guy[-2] += 1  # количество купленных всего +1
        elif len(guy) == 4:  # и если ещё не покупал
            guy[-1] += 1
            guy[-2] += 1
        base.append(guy)

base = sorted([i for i in base if len(i) == 4], key=lambda x: -x[-1])
# смотрим, кто купил больше всего товаров за сегодня
print(base[0][1] - base[0][0] + 1, base[0][-1])
