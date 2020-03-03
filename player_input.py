def player_input():
    '''
    This function is to assign each player with a marker (X or O)
    '''
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