import random
print("Wizard duel")
min_hp = 0
max_hp = 100
player_hp = computer_hp = max_hp
round_number = 1
computer_select = player_select = 0

spells = [["Uchilkaa", 20, 0], ["Hattabich", 0, 20], ["IT_school", 5, 10], ["DeBug    ", 5, -5], ["AI       ", 12, 8]]
name = 0
damage = 1
heal = 2

print("         Spells    Damage Healing")
i = 1
for row in spells:
    print(f'\n{i}', end=' - ')
    i += 1
    for elem in row:
        print('\t', elem, end='')
print("Start game")
while player_hp > min_hp and computer_hp > min_hp:
    print(f"Round №{round_number}")
    round_number += 1
    select = True
    while select:
        player_select = input('Put your spells')
        if player_select in ['1', '2', '3', '4', '5']:
            player_select = int(player_select) - 1
            computer_select = random.randint(0, 4)
            select = False
        else:
            print("Incorrect input")
    play1 = spells[player_select][name]
    play2 = spells[computer_select][name]
    player_hp -= spells[computer_select][damage]
    player_hp += spells[player_select][heal]
    computer_hp -= spells[player_select][damage]
    computer_hp += spells[computer_select][heal]

    if player_select == 2 and computer_select == 0:
        computer_hp -= 10
    elif player_select == 0 and computer_select == 2:
        player_hp -= 10
    elif player_select == 3 and computer_select == 4:
        computer_hp -= 25
        player_hp += 25
    elif player_select == 4 and computer_select == 3:
        computer_hp += 25
        player_hp -= 25
    if player_hp > max_hp:
        player_hp = max_hp
    if computer_hp > max_hp:
        computer_hp = max_hp
    print(f'Player: {play1}\nPlayer health: {player_hp}')
    print(f'Computer: {play2}\nComputer health: {computer_hp}')
