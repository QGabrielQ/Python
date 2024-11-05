import math
def odleglosc(P1,P2):
    x = pow((P2[0]-P1[0]),2)
    y = pow((P2[1]-P1[1]),2)
    distance = math.sqrt(x+y)
    return distance
P1 = [-1,-1]
P2 = [2,3]
print(odleglosc(P1,P2))