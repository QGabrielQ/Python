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
    
      
    
         
Labirynt = np.array([
    [1,1,1,1,1,1,1],
    [1,2,1,0,0,0,1],
    [1,0,1,0,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,1,3,1],
    [1,1,1,1,1,1,1]
    ])
RysujLabirynt(Labirynt," ","#","o","x")