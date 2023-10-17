import time
import os
import random
import select
import sys

def BuildGrid():
    Grid = [[" " for _ in range(15)] for _ in range(15)]  
    for r in range(len(Grid)):
        for c in range(len(Grid)):
            if c ==0  or c ==14:
                if r != 0:
                    Grid[r][c] ="🧱"
            elif r ==0 or  r ==14:
                 Grid[r][c] ="_"
    return Grid


def DisplayGrid(grid):
   for i in grid:
       print(" ".join(i))

def move(grid,position,direction):
    snake ='⚉'
    if direction in ["a","A"]:
        grid[position[0]][position[1]] =' '
        position = [position[0],position[1]-1]
        grid[position[0]][position[1]] =snake
    
    elif direction in ["d","D"]:
        grid[position[0]][position[1]] =' '
        position = [position[0],position[1]+1]
        grid[position[0]][position[1]] =snake

    elif direction in ["W","w"]:
        grid[position[0]][position[1]] =' '
        position = [position[0]-1,position[1]]
        grid[position[0]][position[1]] =snake

    elif direction in ["s","S"]:
        grid[position[0]][position[1]] =' '
        position = [position[0]+1,position[1]]
        grid[position[0]][position[1]] =snake

    return grid,position,direction 


#def AddFruits


Grid = BuildGrid()

position = [6,6]
Grid[6][6] ='⚉'
moves ="a"


menu = """\n[A]- Move LEFT.
[D] -Move RIGHT.
[W] -Move UP.
[S] -Move DOWN. \n
[X] -EXIT.
[Z] -RESTART.
"""


counter =0
count= 0
while True:
    count+=1
    os.system('clear')
    print("\n           SNAKEY ")
    DisplayGrid(Grid)
    print(menu)
    #time.sleep(1)

    rlist, _, _ = select.select([sys.stdin], [], [], 1)

    if rlist:
        # User provided input
        moves = input()
        if moves == 'x' or moves =="X":
            print("Game Exited")
            break

        elif moves == 'Z' or moves =='z':
            print("Restart")
            Grid = BuildGrid()
            position = [6,6]
            Grid[6][6] ='⚉'
            continue

        elif moves in list("wads")or moves in list("WADS"):
            if position[0] >1 and position[1] <14 and position[0] <14 and position[1] >1:
                Grid,position,moves = move(Grid,position,moves)

    else:
        if position[0] >1 and position[1] <14 and position[0] <14 and position[1] >1:
            Grid,position,moves = move(Grid,position,moves)
        else:
            print("Crashed!!")
            restart = input()
            if restart in ['x','X']:
                break
            elif restart in ['Z' or 'z']:
                print("Restart")
            Grid = BuildGrid()
            position = [6,6]
            Grid[6][6] ='⚉'
            moves ="a"
            continue


    

