def rectangle_area(a,b):
    if((a <= 0) or (b <= 0)):
        print("Nie prawidłowe liczby!!")
    else:
        return a*b
print(rectangle_area(10,12))
#         [Start funkcji]
#                |
#      [Czy a <= 0 lub b <= 0?]
#          /           \
#        Tak            Nie
#         |               |
# [Zwróć komunikat]   [Oblicz a * b]
#         |               |
#     [Koniec]        [Zwróć wynik]
#                          |
#                     [Koniec funkcji]
#        [Start]
#           |
#      [Wprowadź a]
#           |
#      [Wprowadź b]
#           |
#  [Wywołaj rectangle_area(a, b)]
#           |
#      [Zwróć wynik]
#           |
#      [Wyświetl wynik]
#           |
#        [Koniec]
