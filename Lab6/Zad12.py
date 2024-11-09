import numpy as np
import os
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
            pass
        elif(Labirynt[PlayerY+1][PlayerX]==3):
         Exit = True
        else:
         Labirynt[PlayerY+1][PlayerX] = 2
         Labirynt[PlayerY][PlayerX] =  0
         os.system('cls' if os.name == 'nt' else 'clear')
         RysujLabirynt(macierz)
         
    if(ruch=="w"):
        if(Labirynt[PlayerY-1][PlayerX]==1):
            pass
        else:
         Labirynt[PlayerY-1][PlayerX] = 2
         Labirynt[PlayerY][PlayerX] =  0
         os.system('cls' if os.name == 'nt' else 'clear')
         RysujLabirynt()

    if(ruch=="a"):
        if(Labirynt[PlayerY][PlayerX-1]==1):
            pass
        else:
         Labirynt[PlayerY][PlayerX-1] = 2
         Labirynt[PlayerY][PlayerX] =  0
         os.system('cls' if os.name == 'nt' else 'clear')
         RysujLabirynt(macierz)

    if(ruch=="d"):
        if(Labirynt[PlayerY][PlayerX+1]==1):
            pass
        else:
         Labirynt[PlayerY][PlayerX+1] = 2
         Labirynt[PlayerY][PlayerX] =  0
         os.system('cls' if os.name == 'nt' else 'clear')
         RysujLabirynt(macierz)

def  gra(macierz, n):
 RysujLabirynt(Labirynt," ","#","o","x")

      
    
         
Labirynt = np.array([
    [1,1,1,1,1,1,1],
    [1,2,1,0,0,0,1],
    [1,0,1,0,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,1,3,1],
    [1,1,1,1,1,1,1]
    ])
