import sys

gameboard = [[8,0,0,4,0,6,0,0,3],
             [0,0,9,0,0,0,0,2,0],
             [0,0,0,0,0,0,0,0,1],
             [0,0,0,8,0,0,4,0,0],
             [0,6,0,0,0,0,0,1,0],
             [0,0,3,0,0,2,0,0,9],
             [7,0,2,0,3,0,0,0,0],
             [0,4,0,0,0,0,5,0,0],
             [5,0,0,7,0,9,0,0,8]]

def prtPuzzle():
    global gameboard
    for i in range(0,9):
        print(gameboard[i])
    return

def possible(y,x,n): # row, column, number
    global gameboard
    for i in range(0,9):
        if gameboard[y][i] == n or gameboard[i][x] == n: # check row and column
            return False

    # treat each 3x3 square as a separate matrix
    xSquare = (x//3)*3      # find local 0,0 of the 3x3 square
    ySquare = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if gameboard[ySquare+i][xSquare+j] == n: # check the 3x3 square
                return False

    # if we reach this point, the number n was not in the row, column, or square
    # this is a possible placement of that number
    return True

def solve():
    global gameboard

    # loop through gameboard
    for y in range(0,9):
        for x in range(0,9):
            if gameboard[y][x] == 0:        # find an empty cell
                for n in range(1,10):       # check all possible numbers
                    if possible(y,x,n):     # if number can be placed currently
                        gameboard[y][x] = n # place number in gameboard
                        solve()             # try to solve the board with the new number

                        # if we reach this point, the current number placements didn't yeild a solution
                        #   so we reset the cell back to 0 since this was not the correct number
                        gameboard[y][x] = 0
                        
                # if no number is valid in the current cell return to the previous interation of solve()
                return

    # if we reach this point, all numbers have been placed
    #   call function to print the gameboard
    prtPuzzle()
