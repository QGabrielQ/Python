import math

def find_hypotenuse(catheus1,catheus2):
    """"The function computes a hypotenuse of a triangle
    based on the given two catheti"""
    hypotenuse = math.sqrt(catheus1**2 + catheus2**2)
    return hypotenuse
def findAngles(a,b,c):
    KątAB = 90 #Kąt miedzy przyprostokątnymi
    KątBC = (90*7)/12 
    KątAC = (5/7)*KątBC
    print(KątAB,KątAC,KątBC)

def main():
    a = 3
    b = 4
    c = find_hypotenuse(a,b)
    print(a,b,c)
    findAngles(a,b,c)
if __name__ == "__main__":
    main()
