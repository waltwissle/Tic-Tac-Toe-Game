from IPython.display import clear_output
#game = [[1,2,3], [4,5,6], [7,8,9]]
def display_board(board):
    clear_output()
    ''' 
    This function displays the game board
    '''
       
        
        
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
        