import player_input, choose_first, display_board, place_marker, player_choice, replay, space_check, win_check

print('Welcome to Tic Tac Toe!')

# WHILE LOOP TO KEEP RUNNING THE GAME
while True:
    # PLAY THE GAME
    
    # Set the game up here (Display the Board, Identify who plays  first and assign markers X,O)
    
    the_board = [' '] * 10
    player1_marker,player2_marker = player_input.player_input()
    
    turn = choose_first.choose_first()
    print(turn + ' will go first')
    
    play_game = input( 'ready to play? y or n? ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    # GAME PLAY
    
    while game_on:
        
        if turn == 'Player 1':
            
            # Display the board
            display_board.display_board(the_board)
            print ('Player 1, your move: \n')
            
            # choose a position
            position = 0
            while position not in [1,2,3,4,5,6,7,8,9] or not space_check.space_check(the_board,position):
                position = player_choice.player_choice(the_board)
            
            # Place the marker on the position
            place_marker.place_marker(the_board, player1_marker,position)
            
            # Check if player 1 has won
            if win_check.win_check(the_board,player1_marker):
                display_board.display_board(the_board)
                print('PLAYER 1 HAS WON !!')
                game_on = False
            else: # check if its a tie game
                for i in range(1,10):
                    if space_check.space_check(the_board, i) == True: 
                        space = True
                    else:
                        space = False
            if space == False:
                display_board.display_board(the_board)
                print("TIE GAME")
                game_on = False
                
            else:
                turn = 'Player 2'
                
        
        # No tie and no win then next players turn
    

        #Player 2 Turn
        else:
            #Display the board
            display_board.display_board(the_board)
            print ('Player 2, your move: \n')
            
            # choose a position
            position = 0
            while position not in [1,2,3,4,5,6,7,8,9] or not space_check.space_check(the_board,position):
                position = player_choice.player_choice(the_board)
            
            # Place the marker on the position
            place_marker.place_marker(the_board, player2_marker,position)
            
            # Check if Player 2 has won
            if win_check.win_check(the_board,player2_marker):
                display_board.display_board(the_board)
                print('PLAYER 2 HAS WON !!')
                game_on = False
            else:
                for i in range(1,10):
                    if space_check.space_check(the_board, i) == True: #if the position is empty, return false.
                        space = True
                    else:
                        space = False
            if space == False:
                display_board.display_board(the_board)
                print("TIE GAME")
                game_on = False
                
            else:
                turn = 'Player 1'
        # Player2's turn.
        
            
            #pass

    if not replay.replay():
        break
    # BREAK OUT OF THE WHILE LOOP