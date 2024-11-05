import math
def obwodtrojkata(P1,P2,P3):
    x1 = pow((P2[0]-P1[0]),2)
    y1 = pow((P2[1]-P1[1]),2)
    A = math.sqrt(x1+y1)
    x2 = pow((P1[0]-P3[0]),2)
    y2 = pow((P1[1]-P3[1]),2)
    B = math.sqrt(x2+y2)
    x3 = pow((P2[0]-P3[0]),2)
    y3 = pow((P2[1]-P3[1]),2)
    C = math.sqrt(x3+y3)
    return A + B + C
    
P1 = [7.5,-8]
P2 = [-2,0]
P3 = [7,12]
print(obwodtrojkata(P1,P2,P3))