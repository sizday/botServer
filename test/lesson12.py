import random

min_health = 0
max_health = 100
computer_health = player_health = max_health
spells = [["COVID-19", 20, 0], ["DYRKA  ", 0, 20], ["DEPUTATE", 12, 8], ["ISOLATION", 7, 13], ["GRECHKA", 6, 6]]
name = 0
damage = 1
health = 2
print("My play")
i = 1
for row in spells:
    print(f"\n{[i ]}", end=' -')
    i += 1
    for elem in row:
        print('\t', elem, end='')
while True:
    select = input('Вы хотите сыграть?(yes/no)')
    if select == 'no':
        exit(0)
    elif select != 'yes':
        print('Error')
    else:
        print('Новая игра')
        for round in range(1, 5):
            choice = True
            player_select = 0
            computer_select = 0
            while choice:
                player_select = input('Введи способность от 1 до 5')
                if '0' < player_select < '6':
                    player_select = int(player_select) - 1
                    computer_select = random.randint(0, 4)
                    choice = False
                else:
                    print("Error")
            print(f"Round №{round}")
            play1 = spells[player_select][name]
            play2 = spells[computer_select][name]

            player_health += spells[player_select][health]
            player_health -= spells[computer_select][damage]
            computer_health += spells[computer_select][health]
            computer_health -= spells[player_select][damage]

            if player_health > max_health:
                player_health = max_health
            if computer_health > max_health:
                computer_health = max_health
            print(f'Игрок сыграл {play1}')
            print(f'Компьютер сыграл {play2}')
            print(f'У игрока {player_health} здоровья')
            print(f'У компьютера {computer_health} здоровья')
            if player_health < min_health or computer_health < min_health:
                break
        print("Game over")
        if player_health > computer_health:
            print("Поздравляю! Ты выиграл!")
        elif computer_health > player_health:
            print("Хфхфхфх! Я победил!")
        else:
            print("Ничья!")
