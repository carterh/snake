from engine import *

def draw(game_engine):
    print(' ')
    #CR: fix the hard-coded indices
    for row in range(9,-1,-1):
        rowChars = []
        for col in range(10):
            if game_engine.inside_body(row,col):
                rowChars.append('o')
            else:
                rowChars.append('_')
        print(''.join(rowChars))
    print(' ')
