
from sys import base_exec_prefix


a = 4
b = 5
if a > 0 and b > 0:
    P = a * b
    print("Pole prostokąta wynosi: ", P)
else:
    print("Błedne dane")
    print("Boki prostokąta muszą byc dodatnie")