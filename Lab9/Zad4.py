def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Przykładowe wywołanie funkcji
n = 6
print(fibonacci(n))


#        [Start funkcji fibonacci(n)]
#                  |
#         [Czy n <= 1?]
#             /      \
#           Tak       Nie
#           /           \
#   [Zwróć n]      [Wywołaj fibonacci(n-1) i fibonacci(n-2)]
#                       |
#                  [Zwróć fibonacci(n-1) + fibonacci(n-2)]
#                       |
#                  [Koniec funkcji]
#  [Start]
#     |
# [Wprowadź n]
#     |
# [Wywołaj fibonacci(n)]
#     |
# [Zwróć wynik]
#     |
#  [Koniec]