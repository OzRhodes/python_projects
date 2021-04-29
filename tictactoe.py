1
1
# Simple Tic Tac Toe with simple intelligence

import random

def printBoard(board):
    print('\n\n')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
    print('\n')

    
def insertLetter(ltr, pos):
    board[pos] = ltr
    
def computerMove():
    # options to move exclusing 0
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x !=0]
    # default is end of game
    move = 0 
    
    # can I or play win if yes place my counter there
    
    for ltr in ['O','X']:
        for possMove in possibleMoves:
            # create clone and then check if we are a winner in any of the spots free
            copyBoard = board[:]
            copyBoard[possMove] = ltr 
            if isWinner (copyBoard,ltr):
                move=possMove
                return move
                
    # try centre
    if 5 in possibleMoves:
        move =5
        return 5
        
    # try corner
    cornersFree = []
    for possMove in possibleMoves:
        if possMove in [1,3,7,9]:
            cornersFree.append(possMove)
    if len(cornersFree) >0:
        move = selectCorner(cornersFree)
        return move
            
    # try edge
    edgesFree = []

    for possMove in possibleMoves:
        if possMove in [2,4,6,8]:
            edgesFree.append[i]
    if len(edgesFree) >0:
        move = selectEdge(edgesFree)
        return move

def selectEdge(edges):
    length = len(edges)
    r = random.randrange(1, length)
    return edges(r)
    
             
def selectCorner(corners):   
   length = len(corners)
   r = random.randrange(1, length)
   return corners(r)                   
         
def spaceFree(pos):
    if board[pos] ==' ':
        return True
    else:
        return False 
    
def isWinner(board, ltr):
    winner = False
    if (board[1] == ltr and board[2] == ltr and board[3] == ltr):
        winner = True
    if (board[4] == ltr and board[5] == ltr and board[6] == ltr):
        winner = True
    if (board[7] == ltr and board[8] == ltr and board[9] == ltr):
        winner = True
    if (board[1] == ltr and board[4] == ltr and board[7] == ltr):
        winner = True
    if (board[2]== ltr and board[5] == ltr and board[8] == ltr):
        winner = True
    if (board[3] == ltr and board[6] == ltr and board[9] == ltr): 
        winner = True
    if (board[1] == ltr and board[5] == ltr and board[9] == ltr): 
         winner = True
    if (board[3] == ltr and board[5] == ltr and board[7] == ltr):
        winner = True

    return winner
        
def boardFull(board):
    if ' ' in board:
        return False
    else:
        return True

def playerMove():
    play = True
    while play:
        move = input('Please select a postion for your X. (1-9) : ')
        try:
            move = int(move)    
            if move >0 and move <10:
                if spaceFree(move):
                    print (move)
                    insertLetter('X', move)
                    play = False                
                else:
                    print('Sorry...space is taken...try again. ')        
            else:
                print('Enter and number between 1 & 9')
        except:
            print('Please type a number...???')



board = [' ' for i in range (10)]

def main():
    
    print ('Welcome to tic tac toe !\n\n')
    
    printBoard(board)
    
    
    # still spaces to go
    while not boardFull(board):
        
        #player
        if not isWinner(board, 'X'):
            playerMove()
            printBoard(board)
        if isWinner(board, 'X'):
            print('Sorry - X - won this time')
            break
    
        if not isWinner(board, 'O'):
            move = computerMove()
            if move == 0: # Computer can't move
                print('Tied Game!!!')
            else:
                insertLetter('O',move)
                print('Computer move is : ' + str(move))
                printBoard(board)
        if isWinner(board, 'O'):
            print('Sorry - O - won this time')
            break
    

        
main()
