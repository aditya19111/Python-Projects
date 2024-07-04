game_on = True

winner = None

current_player = 'X'

board = ['-','-','-','-','-','-','-','-','-']

def display_board():
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])
    
def user():
    print('Player 1 select X OR O')
    p1 = input()
    p2 = ''
    if p1 == 'X':
        p2 = 'O'
        print('player 2 is:'+p2)
    elif p1 == 'O':
        p2 = 'X'
        print('player 2 is:'+p2)
    else:
        print('invalid entry try again!')
        user()

def filling_box():
    global current_player
    print(current_player + "'s turn")
    valid = True
    while valid is True:
        position = input("Choose position from 1 - 9: ")
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
          position = input("Choose position from 1 - 9: ")
        position = int(position) - 1

        if board[position] == "-":
            break
        else:
            print("Slot already taken")
    board[position] = current_player
    display_board()

def flip_turn():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

def win_or_tie():
    global current_player
    global game_on
    global winner
    if board[0] == board[1] == board[2] != '-':
        game_on = False
        winner = current_player
        print('your winner is: '+winner)
    elif board[3] == board[4] == board[5] != '-':
        game_on = False
        winner = current_player
        print('your winner is: '+winner)
    elif board[6] == board[7] == board[8] != '-':
        game_on = False
        winner = current_player
        print('your winner is: '+winner)
    elif board[0] == board[3] == board[6] != '-':
        game_on = False
        winner = current_player
        print('your winner is: '+winner)
    elif board[1] == board[4] == board[7] != '-':
        game_on = False
        winner = current_player
        print('your winner is: '+winner)
    elif board[2] == board[5] == board[8] != '-':
        game_on = False
        winner = current_player
        print('your winner is: '+winner)
    elif board[0] == board[4] == board[8] != '-':
        game_on = False
        winner = current_player
        print('your winner is: '+winner)
    elif board[2] == board[4] == board[6] != '-':
        game_on = False
        winner = current_player
        print('your winner is: '+ winner)
    elif '-' not in board:
        print('Its a tie!!')
    

def actual_game():
    display_board()
    user()
    while game_on:
        filling_box()
        win_or_tie()
        flip_turn()

actual_game()

    



