import random

secretNumber = random.randint(1, 20)
print('Задумано число от 1 до 20.Угадай его.')
for gussesTaken in range(1, 7):
    print('Ваш вариант:')
    guess = int(input())
    if guess < secretNumber:
        print('Число меньше задуманного')
    elif guess > secretNumber:
        print('Число больше задуманного')
    else:
        break
if guess == secretNumber:
    print('Верно.Количество попыток: ' + str(gussesTaken))
else:
    print("Нет.Задумано число " + str(secretNumber))
