for i in range(0,11):
    if(i%2==0):
        print(i,"-parzysta")
    else:
        print(i,"-nieparzysta")

#              [Start]
#                 |
#           [Inicjalizuj i = 0]
#                 |
#         [Czy i <= 10?]
#            /        \
#          Tak        Nie
#          |           |
#      [Wypisz i]    [Koniec]
#          |
#        [Czy i % 2 == 0?]
#          /              \
#        Tak               Nie
#         |                 |
#  [Wypisz "Parzysta"]     [Wypisz "Nieparzysta"]
#         |
#      [i + 1]
#         |
#  [Powrót do "Czy i <= 10?"]
