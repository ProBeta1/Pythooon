board={1:'--',2:'--',3:'--',4:'--',5:'--',6:'--',7:'--',8:'--',9:'--'}
flag=0
def printboard(board):
    print('yo ... printing....')
    for i in range(1,10,3):
        print(board[i]+' | ' +board[i+1]+' | ' +board[i+2])
        print('-----------------------')
    print('Hahaha .....')
def win(board):
    flag=0
    for i in range(1,8,3):
        if board[i]== board[i+1]==board[i+2]=='x':
            flag=1
        else
    for i in range(1,4,1):
        if board[i]==board[i+3]==board[i+6]=='x':
            flag=1
    #dia
    if board[1]==board[5]==board[9]=='x':
        flag=1
    elif board[3]==board[5]==board[7]=='x':
        flag=1
    if flag == 1:
        print('HOHO Mr X ne baaji mar leee.....')
        return 10

        
turn='x'

for i in range(9):
    if turn=='x':
        move=int(input('Input Mr X : '))
        board[move]='x'
    if turn=='o':
        move=int(input('Enter Mr Zero :'))
        board[move]='o'
    printboard(board)
    if turn=='x':
        turn='o'
    else:
        turn='x'
    if(win(board))==10:break
    
