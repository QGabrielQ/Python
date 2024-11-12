def RysujDomek(LPieter,Dach,Pietro): 
    lspacje = 4
    ldach = 2
    for i in range(0,5):
        print(lspacje*" "+ldach * Dach)
        lspacje -= 1
        ldach += 2
    for i in range(0,LPieter):
        print(10*Pietro)
        print(3*Pietro+4*" "+3*Pietro)
        print(3*Pietro+4*" "+3*Pietro)
        print(10 * Pietro)
    

RysujDomek(3,"^","#")