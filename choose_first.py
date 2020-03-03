import random

def choose_first():
    '''
    This funtion is to randomly select who plays first.
    '''
    flip = random.randint(0,1) # this will randomly generate 0 or 1 like a coin flip 
    if flip == 1:
        return 'Player 1'
    else:
        return 'Player 2'