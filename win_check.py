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
    
   