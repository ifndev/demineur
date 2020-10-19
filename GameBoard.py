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
            self.__grid[x][y].set_bomb(True)

            # Needs nearby bombs counting


    def propagateFrom(self, x: int, y: int) -> None:
        #TODO #1 implementGameBoard.propagate()
        pass
