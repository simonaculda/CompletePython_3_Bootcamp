import random


def display_board(board):
    # print('\n'*100)
    print('_   _   _')
    for i in range(0, 3):
        print('  |   |  ')
        print(board[3*i+1] + ' | ' + board[3*i+2] + ' | ' + board[3*i+3])
        print('_ | _ | _')


def player_input():
    """

    :return: Player1 marker, PLayer2 marker
    """
    print('Welcome to Tic Tac Toe!')
    marker = ''
    while marker != 'X' and marker != '0':
        marker = input('Player 1, please chose X or 0 ').upper()

    player1 = marker
    if player1 == 'X':
        player2 = '0'
    else:
        player2 = 'X'
    return (player1, player2)


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, mark):
    for i in range(0,3):
        if board[3*i+1] == board[3*i+2] == board[3*i+3] == mark:
            return True
    if board[1] == board[4] ==board[7]==mark or board[2]==board[5]==board[8]==mark or board[3]==board[6]==board[9] == mark:
        return True

    if (board[3]==board[5]==board[7]==mark) or (board[1]==board[5]==board[9] == mark):
        return True

    return False


def chose_first():
    if random.randint(1, 2) == 1:
        return 'Player1'
    else:
        return 'Player2'


def space_check(board, position):

    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Chose your next position: (1-9)'))

    return position


def replay():
    answer = ''
    while answer != 'Yes' and answer != 'No':
        answer = str(input('Do you want to play again? Enter Yes or No:'))
    if answer == 'Yes':
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')
while True:
    main_board = [' '] * 10

    p1_marker, p2_marker = player_input()

    turn = chose_first()
    print(turn + ' will go first')
    answer = ''
    while 'Yes' != answer and answer != 'No':
        answer = str(input('Are you ready to play? Enter Yes or No'))
    if answer == 'Yes':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player1':
            # show the board
            display_board(main_board)
            # chose a position
            poz = player_choice(main_board)
            # place the marker
            place_marker(main_board, p1_marker, poz)
            # check if won
            if win_check(main_board,p1_marker):
                display_board(main_board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(main_board):
                    display_board(main_board)
                    print('Tie Game')
                    break
                else:
                    turn = 'Player2'

            # or check if tie
            # not tie not win? then next player's turn
        else:
            display_board(main_board)
            # chose a position
            poz = player_choice(main_board)
            # place the marker
            place_marker(main_board, p2_marker, poz)
            # check if won
            if win_check(main_board,p2_marker):
                display_board(main_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(main_board):
                    display_board(main_board)
                    print('Tie Game')
                    break
                else:
                    turn = 'Player1'

            # or check if tie
            # not tie not win? then next player's turn
    if not replay():
        break







# player_input()
dis_board = ['0','X','0','X','0','X','0','X','0','X']
print(full_board_check(dis_board))
# print(chose_first())
# print(win_check(dis_board,'0'))
# display_board(place_marker(dis_board,'$', 8))
# display_board(['#','X','O','X','O','X','O','X','O','X'])


