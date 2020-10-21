from GameBoard import GameBoard


class GameDisplay:
    def __init__(self):
        self.__bomb_char = "💥"
        self.__shadow_char = "⬛"
        self.__flag_char = "🚩"
        #self.__number_chars = ["⬜","1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"]
        self.__number_chars = ["⬜","1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 "]

    def print_board(self, Gb: GameBoard) -> None:
        for row in Gb.get_grid():
            for cell in row:
                if cell.is_hidden():
                    if cell.is_flagged():
                        print(self.__flag_char, end='')
                    else:
                        print(self.__shadow_char, end='')
                else:
                    if cell.is_bomb():
                        print(self.__bomb_char, end='')
                    else:
                        print(self.__number_chars[cell.get_nearby_bombs()], end='')

            print('')
