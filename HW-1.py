#Тип змінної str - стрічка
fruite = "apple"

#Тип змінної int - ціле число
amount = 10

#Тип змінної float - дробове число
weight = 1.25

#Тип змінної bool - логічне значення, True or False
expensive = True


# Програма "Вгадай число"
# В цій грі приймають участь дві людини
# Перший гравець обирає таємне число і вводить в програму
# Другий гравець старається вгадати це число з 10 спроб
# Якщо це йому вдається - він виграв, інакше він програв

player1 = int(input("Введіть таємне число від 1 до 100:  "))
result = False
for i in range(10):
    player2 = int(input("Вгадайте таємне число = "))
    if player1 < player2:
        print("Число завелике")
    elif player1 > player2:
        print("Число замале")
    else:
        result = True
        break

if result == True:
    print("Ви виграли!!!")
else:
    print("Ви програли!!!")






#        

        