import pprint
bingoNumbers = []
bingoBoards=[[[[0,0] for _ in range(5)] for _ in range(5)]for _ in range(100)]
bingoBoards[1][0][0][0]=1
pp=pprint.PrettyPrinter(indent=5)
boardNum=-1
boardRow=0
boardColumn=0
firstWinner=-1
lastWinner=-1
losers=[i for i in range(0,99+1)]
def find_winner():
    winner=-1
    for board in range(100):
        for row in range(5):
           points_row=bingoBoards[board][row][0][1]+bingoBoards[board][row][1][1]+bingoBoards[board][row][2][1]+bingoBoards[board][row][3][1]+bingoBoards[board][row][4][1]
           points_column=bingoBoards[board][0][row][1]+bingoBoards[board][1][row][1]+bingoBoards[board][2][row][1]+bingoBoards[board][3][row][1]+bingoBoards[board][4][row][1]
           if points_column==5 or points_row==5:
               winner=board
    return winner

def remove_winning_board(board):
    for row in range(5):
        points_row=bingoBoards[board][row][0][1]+bingoBoards[board][row][1][1]+bingoBoards[board][row][2][1]+bingoBoards[board][row][3][1]+bingoBoards[board][row][4][1]
        points_column=bingoBoards[board][0][row][1]+bingoBoards[board][1][row][1]+bingoBoards[board][2][row][1]+bingoBoards[board][3][row][1]+bingoBoards[board][4][row][1]
        if points_column==5 or points_row==5:
            losers.remove(board)       
def board_score(board):
    boardScore=0
    for row in range(5):
        for column in range(5):
            if bingoBoards[board][row][column][1]==0:
                boardScore+=bingoBoards[board][row][column][0]
    return boardScore
    
def check_if_winner(board):
    winner=-1
    for row in range(5):
               points_row=bingoBoards[board][row][0][1]+bingoBoards[board][row][1][1]+bingoBoards[board][row][2][1]+bingoBoards[board][row][3][1]+bingoBoards[board][row][4][1]
               points_column=bingoBoards[board][0][row][1]+bingoBoards[board][1][row][1]+bingoBoards[board][2][row][1]+bingoBoards[board][3][row][1]+bingoBoards[board][4][row][1]
               if points_column==5 or points_row==5:
                   winner=1
    return winner

with open("input.txt") as data:
    temp=data.readline()
    bingoNumbers =temp.split(",")
    for line in data:
        if line == '\n':
            boardNum+=1
            boardRow=0            
        else:
            temp=line.split()
            for numbers in temp:
                num=int(numbers)
                bingoBoards[boardNum][boardRow][boardColumn][0]=num
                boardColumn+=1
            boardRow+=1
            boardColumn=0
    for draw in bingoNumbers:
        for board in range(100):
            for row in range(5):
                for column in range(5):
                    if int(draw)==bingoBoards[board][row][column][0]:
                        bingoBoards[board][row][column][1]=1
        winner=find_winner()    
        if winner>0:
            if firstWinner<0:
                boardValue=0
                firstWinner=winner
                for row in range(5):
                    for column in range(5):
                        if bingoBoards[winner][row][column][1]==0:
                            boardValue+=bingoBoards[winner][row][column][0]
                boardValue=int(draw)*boardValue
                losers.remove(firstWinner)
        for board in losers:
            for row in range(5):
                points_row=bingoBoards[board][row][0][1]+bingoBoards[board][row][1][1]+bingoBoards[board][row][2][1]+bingoBoards[board][row][3][1]+bingoBoards[board][row][4][1]
                points_column=bingoBoards[board][0][row][1]+bingoBoards[board][1][row][1]+bingoBoards[board][2][row][1]+bingoBoards[board][3][row][1]+bingoBoards[board][4][row][1]
                if points_column==5 or points_row==5:
                    try:
                        losers.remove(board)
                    except:
                        pass
        if(len(losers)==1):
            lastWinner=losers[0]
        if(len(losers)==0):
            boardScore=board_score(lastWinner)
            boardScore=boardScore*int(draw)
            break
                
                
    print('First winner is board '+str(firstWinner)+' score '+str(boardValue))
    print('Last winner is board '+str(lastWinner)+' score '+str(boardScore))    