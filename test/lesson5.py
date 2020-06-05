import random
print("Угадай моё число")
min_border = int(input("Введите минимальную границу"))
max_border = int(input("Введите максимальную границу"))
m_number = random.randint(min_border, max_border)
user_number = 0
while user_number != m_number:
    user_number = input("Введите число")
    while not user_number.isdigit():
        user_number = input("Введите правильное число")
    user_number = int(user_number)
    if user_number < m_number:
        print("Моё число больше")
    else:
        print("Моё число меньше")
print("Поздравляю,ты угадал! Моё число = ", m_number)

