import random
print('Привет! Я - программа, которая поможет тебе натренировать твой spelling. Я загадываю слово, перемешиваю в нем все буквы и говорю его тебе - твоя задача угадать, что за слово я загадала и записать его правильно. Надеюсь, тебе все понятно, давай начнем!\n')
word_array = ['cheque', 'withdraw', 'geography', 'clothes', 'employer', 'achievable', 'harass', 'success']
words_for_support = ['Не расстраивайся, попробуй еще!','Сейчас все обязательно получится!','Ты чудо, не переживай!','Do not worry, be happy!','У тебя все получится, если попробуешь еще раз','Отдохни и попробуй еще разок', 'Не грусти, а то накоп не будет расти!','Соберись и давай еще разок, ладно?']


def spelling_train(rigth_v1, answer):
  while answer != rigth_v1:
    print('Неверно\n')
    support = random.choice(words_for_support)
    print(support, '\n')
    right_v1 = random.choice(word_array)
    l = list(right_v1)
    random.shuffle(l)
    result = ''.join(l)
    print('Твоё слово: ', result, '\n')
    answer = input('Напиши слово правильно: \n')
  print('Good job! Thank you very much!!!')


right_word = random.choice(word_array)
l = list(right_word)
random.shuffle(l)
result = ''.join(l)
print('Твоё слово: ', result, '\n')
user_answer = input('Напиши слово правильно: \n')
spelling_train(right_word, user_answer)
