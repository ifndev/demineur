from typing import List
from Cell import Cell
from random import randint, seed


class GameBoard:
    def __init__(self, size_x: int, size_y: int):
        self.__size_x = size_x
        self.__size_y = size_y

        self.__grid = []
        
        for x in range(size_x):
            self.__grid.append([])
            for y in range(size_y):
                self.__grid[x].append(Cell())

    def get_grid(self) -> List[List[Cell]]:
        return self.__grid

    def reveal(self, x: int, y: int) -> bool:
        self.__grid[x][y].set_hidden(False)

        if self.__grid[x][y].is_bomb():
            for x in self.__grid:
                for y in x:
                    y.set_hidden(False)
            return True # Game over
        else:
            self.propagate_from(x, y)

    def toggle_flagged(self, x: int, y: int) -> None:
        self.__grid[x][y].set_flagged(not self.__grid[x][y].is_flagged())

    def populate(self) -> None:
        seed()
        nb_bombs = self.__size_x # This should be an option
        for i in range(nb_bombs):
            x = randint(0, self.__size_x - 1) # Bad idea, we can end up with too less bombs
            y = randint(0, self.__size_y - 1)
            
            if not self.__grid[x][y].is_bomb():
                self.__grid[x][y].set_bomb(True)
                for x_adjacent in range(-1, 2):  # TODO prettify
                    for y_adjacent in range(-1, 2):
                        if (0 <= x+x_adjacent < self.__size_x) and (0 <= y + y_adjacent < self.__size_y):
                            self.__grid[x+x_adjacent][y+y_adjacent].set_nearby_bombs( self.__grid[x+x_adjacent][y+y_adjacent].get_nearby_bombs() + 1)

    def propagate_from(self, x: int, y: int, r: int = 0) -> None:
        # About the "r" optional argument
        # 
        # In order to prevent a stack overflow, python limits recursion depth to 990
        # Circumventing would not be smart and could lead to the game hanging on propagate
        # on really large boards.
        #
        # ==> We manually clamp the depth to a fixed limit, revealing only part of the board

        if self.__grid[x][y].get_nearby_bombs() == 0 and r < 200:
                                                         # Here
            self.__grid[x][y].set_hidden(False)
            for x_adjacent in range(-1, 2):
                for y_adjacent in range(-1, 2):
                    if not (x==0 and y==0) and (0 <= x+x_adjacent < self.__size_x) and (0 <= y + y_adjacent < self.__size_y):
                        if self.__grid[x+x_adjacent][y+y_adjacent].is_hidden():
                            self.propagate_from(x + x_adjacent, y + y_adjacent, r + 1)
        elif not self.__grid[x][y].is_bomb():
            self.__grid[x][y].set_hidden(False)
