lista = []
for i in range(10):
    x = int(input(f"Podaj liczbę {i+1}: "))
    lista.append(x)
max = lista[0]
for j in lista:
    if j > max:
        max = j
print(max)

#         [Start]
#            |
#         [Inicjuj a = []]        
#            |
#         [i = 0]
#            |
#         [Czy i <= 10?] - "1"
#         /            |_____________
#      Tak                           |
#      |                            Nie
# [Wczytaj x do a[i]]                |
#    |                              [j = 0]
# [i += 1]                           |
#     |                             [max = a[j]] 
# [Powrót do "1"]                    | 
#                                   [Czy j <= 10?] - "2"
#                                  /                     \
#                                 /                       Nie
#                               Tak                        |   
#                                |                      [Wypisz max]
#                   [Czy max < a[j]?]                       |
#                  /                 \                  [Koniec]
#                Tak                  Nie
#                 |                    | 
#              [max=a[j]]            [Powrót do "2"]
#                 |
#              [j + 1] 
#                 |
#             [Powrót do "2"]
#