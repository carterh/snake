from engine import *
ROWS = 20
COLS = 20

def draw(game_engine):
    print(' ' + ('_'*COLS) + ' ')
    #CR: fix the hard-coded indices
    for row in range(ROWS-1,-1,-1):
        rowChars = ['|']
        for col in range(COLS):
            if game_engine.inside_body((row,col)):
                rowChars.append('o')
            elif game_engine.apple == (row,col):
                rowChars.append('a')
            else:
                rowChars.append(' ')
        rowChars.append('|')
        print(''.join(rowChars))
    print('|'+ ('-'*COLS) + '|')
