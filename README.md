#Hello World -- My first commit--TIC TAC TOE GAME (Vs Computer version, AI)
import copy
board={1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-',9:'-'}
turn='x'
def printboard(board):
    print('*********TIC - TAC - TOE GAME BOARD********')
    for i in range(1,10,3):
        print(board[i]+' | ' +board[i+1]+' | ' +board[i+2])
        print('----------')
def winr(board):
    flag=0
    for i in range(1,8,3):
        if board[i]== board[i+1]==board[i+2]=='x':
            flag=1
        elif board[i]== board[i+1]==board[i+2]=='o':
            flag=2
    for i in range(1,4,1):
        if board[i]==board[i+3]==board[i+6]=='x':
            flag=1
        elif board[i]==board[i+3]==board[i+6]=='o':
            flag=2
    if board[1]==board[5]==board[9]=='x':
        flag=1
    elif board[1]==board[5]==board[9]=='o':
        flag=2
    elif board[3]==board[5]==board[7]=='x':
        flag=1
    elif board[3]==board[5]==board[7]=='o':
        flag=2
    return flag 

def isspaceFree(board,move):
    return board[move]=='-'
def myAI(board):
    for i in range(1,10):        #If computer can win in next move
        cpy = copy.deepcopy(board)
        if isspaceFree(cpy,i):
            cpy[i]='o'
            if winr(cpy)==2:
                return i
    for i in range(1,10):       #If Mr X can win in the next move
        cpy= copy.deepcopy(board)
        if isspaceFree(cpy,i):
            cpy[i]='x'
            if winr(cpy)==1:
                return i
    for i in range(1,10,2):     #Acquire corners/center
        if isspaceFree(board,i):
            return i
    for i in range(2,10,2):     #Acquire rem. locations
        if isspaceFree(board,i):
            return i
print('WELCOME.. This is tictac AI, created by Mr Abhinav Srivastava')
print('Please enter your name :')
name=input()
print('Let the game begin.........')
printboard(board)
print('I am Mr ZeroHero , you will enter "x" ')
for i in range(9):
    if turn=='x':
        move=int(input('Input your move : '))
        if isspaceFree(board,move):
            board[move]='x'
    else:
        move= myAI(board)
        board[move]='o'
    printboard(board)
    if turn == 'x':
        turn='o'
    else:
        turn = 'x'
    if winr(board)==1 or winr(board) ==2 :
        break
if winr(board) == 1:
    print('Oh my Goodness! '+str(name)+', You defeated me... Such a intelligent move...Damn it...')
elif winr(board)==2:
    print('Yeah.. I won...YES..YES...You looser...!!!!')
else:
    print('Oh, Match ended in a draw , '+str(name) + ' You played quite well...')
