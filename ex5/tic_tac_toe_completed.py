theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ',
            'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
the_num_Board = {'top-L': '1', 'top-M': '2', 'top-R': '3', 'mid-L': '4',
                 'mid-M': '5', 'mid-R': '6', 'low-L': '7', 'low-M': '8', 'low-R': '9'}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'
for i in range(9):
    printBoard(the_num_Board)
    print()
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        theBoard[move] = "X"
        turn = 'O'
    else:
        theBoard[move] = "O"
        turn = 'X'
printBoard(theBoard)
