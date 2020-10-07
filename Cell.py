class Cell:
    def __init__(self):
        self.__flagged = False
        self.__bomb = False
        self.__hidden = False
        self.__nearby_bombs = 0

    def is_bomb(self):
        return self.bomb

    def set_bomb(self, bomb: bool):
        self.bomb = bomb

    def is_flagged(self):
        return self.flagged

    def set_flagged(self, flagged: bool):
        self.flagged = flagged

    def is_hidden(self):
        return self.hidden

    def set_hidden(self, hidden: bool):
        self.hidden = hidden

    def get_nearby_bombs(self):
        return self.nearby_bombs

    def set_nearby_bombs(self, nearby_bombs: int):
        self.nearby_bombs = nearby_bombs
