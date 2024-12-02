def NWD(a,b):
    while b != 0:
        a, b=b, a %b
    return a
#       [Start NWD(a,b)]
#            |
#       [Wczytaj a i b]
#            |
#       [Czy b == 0?] - "1"
#      /             \
#    Tak              Nie
#     |                |
# [Return a]         [a,b = b,a%b]
#                       |
#                   [Powrót do "1"]

def NWDRek(a,b):
    if(b == 0):
        return a
    else:
        return NWDRek(b,a%b)
#                     [Start NWD(a,b)]
#                        |
#                     [Wczytaj a i b]
#                         |
#                     [Czy b == 0?]
#                    /            \
#                  Tak             Nie
#                   |               |
#                [Return a]       [Wywołaj NWD(b,a%b)]
#                                   |
#                                 [Koniec]
print(NWD(12,18))
print(NWDRek(12,18))

