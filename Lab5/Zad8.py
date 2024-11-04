from random import seed
from random import randint
seed(123)
randomnumber = randint(0,100)
print("Wylosowano liczbe!")
guess = False
while (guess == False):
    x = int(input("Podaj twoją odpowiedz: "))
    if (x < randomnumber):
        print("Liczba jest wieksza od podanej!")
    if (x > randomnumber):
        print('liczba jest mniejsza od podanej')
    if(x == randomnumber):
        guess = True
        print("Wygrałeś!")
print(randomnumber)

