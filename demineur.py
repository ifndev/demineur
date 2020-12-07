import curses
from GameBoard import GameBoard


def render(scr, gb: GameBoard, cursor_y, cursor_x):
    y = 1
    for row in gb.get_grid():
        x = 1
        for cell in row:
            if y == cursor_y and x == cursor_x:
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
            x += 1
        y += 1


def main(scr):
    HEIGHT, WIDTH = scr.getmaxyx()  # Returns a tuple
    WIDTH -= 2
    HEIGHT -= 2

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)  # Mine
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)  # Flag
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)  # Cursor
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)  # Successfully spotted mine

    scr.border(0)
    curses.curs_set(False)

    gb = GameBoard(WIDTH, HEIGHT)
    cursor_x = 1
    cursor_y = 1

    gb.populate()
    
    render(scr, gb, cursor_y, cursor_x)

    while True:  # Main Loop
        ch = scr.getch()
        
        if ch == ord('q'):
            return
        
        if ch == ord(' '):
            # If the cell is flagged, prevent uncovering the cell
            if not gb.is_flagged(cursor_x - 1, cursor_y - 1) and gb.reveal(cursor_x - 1, cursor_y - 1):
                cursor_x, cursor_y = -1, -1

        if ch == ord('f'):
            gb.toggle_flagged(cursor_x-1, cursor_y-1)

        if ch == curses.KEY_LEFT and cursor_x > 1:
            cursor_x -= 1 % WIDTH

        elif ch == curses.KEY_RIGHT and cursor_x < WIDTH:
            cursor_x += 1 % WIDTH

        elif ch == curses.KEY_UP and cursor_y > 1:
            cursor_y -= 1 % HEIGHT

        elif ch == curses.KEY_DOWN and cursor_y < HEIGHT:
            cursor_y += 1 % HEIGHT

        render(scr, gb, cursor_x, cursor_y)


if __name__ == "__main__":
    curses.wrapper(main)
