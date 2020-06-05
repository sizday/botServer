import random
print("*КМН*")
print("Камень = к\nБумага = б\nНожницы = н")
player_score = 0
player_choice = ""
computer_score = 0
computer_choice = ""
number_round = 1
print("Game start!")

while player_score < 3 and computer_score < 3:
    print(f"Round №{number_round}")
    number_round += 1
    computer_choice = random.choice("кбн")
    while True:
        player_choice = input("Твой выбор")
        if player_choice in ["к", "б", "н"]:
            break
        else:
            print("Некорректный ввод")
    print(f"Выбор компьютера = {computer_choice}")

    if player_choice == "к" and computer_choice == "б":
        computer_score += 1
    elif player_choice == "б" and computer_choice == "к":
        player_score += 1
    elif player_choice == "н" and computer_choice == "б":
        player_score += 1
    elif player_choice == "б" and computer_choice == "н":
        computer_score += 1
    elif player_choice == "н" and computer_choice == "к":
        computer_score += 1
    elif player_choice == "к" and computer_choice == "н":
        player_score += 1
    else:
        print("Ничья")

    print(f"Текущий счёт {player_score}:{computer_score}")
print("Игра закончилась")
if player_score > computer_score:
    print("Вы выиграли!")
else:
    print("Вы проиграли :(")

