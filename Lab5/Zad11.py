import numpy as np
import os
Labirynt = np.array([
    [1,1,1,1,1,1,1],
    [1,2,1,0,0,0,1],
    [1,0,1,0,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,1,3,1],
    [1,1,1,1,1,1,1]
    ])
MoveCount = 20
Exit = False
while(Exit == False and MoveCount > 0):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Labirynt)
    PlayerX = int(np.where(Labirynt == 2)[1][0])
    PlayerY = int(np.where(Labirynt == 2)[0][0])
    print(f"Move count: {MoveCount}")
    print(f"Cords: {PlayerX} {PlayerY} ")
    move = str(input("Input move: "))
    if(move=="s"):
        if(Labirynt[PlayerY+1][PlayerX]==1):
            continue
        elif(Labirynt[PlayerY+1][PlayerX]==3):
         Exit = True
        else:
         Labirynt[PlayerY+1][PlayerX] = 2
         Labirynt[PlayerY][PlayerX] =  0
         MoveCount -= 1
    if(move=="w"):
        if(Labirynt[PlayerY-1][PlayerX]==1):
            continue
        else:
         Labirynt[PlayerY-1][PlayerX] = 2
         Labirynt[PlayerY][PlayerX] =  0
         MoveCount -= 1
    if(move=="a"):
        if(Labirynt[PlayerY][PlayerX-1]==1):
            continue
        else:
         Labirynt[PlayerY][PlayerX-1] = 2
         Labirynt[PlayerY][PlayerX] =  0
         MoveCount -= 1
    if(move=="d"):
        if(Labirynt[PlayerY][PlayerX+1]==1):
            continue
        else:
         Labirynt[PlayerY][PlayerX+1] = 2
         Labirynt[PlayerY][PlayerX] =  0
         MoveCount -= 1
    if(MoveCount == 0):
       print("Game Over! You ran out of moves!!!")
    if(Exit == True):
       print("You win!!!!")
    

