import sys
theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
the_num_Board = {'1': '1', '2': '2', '3': '3',
                 '4': '4', '5': '5', '6': '6',
                 '7': '7', '8': '8', '9': '9'}
check_list = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
              [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7])


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def checkwin(board, turn):
    """[summary]

    Args:
        lx ([type]): [description]
        lo ([type]): [description]1
    >>> checwin([1,2,3], [2,4,5])
    X win1
    """
    for i in check_list:
        if board[f"{i[0]}"] == " " or board[f"{i[1]}"] == " " or board[f"{i[2]}"] == " ":
            continue
        elif board[f"{i[0]}"] == board[f"{i[1]}"] == board[f"{i[2]}"]:
            printBoard(theBoard)
            print(f"{turn} WIN!!!")
            sys.exit()


turn = 'X'
indexlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(9):
    printBoard(the_num_Board)
    print()
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    while True:
        move = input()
        try:
            o = int(move)

        except ValueError:
            print("Incrorect type")
            continue
        try:
            c = indexlist[o-1]
            break
        except IndexError:
            print("Type number 1-9 ")
            continue
        theBoard[move] = turn
    if turn == 'X':
        theBoard[move] = "X"
        checkwin(theBoard, turn)
        turn = 'O'

    elif turn == "O":
        theBoard[move] = "O"
        checkwin(theBoard, turn)
        turn = 'X'


printBoard(theBoard)
