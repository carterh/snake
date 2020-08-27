def draw(game_engine, stdscr):
    ROWS = game_engine.rows
    COLS = game_engine.cols

    #Clear the terminal
    stdscr.clear()

    #Draw the top line
    stdscr.addstr(0,1,' ' + ('_'*COLS) + ' ')
    
    #Draw the board
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
        stdscr.addstr(ROWS-row,1,''.join(rowChars))

    #Draw the bottom line
    stdscr.addstr(ROWS+1,1,'|'+ ('-'*COLS) + '|')

    #Refresh the terminal screen
    stdscr.refresh()
