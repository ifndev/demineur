class Cell:
    def __init__(self):
        self.__flagged = False
        self.__bomb = False
        self.__hidden = True
        self.__nearby_bombs = 0

    def is_bomb(self):
        return self.__bomb

    def set_bomb(self, bomb: bool):
        self.__bomb = bomb

    def is_flagged(self):
        return self.__flagged

    def set_flagged(self, flagged: bool):
        self.__flagged = flagged

    def is_hidden(self):
        return self.__hidden

    def set_hidden(self, hidden: bool):
        self.__hidden = hidden

    def get_nearby_bombs(self):
        return self.__nearby_bombs

    def set_nearby_bombs(self, nearby_bombs: int):
        self.__nearby_bombs = nearby_bombs
