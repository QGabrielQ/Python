import numpy as np
import os
puste = " "
sciana = "#"
ludzik = "o"
drzwi = "x"
def RysujLabirynt(macierz, puste, sciana, ludzik, drzwi):
   for i in macierz:
      print("\n",end="")
      for j in i:
        if(j == 1):
            print(sciana,sep="",end="")
        if(j == 0):
           print(puste,sep="",end="")
        if(j == 2):
           print(ludzik,sep="",end="")
        if(j==3):
           print(drzwi,sep="",end="")

def aktualizujLabirynt(macierz, ruch):
    PlayerX = int(np.where(Labirynt == 2)[1][0])
    PlayerY = int(np.where(Labirynt == 2)[0][0])
    if(ruch=="s"):
        if(Labirynt[PlayerY+1][PlayerX]==1):
            os.system('cls' if os.name == 'nt' else 'clear')
            RysujLabirynt(macierz, puste, sciana, ludzik, drzwi)
        elif(Labirynt[PlayerY+1][PlayerX]==3):
         print("YOU WIN!!!!!!")
         exit()
        else:
         Labirynt[PlayerY+1][PlayerX] = 2
         Labirynt[PlayerY][PlayerX] =  0
         os.system('cls' if os.name == 'nt' else 'clear')
         RysujLabirynt(macierz, puste, sciana, ludzik, drzwi)
         
    if(ruch=="w"):
        if(Labirynt[PlayerY-1][PlayerX]==1):
            os.system('cls' if os.name == 'nt' else 'clear')
            RysujLabirynt(macierz, puste, sciana, ludzik, drzwi)
        elif(Labirynt[PlayerY-1][PlayerX]==3):
         print("YOU WIN!!!!!!")
         exit()
        else:
         Labirynt[PlayerY-1][PlayerX] = 2
         Labirynt[PlayerY][PlayerX] =  0
         os.system('cls' if os.name == 'nt' else 'clear')
         RysujLabirynt(macierz, puste, sciana, ludzik, drzwi)

    if(ruch=="a"):
        if(Labirynt[PlayerY][PlayerX-1]==1):
            os.system('cls' if os.name == 'nt' else 'clear')
            RysujLabirynt(macierz, puste, sciana, ludzik, drzwi)
        elif(Labirynt[PlayerY][PlayerX-1]==3):
         print("YOU WIN!!!!!!")
         exit()
        else:
         Labirynt[PlayerY][PlayerX-1] = 2
         Labirynt[PlayerY][PlayerX] =  0
         os.system('cls' if os.name == 'nt' else 'clear')
         RysujLabirynt(macierz, puste, sciana, ludzik, drzwi)

    if(ruch=="d"):
        if(Labirynt[PlayerY][PlayerX+1]==1):
            os.system('cls' if os.name == 'nt' else 'clear')
            RysujLabirynt(macierz, puste, sciana, ludzik, drzwi)
        elif(Labirynt[PlayerY][PlayerX+1]==3):
         print("YOU WIN!!!!!!")
         exit()
        else:
         Labirynt[PlayerY][PlayerX+1] = 2
         Labirynt[PlayerY][PlayerX] =  0
         os.system('cls' if os.name == 'nt' else 'clear')
         RysujLabirynt(macierz, puste, sciana, ludzik, drzwi)

def  gra(macierz, n):
 RysujLabirynt(Labirynt," ","#","o","x")
 while n > 0:
    print("\n")
    ruch = str(input("Podaj ruch: "))
    aktualizujLabirynt(macierz,ruch)
    n -= 1
    if(n == 0):
        print("\n You ran out of moves!!!!")

      
    
         
Labirynt = np.array([
    [1,1,1,1,1,1,1],
    [1,2,1,0,0,0,1],
    [1,0,1,0,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,1,3,1],
    [1,1,1,1,1,1,1]
    ])
gra(Labirynt,20)