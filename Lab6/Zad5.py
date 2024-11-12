def pietro(znak):
    print(10*znak)
    print(3*znak+4*" "+3*znak)
    print(3*znak+4*" "+3*znak)
    print(10 * znak)
def dach(znak):
    spacje = 4
    dach = 2
    for i in range(0,5):
        print(spacje*" "+dach * znak)
        spacje -= 1
        dach += 2

dach("[")
pietro("#")
pietro("#")