from random import randrange


def DisplayBoard(board):
    print("+-------" * 3,"+",sep="")
    for row in range(3):
        print("|       " * 3,"|",sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ",end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")


def EnterMove(board):
    ok = False
    while not ok:
        move = input("Enter your move: ") 
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if not ok:
            print("Wrong move! Please, try again.")
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3
        sign = board[row][col]
        ok = sign not in ['O','X'] 
        if not ok:
            print("Occupied already! Give it another try")
            continue
    board[row][col] = 'O'


def ListOfFreeFields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O','X']:
                free.append((row,col))
    return free


def VictoryFor(board,sgn):
    if sgn == "X":
        who = 'machine'
    elif sgn == "O":
        who = 'human'
    else:
        who = None
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn:
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def DrawMove(board):
    free = ListOfFreeFields(board)
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
board[1][1] = 'X'
free = ListOfFreeFields(board)
humanturn = True
while len(free):
    DisplayBoard(board)
    if humanturn:
        EnterMove(board)
        victory = VictoryFor(board,'O')
    else:   
        DrawMove(board)
        victory = VictoryFor(board,'X')
    if victory != None:
        break
    humanturn = not humanturn       
    free = ListOfFreeFields(board)


DisplayBoard(board)
if victory == 'human':
    print("You won, human!")
elif victory == 'machine':
    print("The machine won!")
else:
    print("Draw!")