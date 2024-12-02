def bubblesort_max(Lista):
    for i in range(len(Lista)-1):
        for j in range(len(Lista)-i-1):
            if Lista[j] > Lista[j+1]:
                temp = Lista[j]
                Lista[j] = Lista[j+1]
                Lista[j+1] = temp
def bubblesort_min(Lista):
    for i in range(len(Lista)-1):
        for j in range(len(Lista)-i-1):
            if Lista[j] < Lista[j+1]:
                temp = Lista[j]
                Lista[j] = Lista[j+1]
                Lista[j+1] = temp
#                       [Strart bubblesort_min(Lista)]
#                                     |
#                               [Wczytaj Lista]
#                                     |
#                                  [i = 0]
#                                     |
#                           [Czy i <= len(Lista)-1?] - "1"
#                          /                             \
#                        Tak                             Nie
#                         |                               |
#                      [j = 0]                          [Koniec]
#                         |
#             [Czy j <= len(Lista)-i-1?] - "2"
#            /                            \
#          Tak                             Nie
#           |                                \
#  [Czy Lista[j]<Lista[j+1]?]               [i+1]
#     |                      \                |
#    Tak                     Nie            [Powrót do "1"]
#     |                         \
#   [temp = Lista[j]]         [j+1]
#     |                           \
#   [Lista[j] = Lista[j+1]]     [Powrót do "2"]
#      |
#   [Lista[j+1] = temp]
#      |
#    [j+1]
#      |
#  [Powrót do "2"]
#
#
#

Lista=[6,2,7,1,5]
bubblesort_max(Lista)
print(Lista)
bubblesort_min(Lista)
print(Lista)
