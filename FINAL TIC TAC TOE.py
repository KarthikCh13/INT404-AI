import random

def BuildGame(bd1):
    print('   |   |')
    print(' ' + bd1[7] + ' | ' + bd1[8] + ' | ' + bd1[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + bd1[4] + ' | ' + bd1[5] + ' | ' + bd1[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + bd1[1] + ' | ' + bd1[2] + ' | ' + bd1[3])
    print('   |   |')

def PlayerInputXorO():
    Piece = ''
    while not (Piece == 'X' or Piece == 'O'):
        print('Chose which one you want to play with : X or O')
        Piece = input().upper()

    if Piece == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def FirstMove():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def RandomlyChooseMove(RandomBoard, movesList):
    MovePossibilities = []
    for i in movesList:
        if FreeBlock(RandomBoard, i):
            MovePossibilities.append(i)

    if len(MovePossibilities) != 0:
        return random.choice(MovePossibilities)
    else:
        return None

def PlayMove(pBoard, letter, move):
    pBoard[move] = letter


def CopyBoard(BoardC):
    boardCopy = []

    for i in BoardC:
        boardCopy.append(i)

    return boardCopy

def ReadAIMove(AIBoard, LetterOfAI):
    if LetterOfAI == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = CopyBoard(AIBoard)
        if FreeBlock(copy, i):
            PlayMove(copy, LetterOfAI, i)
            if WinnerCheck(copy, LetterOfAI):
                return i

    for i in range(1, 10):
        copy = CopyBoard(AIBoard)
        if FreeBlock(copy, i):
            PlayMove(copy, playerLetter, i)
            if WinnerCheck(copy, playerLetter):
                return i

    move = RandomlyChooseMove(AIBoard, [1, 3, 7, 9])
    if move != None:
        return move

    if FreeBlock(AIBoard, 5):
        return 5

    return RandomlyChooseMove(AIBoard, [2, 4, 6, 8])

def FreeBlock(fBoard, move):
    return fBoard[move] == ' '

def ReadPlayerMove(pBoard):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not FreeBlock(pBoard, int(move)):
        print('Where do you want to place your next move? \n Select between 1 - 9')
        move = input()
    return int(move)




def BoardFull(full):
    for i in range(1, 10):
        if FreeBlock(full, i):
            return False
    return True


def WinnerCheck(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[7] == letter and board[4] == letter and board[1] == letter) or
    (board[8] == letter and board[5] == letter and board[2] == letter) or
    (board[9] == letter and board[6] == letter and board[3] == letter) or
    (board[7] == letter and board[5] == letter and board[3] == letter) or
    (board[9] == letter and board[5] == letter and board[1] == letter))

def StartOver():
    print('Do you want to play again?\n Type yes or no')
    return input().lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    BoardMain = [' '] * 10
    HumanLetter, AILetter = PlayerInputXorO()
    turn = FirstMove()
    print('The ' + turn + ' will start first.')
    GameOnGoing = True

    while GameOnGoing:
        if turn == 'player':
            BuildGame(BoardMain)
            move = ReadPlayerMove(BoardMain)
            PlayMove(BoardMain, HumanLetter, move)

            if WinnerCheck(BoardMain, HumanLetter):
                BuildGame(BoardMain)
                print('HOW DID YOU WIN? I THOUGHT IT WAS IMPOSSIBLE')
                GameOnGoing = False
            else:
                if BoardFull(BoardMain):
                    BuildGame(BoardMain)
                    print('You tied with the AI! \n Get used to this. You will see this a lot')
                    break
                else:
                    turn = 'computer'

        else:
            move = ReadAIMove(BoardMain, AILetter)
            PlayMove(BoardMain, AILetter, move)

            if WinnerCheck(BoardMain, AILetter):
                BuildGame(BoardMain)
                print('Seriously? You let a few if conditions beat you?')
                GameOnGoing = False
            else:
                if BoardFull(BoardMain):
                    BuildGame(BoardMain)
                    print('You tied with the AI! \n Get used to this. You will see this a lot')
                    break
                else:
                    turn = 'player'

    if not StartOver():
        break