import numpy as np
import random

#created 3x3 multi-array with numpy
def board_create():
    return(np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))

#controlling all possiblities and fill all of these in 'l' (an empty list.)
def allPossibilities(board):
    l = []
      
    for i in range(len(board)):
        for j in range(len(board)):
              
            if board[i][j] == 0:
                l.append((i, j))
    return(l)

#selecting a random place in 'l' first and set the selected place as 'player number'
def random_place_selection(board, player):
    selection = allPossibilities(board) #create an object as selection which is equal to function's return.
    current_loc = random.choice(selection)
    board[current_loc] = player #setting selected place as 'player number'
    return(board)

#controlling direction of horizontal 
def horizontalWin(board, player):
    for x in range(len(board)):
        win = True
          
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue
                  
        if win == True:
            return(win)
    return win
#controlling direction of vertical
def verticalWin(board, player):
    for x in range(len(board)):
        win = True
          
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
                  
        if win == True:
            return(win)
    return(win)
#controlling direction of diagonal
def diagonalWin(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return win

#evaluate if there is any winner.  
def evaluate(board):
    winner = 0
      
    for player in [1, 2]:
        if (horizontalWin(board, player) or
            verticalWin(board,player) or 
            diagonalWin(board,player)):
                 
            winner = player
              
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
  
# Main function to start the game
def play():
    board, winner, counter = board_create(), 0, 1
    print(board)
      
    while winner == 0:
        for player in [1, 2]:
            board = random_place_selection(board, player)
            print("Board after " + str(counter) + " move")
            print(board)
            
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return(winner)
  
if str(play()) == "-1":
    print("No Winner. Draw!")
else:
    print("The winner is Player " + str(play()))

