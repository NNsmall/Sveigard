import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('Сколько будет: ' + str(number1) + ' + ' + str(number2) + '?')
answer = int(input())
if answer == int(number1) + int(number2):
    print('Верно!')
else:
    print('Нет! Правильный ответ - ' + str(number1 + number2))