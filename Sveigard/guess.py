# Это игра по угадыванию чисел
import  random

myName = str(input("Привет! Как тебя зовут?\n"))
attempts = int(input(f"Введите количество попыток, {myName}:\n"))
min_numb = int(input(f"Введите минимальное число, {myName}:\n"))
max_numb = int(input(f"Введите максимальное число, {myName}:\n"))

number = random.randint(min_numb, max_numb)
print(f"Что ж, {myName}, я загадываю число от {min_numb} до {max_numb}. У тебя {attempts} попытки.")

for i in range(attempts):
    guess = int(input("Попробуй угадать\n"))

    if guess < number:
        print("Твое число слишком маленькое")
    elif guess > number:
        print("Твое число слишком большое")
    else:
        break

if guess == number:
    guessesTaken = i + 1
    print(f"Отлино, {myName}! Ты справился за {guessesTaken} попытки!")

else:
    print(f"Увы я загадано число {number}.")