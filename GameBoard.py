from typing import List
from Cell import Cell
from random import randint, seed

class GameBoard:
    def __init__(self, sizeX: int, sizeY: int):
        self.__sizeX = sizeX
        self.__sizeY = sizeY

        self.__grid = []
        
        for y in range(sizeY):
            self.__grid.append([])
            for x in range(sizeX):
                self.__grid[y].append(Cell())

    def get_grid(self) -> List[List[Cell]]:
        return self.__grid

    def reveal(self, x: int, y: int) -> bool:
        self.__grid[x][y].set_hidden(False)

        if self.__grid[x][y].is_bomb():
            pass
            # Game over
        else:
            self.propagateFrom(x, y)

    def toggle_flagged(self, x: int, y: int) -> None:
        self.__grid[x][y].set_flagged(not self.__grid[x][y].is_flagged())

    def populate(self) -> None:
        seed()
        nb_bombs = self.__sizeX # This should be an option
        for i in range(nb_bombs):
            x = randint(0, self.__sizeX-1) # Bad idea, we can end up with too less bombs
            y = randint(0, self.__sizeY-1)
            
            if not self.__grid[x][y].is_bomb():
                self.__grid[x][y].set_bomb(True)
                for xAdgacent in range(-1, 2): # TODO prettify
                    for yAdgacent in range(-1, 2):
                        if (0 <= x+xAdgacent < self.__sizeX) and (0 <= y+yAdgacent < self.__sizeY):
                            self.__grid[x+xAdgacent][y+yAdgacent].set_nearby_bombs( self.__grid[x+xAdgacent][y+yAdgacent].get_nearby_bombs() + 1)


    def propagateFrom(self, x: int, y: int) -> None:
        if self.__grid[x][y].get_nearby_bombs() == 0:
            self.__grid[x][y].set_hidden(False)
            for xAdgacent in range(-1, 2):
                for yAdgacent in range(-1, 2):
                    if not (x==0 and y==0) and (0 <= x+xAdgacent < self.__sizeX) and (0 <= y+yAdgacent < self.__sizeY):
                        if self.__grid[x+xAdgacent][y+yAdgacent].is_hidden():
                            self.propagateFrom(x+xAdgacent, y+yAdgacent)
        elif not self.__grid[x][y].is_bomb():
            self.__grid[x][y].set_hidden(False)
        pass
