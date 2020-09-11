def printboard(board):
    print('\t\t' + '|' + '\t\t' + '|' + '    ')
    print('   ' + board[1] + '    ' + '|' + '   ' + board[2] + '   ' + '|' + '   ' + board[3] + '    ')
    print('\t\t' + '|' + '\t\t' + '|' + '\t\t')
    print('--------' + '|' + '-------' + '|' + '--------')
    print('\t\t' + '|' + '\t\t' + '|' + '\t\t')
    print('   ' + board[4] + '    ' + '|' + '   ' + board[5] + '   ' + '|' + '   ' + board[6] + '    ')
    print('\t\t' + '|' + '\t\t' + '|' + '\t\t')
    print('--------' + '|' + '-------' + '|' + '--------')
    print('\t\t' + '|' + '\t\t' + '|' + '\t\t')
    print('   ' + board[7] + '    ' + '|' + '   ' + board[8] + '   ' + '|' + '   ' + board[9] + '    ')
    print('\t\t' + '|' + '\t\t' + '|' + '\t\t')


def validInput(board):
    position = 0
    valid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    alreadythere = False
    while position not in valid or alreadythere:
        alreadythere = False
        printboard(board)
        position = input('\n\nPlease choose a space numbered between 1 and 9: ')
        if not position.isdigit():
            print('\n' * 100)
            print("Sorry you need to choose between 1 and 9")
        else:
            position = int(position)
            if board[position] == 'x' or board[position] == 'o':
                print('\n' * 100)
                alreadythere = True
                print('This position is taken. Choose another. Dont be dumb')
            elif position not in valid:
                print("Sorry you need to choose between 1 and 9")
                print('\n' * 100)
    print('\n'*100)
    return position


def winnerCheck(boardlist):
    if boardlist[1] == boardlist[2] == boardlist[3] == 'x' or  boardlist[1] == boardlist[2] == boardlist[3] == 'o':
        return True
    elif boardlist[4] == boardlist[5] == boardlist[6] == 'x' or  boardlist[4] == boardlist[5] == boardlist[6] == 'o':
        return True
    elif boardlist[7] == boardlist[8] == boardlist[9] == 'x' or  boardlist[7] == boardlist[8] == boardlist[9] == 'o':
        return True
    elif boardlist[1] == boardlist[4] == boardlist[7] == 'x' or  boardlist[1] == boardlist[4] == boardlist[7] == 'o':
        return True
    elif boardlist[2] == boardlist[5] == boardlist[8] == 'x' or  boardlist[2] == boardlist[5] == boardlist[8] == 'o':
        return True
    elif boardlist[3] == boardlist[6] == boardlist[9] == 'x' or  boardlist[3] == boardlist[6] == boardlist[9] == 'o':
        return True
    elif boardlist[1] == boardlist[5] == boardlist[9] == 'x' or  boardlist[1] == boardlist[5] == boardlist[9] == 'o':
        return True
    elif boardlist[7] == boardlist[5] == boardlist[3] == 'x' or  boardlist[7] == boardlist[5] == boardlist[3] == 'o':
        return True
    else:
        return False

person1 = input('Player 1 please enter your name: ')
person2 = input('Player 2 please enter your name: ')
play = True
while play:
    print('====================Welcome to TIc Tac TOE!===================='+'\n\n')
    valid = ['x', 'o']
    player1 = 'none'
    player2 = 'none'
    while player1 not in valid:
        player1 = input(person1 + ' please choose either x or o: ')
        player1 = player1.lower()
        if player1 not in valid:
            print("Sorry! You have to choose either x or o. Try again.")
    print(person1+' is ' + player1)
    if player1 == 'x':
        print(person2 + ' is ' + 'o')
        player2 = 'o'
    else:
        print(person2+' is ' + 'x')
        player2 = 'x'
    position1 = 0
    position2 = 0
    turn1 = False
    turn2 = False
    boardlist = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    if player1 == 'x':
        print(person1+' is x so you will go first')
        position1 = validInput(boardlist)
        boardlist[position1] = player1
        turn1 = True
    else:
        print(person2+' is x so you will go first')
        position2 = validInput(boardlist)
        boardlist[position2] = player2
        turn2 = True
    winner = False
    score1 = 0
    score2 = 0
    count = 1
    while not winner and count != 9:
        if not turn1:
            print(person1+' its your turn. Go ahead')
            position1 = validInput(boardlist)
            boardlist[position1] = player1
            turn1 = True
            turn2 = False
            count += 1
        else:
            print(person2+' its your turn. Go ahead')
            position2 = validInput(boardlist)
            boardlist[position2] = player2
            turn2 = True
            turn1 = False
            count += 1
        if winnerCheck(boardlist):
            printboard(boardlist)
            if turn1:
                print("===================="+person1+" HAS WON THE GAME!!!====================")
                score1 += 1
                winner = True
            else:
                print('===================='+person2+' HAS WON THE GAME!!!====================')
                score2 += 1
                winner = True
            print(score2)
            playagain = input('Would you like to play again? y or n: ')
            playagain = playagain.lower()
            if playagain == 'n':
                play = False
            else:
                play = True
        elif count == 9:
            print('====================THIS WAS A DRAWWWW====================!!!')
            printboard(boardlist)
            playagain = input('Would you like to play again? y or n: ')
            playagain = playagain.lower()
            if playagain == 'n':
                play = False
            else:
                play = True



















