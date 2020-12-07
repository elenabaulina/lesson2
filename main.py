gifts = [1, 5.6, 1984, 'iphone', -2]
for index in range(len(gifts)):
    print(type(gifts[index]))

at = input("Введите что-нибудь : ")
r = list(at)
o = 0
for i in range(int(len(r) / 2)):
    r[o], r[o + 1] = r[o + 1], r[o]
    o += 2
print("Смотрите, элементы поменялись друг с другом: ", (r))

seasons = ["Зима", "Весна", "Лето", "Осень"]
month = int(input("Введите номер месяца : "))
a, b, c = [12, 1, 2]
d, e, f = [3, 4, 5]
g, h, y = [6, 7, 8]
o, p, r = [9, 10, 11]
if month == a or month == b or month == c:
    print("Время года : ", seasons[0])
elif month == d or month == e or month == f:
    print("Время года : ", seasons[1])
elif month == g or month == h or month == y:
    print("Время года : ", seasons[2])
elif month == o or month == p or month == r:
    print("Время года : ", seasons[3])
else:
    print("Вы ввели несуществующий номер месяца")

seasons = dict(winter='Зима', spring='Весна', summer='Лето', autumn='Осень')
month = int(input("Введите номер месяца : "))
a, b, c = [12, 1, 2]
d, e, f = [3, 4, 5]
g, h, t = [6, 7, 8]
o, p, r = [9, 10, 11]
if month == a or month == b or month == c:
    print("Время года : ", seasons.get('winter'))
elif month == d or month == e or month == f:
    print("Время года : ", seasons.get('spring'))
elif month == g or month == h or month == t:
    print("Время года : ", seasons.get('summer'))
elif month == o or month == p or month == r:
    print("Время года : ", seasons.get('autumn'))
else:
    print("Вы ввели несуществующий номер месяца")

lists = input("Напишите предложение: ")
lists = lists.split()
i = 0
for list in lists:
    i += 1
    print(i, list[0:10])
