import curses
from GameBoard import GameBoard
from Scoreboard import Scoreboard, stringify_winner
import time


def calculate_score(start_time, end_time):
    return (1 / (end_time - start_time)) * 10000


def render(scr, gb: GameBoard, cursor_y, cursor_x):
    """
    Affiche le démineur dans la "fenêtre" Curses
    :param scr:
    :param gb:
    :param cursor_y:
    :param cursor_x:
    :return:
    """
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


def game_over() -> None:
    """
    Affiche le menu de game over
    """
    print("Game Over!")
    print("Vous aurez probablement plus de chances la prochaine fois...")


def game_won(score) -> None:
    """
    Affiche le menu de victoire de partie
    :return:
    """

    scoreboard = Scoreboard()

    print("Vous avez gagné!")
    print("Voici votre score : ")
    print("")
    name = input("Entrez votre nom : ")

    scoreboard.add_to_scoreboard(name, score)
    scoreboard.save_scoreboard()


def display_score(scoreboard) -> None:
    """
    Display the scoreboard
    :param scoreboard: Instance de Scoreboard
    """
    print("Nos gagnants sont...")
    i = 1
    for winner in scoreboard.get_scoreboard():
        print(str(i) + ". " + stringify_winner(winner))
        i += 1


def display_controls() -> None:
    """
    Display the controls
    """
    print("[ARROWS] pour déplacer le curseur")
    print("[SPACE] pour révéler une case")
    print("[F] pour placer ou retirer un drapeau")


def play(scr) -> None:
    """
    Handles the controls and the game logic.
    :param scr: the instance of the window created by Curses
    """
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

    # start time
    start_time = time.time()

    while True:  # Main Loop
        ch = scr.getch()

        if ch == ord('q'):
            return

        if ch == ord(' '):
            # If the cell is flagged, prevent uncovering the cell
            if not gb.is_flagged(cursor_x - 1, cursor_y - 1) and gb.reveal(cursor_x - 1, cursor_y - 1):
                # There's a bomb here... Boom!
                curses.endwin()  # Close the game window
                game_over()
                break

            # Check if we found all the bombs
            if gb.get_remaining_bombs() == 0:
                curses.endwin()  # Close the game window
                game_won(calculate_score(start_time=start_time, end_time=time.time()))
                break

        if ch == ord('f'):
            gb.toggle_flagged(cursor_x - 1, cursor_y - 1)

        if ch == curses.KEY_LEFT and cursor_x > 1:
            cursor_x -= 1 % WIDTH

        elif ch == curses.KEY_RIGHT and cursor_x < WIDTH:
            cursor_x += 1 % WIDTH

        elif ch == curses.KEY_UP and cursor_y > 1:
            cursor_y -= 1 % HEIGHT

        elif ch == curses.KEY_DOWN and cursor_y < HEIGHT:
            cursor_y += 1 % HEIGHT

        render(scr, gb, cursor_x, cursor_y)


def main() -> None:
    """
    Handles the main menu.
    """
    scoreboard = Scoreboard()
    scoreboard.save_scoreboard()  # Créer le fichier scoreboard s'il n'existe pas

    # Affichage du menu
    print("Bienvenue sur le Démineur 3000")
    print("Réalisé par Patrick CONTI et Florian CUNY")
    print("")
    print("Que souhaitez-vous faire ?")
    print("1: Nouvelle partie")
    print("2: Afficher les scores")
    print("3: Afficher les contrôles")
    print("4: Quitter")

    selection = 0

    while selection != 4:
        if selection == 1:
            curses.wrapper(play)
        elif selection == 2:
            display_score(scoreboard)
        elif selection == 3:
            display_controls()

        print("")
        selection = int(input("Entrez un numéro : "))
        print("")


if __name__ == "__main__":
    main()
