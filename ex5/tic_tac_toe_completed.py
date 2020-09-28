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
    """[summary]

    Args:
        board (Dict): dict of value on tic tac toe
    """
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def checkwin(board, turn):
    for i in check_list:
        if board[f"{i[0]}"] == " " or board[f"{i[1]}"] == " " or board[f"{i[2]}"] == " ":
            continue
        elif board[f"{i[0]}"] == board[f"{i[1]}"] == board[f"{i[2]}"]:
            printBoard(theBoard)
            print(f"{turn} WIN!!!")
            sys.exit()


turn = 'X'
indexlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# loop 9 time
for i in range(9):
    printBoard(the_num_Board)
    print()
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    # check move that is not letter or more than 9
    while True:
        move = input()
        try:
            o = int(move)
        except ValueError:
            print("Incrorect type")
            continue
        if o not in range(1, 10):
            print("Index out of range")
            continue
        if "X" in theBoard[move] or "O" in theBoard[move]:
            print("This number is already used")
            continue
        theBoard[move] = turn
        break
    checkwin(theBoard, turn)
    if turn == 'X':
        turn = 'O'
    elif turn == "O":
        turn = 'X'
    if i == 8:
        print("Draw!")

printBoard(theBoard)
