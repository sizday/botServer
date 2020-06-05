import random
count_stats = 5
stats = [random.randint(40, 71) for i in range(count_stats)]
names = ["Сила", "Ум", "Ловкость", "Карантин", "Дистанционка"]
for i in range(count_stats):
    print(f"{i+1}) {names[i]} = {stats[i]}")
select = int(input("Какую Характеристику Вы Хотите Изменить?"))
select -= 1
stats[select] += random.randint(10, 15)
for i in range(count_stats):
    if i == select:
        continue
    stats[i] -= random.randint(1, 5)
print("Новые характеристики")
for i in range(count_stats):
    print(f"{i+1}) {names[i]} = {stats[i]}")
