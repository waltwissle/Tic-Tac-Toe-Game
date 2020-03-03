def space_check(board, position):
    '''
    This function checks for empty spaces on the board

    '''
    
    if board[0] or board[1] or board[2] or board[3] or board[4] or board[5] or board[6] or board[7] or board[8] or board[9] == ' ':
        return True