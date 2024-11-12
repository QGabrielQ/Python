import math
def Współliniowe(P1,P2,P3):
    Lewa = (P2[0]-P1[0])*(P3[1]-P1[1])
    Prawa = (P2[1]-P1[1])*(P3[0]-P1[0])
    if (Lewa == Prawa):
        return 1
    else:
        return 0


def obwodtrojkata(P1,P2,P3):
    if(Współliniowe(P1,P2,P3) == 0):
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
    else:
        print("Punkty leżą na jednej lini!!!!")
        return 0
    
    
P1 = [4,0]
P2 = [0,3]
P3 = [0,0]
print(obwodtrojkata(P1,P2,P3))