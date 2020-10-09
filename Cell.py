class Cell:
    def __init__(self):
        self.__flagged = False
        self.__bomb = False
        self.__hidden = True
        self.__nearby_bombs = 0

    def is_bomb(self) -> bool:
        return self.__bomb

    def set_bomb(self, bomb: bool) -> None:
        self.__bomb = bomb

    def is_flagged(self) -> bool:
        return self.__flagged

    def set_flagged(self, flagged: bool) -> None:
        self.__flagged = flagged

    def is_hidden(self) -> bool:
        return self.__hidden

    def set_hidden(self, hidden: bool) -> None:
        self.__hidden = hidden

    def get_nearby_bombs(self) -> int:
        return self.__nearby_bombs

    def set_nearby_bombs(self, nearby_bombs: int) -> None:
        self.__nearby_bombs = nearby_bombs
