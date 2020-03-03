 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from IPython.display import clear_output
#game = [[1,2,3], [4,5,6], [7,8,9]]
def display_board(board):
    clear_output()
    ''' 
    row1 = board[1:4]
    row2 = board[4:7]
    row3 = board[7:]
    game = [row1, row2, row3]
    print('    0    1    2')
    for row,col in enumerate(game):
    print(row, col)
    '''
       
        
        
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
        

def player_input():
    #player1 = input("Please pick a marker 'X' or 'O'")
    marker = ''
    # KEEP ASKING PLAYER 1 TO CHOOSE 'X' OR 'O'
    while marker != 'X' and marker != 'O':
    #while not (marker == 'X' or marker == 'O'):
        marker = input('Player1: choose X or O:').upper()
        # ASSIGN MARKER TO PLAYER 1, AND THE OPPOSITE MARKER TO PLAYER2    
        player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return (player1, player2)
	
	
	
def place_marker(board, marker, position):
    
    board[position] = marker
	
	
	
def win_check(board, mark):
    
    # GAME WIN CONDITION
    return((board[1] == board[2] == board[3] == mark) or #(Check Horizontal win condition. (Rows))
           (board[4] == board[5] == board[6] == mark) or
           (board[7] == board[8] == board[9] == mark) or
           # Vertical win Condition (Columns)
           (board[1] == board[4] == board[7] == mark) or
           (board[2] == board[5] == board[8] == mark) or
           (board[3] == board[6] == board[9] == mark) or
           # Diagonal win condition
           (board[1] == board[5] == board[9] == mark) or
           (board[3] == board[5] == board[7] == mark))
    
   
import random

def choose_first():
    flip = random.randint(0,1) # this will randomly generate 0 or 1 like a coin flip 
    if flip == 1:
        return 'Player 1'
    else:
        return 'Player 2'
		
		
def space_check(board, position):
    
    '''
    freely available means that the position is an empty string. 
    the syntax return board[position] == ' ' returns true if the the string is empty or false if its not.
    NOTE when 'return' is used, its used to check the validity of a statement.
    '''
    return board[position] == ' '
	
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i): #if the position is empty, return false.
            return False
    # Board if Full, the above returns true.
    return True
	
def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
    #while position not in range(1,10) or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
        
    return position
	
	
	
def replay():
    
    choice = input('Play again? Enter Yes or No')
    
    return choice == 'Yes'  #return true if the answer is 'yes'

# WHILE LOO TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac Toe!')

while True:
    # PLAY THE GAME
    

    # Set the game up here (Board, Who's  first, Choose markers X,O)
    
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input( 'ready to play? y or n?')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    # GAME PLAY
    
    while game_on:
        
        if turn == 'Player 1':
            
            # show the board
            display_board(the_board)
            print ('Player 1, your move: \n')
            
            # choose a position
            position = player_choice(the_board)
            
            # Place the marker on the position
            place_marker(the_board, player1_marker,position)
            
            # Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON !!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    game_on = False
                else:
                    turn = 'Player 2'
            
            # Or check if there is a tie
            
            # No tie and no win then next players turn
    

        #Player 2 Turn
        
        else:
            # show the board
            display_board(the_board)
            print ('Player 2, your move: \n')
            # choose a position
            position = player_choice(the_board)
            
            # Place the marker on the position
            place_marker(the_board, player2_marker,position)
            
            # Check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON !!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    game_on = False
                else:
                    turn = 'Player 1'
        # Player2's turn.
        
            
            #pass

    if not replay():
        break
    # BREAK OUT OF THE WHILE LOOP
	

   
	

