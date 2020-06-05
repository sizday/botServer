import random
min_health = 0
max_health = 100
player_health = max_health
comp_health = max_health
spells = [["COVID-19", 20, 0], ["DYRKA", 0, 20], ["CRISIS", 12, 8], ["GRECHKA", 6, 6]]
name = 0
damage = 1
health = 2
print("ЧЁ Та ЗА ИГРА")
print("Имя        Урон   Здоровье")
for i in range(len(spells)):
    print(f"{spells[i][name]}    {spells[i][damage]}    {spells[i][health]}")
while True:
    select = input("Попробовать снова? (да, нет)")
    if select == "нет":
        exit(0)
    elif select != "да":
        print("Error")
    else:
        print("Игра началась")
        for i in range(5):
            print(f"Раунд №{i+1}")
            choice = True
            player_select = 0
            comp_select = 0
            while choice:
                player_select = input("Выберите способность: ")
                if "0" < player_select < "5":
                    player_select = int(player_select)-1
                    comp_select = random.randint(0, 3)
                    choice = False
                else:
                    print("Некорректный ввод")

            play1 = spells[player_select][name]
            play2 = spells[comp_select][name]
            player_health += spells[player_select][health]
            player_health -= spells[comp_select][damage]
            comp_health += spells[comp_select][health]
            comp_health -= spells[player_select][damage]
            if player_select == 3 and comp_select == 0:
                comp_health = 0
            elif player_select == 0 and comp_select == 3:
                player_health = 0
            if player_health > max_health:
                player_health = max_health
            if comp_health > max_health:
                comp_health = max_health
            print(f"Игрок: {play1}\nКомпьютер: {play2}\n"
                  f"Здоровье игрока: {player_health}\nЗдоровье компьютера: {comp_health}")
            if player_health <= min_health or comp_health <= min_health:
                break

    print("Game Over")
    if player_health > comp_health:
        print("Поздравляю ты выиграл")
    elif player_health < comp_health:
        print("Поздравляю ты чучмек")
    else:
        print("Ничья")
