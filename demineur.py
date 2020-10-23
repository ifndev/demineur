import curses
from GameBoard import GameBoard

def render(scr, Gb, cursorY, cursorX):
    y=1
    for row in Gb.get_grid():
        x=1
        for cell in row:
            if (y==cursorY and x==cursorX):
                scr.addstr(x, y, "+", curses.color_pair(3))
            
            elif cell.is_hidden():
                if cell.is_flagged():
                    scr.addstr(x, y, "F", curses.color_pair(2))
                    
                else:
                    scr.addstr(x, y, " ")
                    
            else:
                if cell.is_bomb():
                    if cell.is_flagged():
                        scr.addstr(x, y, "X", curses.color_pair(4))
                    else:
                        scr.addstr(x, y, "X", curses.color_pair(1))
                    
                else:
                    if cell.get_nearby_bombs() > 0:
                        scr.addstr(x, y, str(cell.get_nearby_bombs()), curses.A_REVERSE)
                    else:
                        scr.addstr(x, y, " ", curses.A_REVERSE)
            x +=1
        y+=1

def main(scr):
    HEIGHT, WIDTH = scr.getmaxyx()
    WIDTH-=2
    HEIGHT-=2

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED) # Mine
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE) # Flag
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW) # Cursor
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN) # Sucessfully spotted mine

    scr.border(0)
    curses.curs_set(False)

    Gb = GameBoard(WIDTH, HEIGHT)
    cursorX = 1
    cursorY = 1

    Gb.populate()
    
    render(scr, Gb, cursorY, cursorX)

    while True: # Main Loop
        ch = scr.getch()
        
        if ch == ord('q'):
            return
        
        if ch == ord(' '):
            if(Gb.reveal(cursorX-1, cursorY-1)):
                cursorX, cursorY = -1, -1
            

        if ch == ord('f'):
            Gb.toggle_flagged(cursorX-1, cursorY-1)
            

        if ch == curses.KEY_LEFT and cursorX > 1:
            cursorX -=1 % WIDTH

        elif ch == curses.KEY_RIGHT and cursorX < WIDTH:
            cursorX +=1 % WIDTH

        elif ch == curses.KEY_UP and cursorY > 1:
            cursorY -= 1 % HEIGHT

        elif ch == curses.KEY_DOWN and cursorY < HEIGHT:
            cursorY += 1 % HEIGHT

        render(scr, Gb, cursorX, cursorY)

        


if __name__=="__main__":
    curses.wrapper(main)