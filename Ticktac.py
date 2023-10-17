import os

def BuildGrid():
    Grid = [[" " for _ in range(15)] for _ in range(15)]  
    for r in range(len(Grid)):
        for c in range(len(Grid)):
            if c ==0 or c == 4 or c ==9 or c ==14:
                if r != 0:
                    Grid[r][c] ="|"
            elif r ==0 or r == 4 or r ==9 or r ==14:
                 Grid[r][c] ="_"
    return Grid

def Add_Nums(Grid):
    for r in range(len(Grid)):
        for c in range(len(Grid)):
            if r ==2 and c ==2:
                Grid[r][c] ="1"
            elif r ==2 and c ==6:
                Grid[r][c] ="2"
            elif r ==2 and c ==11:
                Grid[r][c] ="3"
            elif r ==6 and c ==2:
                Grid[r][c] ="4"
            elif r == 6 and c ==6:
                Grid[r][c] ="5"
            elif r == 6 and c ==11:
                Grid[r][c] ="6"
            elif r == 11 and c ==2:
                Grid[r][c] ="7"
            elif r ==11 and c ==6:
                Grid[r][c] ="8"
            elif r ==11 and c ==11:
                Grid[r][c] ="9"
                
    return Grid

def UpdateGrid(grid,num,player):
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] ==num:
                grid[r][c] =player

def DisplayGrid(grid):
   for i in grid:
       print(" ".join(i))
            
def checkWin(grid,player):
    ##DIGONALS:
    print()
    if player == grid[2][2] and player == grid[6][6] and player == grid[11][11]:
        print("Player "+player+" Wins!!")
        return True
    elif player == grid[6][2] and player == grid[6][6] and player == grid[11][12]:
        print("Player "+player+" Wins!!")
        return True
    
    #HORIZONTAL whatever!!
    for r in grid:
        if r.count(player) ==3:
            print("Player "+player+" Wins!!")
            return True
    #VERTICAL
    if player ==grid[2][2] and player == grid[6][2] and player==grid[11][2]:
            print("Player "+player+" Wins!!")
            return True
        
    if player == grid[2][6] and player == grid[6][6] and player and player ==grid[11][6]:
            print("Player "+player+" Wins!!")
            return True
        
    if player == grid[2][11] and player == grid[6][11] and player ==grid[11][11]:
            print("Player "+player+" Wins!!")
            return True


def restart(grid):
    grid =BuildGrid()
    grid = Add_Nums(grid)
    return grid

    
Grid = BuildGrid()
Grid = Add_Nums(Grid)
menu = """\n Menu: 
- To play Enter Block Number 
X.To Exit Game
Z.To Restart \n"""

PlayerTurn = True
Turns =9

#PLayer Mode [Computer Or 2player]:
modetxt = """*Enter Play mode:
1. To play Computer
2. To play your Friend """



PlayMode =bool()
mode = input(modetxt)
if mode == '1' :
    PlayMode =True
elif mode =='2':
    PlayMode = True


while PlayMode ==False:
    pass
    os.system('clear')
    DisplayGrid(Grid)
    #Check if player won
    if checkWin(Grid,"X") ==True or checkWin(Grid,"O"):
        print("Game Over!!")
        print("1.Enter Z to restart Game \n2.Enter X to exit")
    else:
        print(menu)


     #Check Turns
    if Turns ==0:
        os.system("clear")
        DisplayGrid(Grid)
        print("\nDRAW!!!!!!!!!!\n")
        print("1.Enter Z to restart Game \n2.Enter X to exit")
    #UserInput
    UserInput = input()

    if UserInput =="X" or UserInput =="x":
        print("Game Exited")
        break

    elif UserInput =="Z" or UserInput =="z":
        Grid = restart(Grid)
        Turns=9
        PlayerTurn = True
        continue

    # elif UserInput in [str(i) for i in range(1,10)]:
    #     UpdateGrid(Grid,UserInput,"X")



#TWO PLAYER LOOP
while PlayMode ==True:

    os.system('clear')
    

    DisplayGrid(Grid)

    #Check if player won
    if checkWin(Grid,"X") ==True or checkWin(Grid,"O"):
        print("Game Over!!")
        print("1.Enter Z to restart Game \n2.Enter X to exit")
    else:
        print(menu)
        #Player turns checker:
        if PlayerTurn ==True:
            print("Player 1's Turn:")
        else:
            print("Player 2's Turn:")

    #Check Turns
    if Turns ==0:
        os.system("clear")
        DisplayGrid(Grid)
        print("\nDRAW!!!!!!!!!!\n")
        print("1.Enter Z to restart Game \n2.Enter X to exit")

    #UserInput
    UserInput = input()

    if UserInput =="X" or UserInput =="x":
        print("Game Exited")
        break

    elif UserInput =="Z" or UserInput =="z":
        Grid = restart(Grid)
        Turns=9
        PlayerTurn = True
        continue

    elif UserInput in [str(i) for i in range(1,10)]:
        if PlayerTurn == True:
            UpdateGrid(Grid,UserInput,"X")
            PlayerTurn =False
        else:
            UpdateGrid(Grid,UserInput,"O")
            PlayerTurn =True
        Turns-=1

    

    

    
        




