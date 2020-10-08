from Cell import Cell

class GameBoard:
    def __init__(self, sizeX: int, sizeY: int):
        self.__sizeX = sizeX
        self.__sizeY = sizeY

        self.__grid = []
        
        
        for y in range(sizeY):
            self.__grid.append([])
            for x in range(sizeX):
                self.__grid[y].append(Cell())

    def get_grid(self):
        return self.__grid

    def reveal(self, x: int, y: int):
        self.__grid[x][y].set_hidden(False)

        if self.__grid[x][y].is_bomb():
            pass
            # Game over
        else:
            self.propagateFrom(x, y)

    def toggle_flagged(self, x: int, y: int):
        self.__grid[x][y].set_flagged(not self.__grid[x][y].is_flagged())

    def populate(self):
        #TODO #5 implement populate()
        pass

    def propagateFrom(self, x: int, y: int):
        #TODO #1 implementGameBoard.propagate()
        pass