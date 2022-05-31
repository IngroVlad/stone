import random


user = input("Сделайте выбор - камень, ножницы, бумага:")
possibe = "камень", "ножницы", "бумага"
computer = random.choice(possibe) #Случайный выбор из переменной "possibe"


if user == computer:
    print("Оба пользователя выбрали: ", user, "Ничья!")

elif user == "камень":
    if computer == "ножницы":
        print("Камень бьет ножницы. Вы победили!")
    else:
        print("Бумага обарачивает камень! Вы проиграли")
elif user == "бумага":
    if computer == "камень":
        print("Бумага обарачивает камень! Вы выйграли!")
    else: 
        print("Вы проиграли!")
elif user == "ножницы":
    if computer  == "бумага":
        print("Ножницы режут бумагу, Вы победили!")
    else:
        print("Вы проиграли!")
elif user == "ножницы":
    if computer  == "бумага":
        print("Ножницы режут бумагу, Вы победили!")
    else:
        print("Ножницы режут бумагу! Вы проиграли!")