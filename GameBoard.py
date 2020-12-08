from typing import List
from Cell import Cell
from random import randint, seed


class GameBoard:
    def __init__(self, size_x: int, size_y: int):
        self.__size_x = size_x
        self.__size_y = size_y

        self.__grid = []

        self.__bombs = self.__size_x  # Serait mieux si c'était une option, ça permetterai de moduler la difficulté
        self.__remaining_bombs = self.__bombs
        
        for x in range(size_x):
            self.__grid.append([])
            for y in range(size_y):
                self.__grid[x].append(Cell())

    def get_grid(self) -> List[List[Cell]]:
        return self.__grid

    def reveal(self, x: int, y: int) -> bool:
        """
        Révèle une cellule
        :param x:
        :param y:
        :return: True if the uncovered cell is a bomb.
        """
        self.__grid[x][y].set_hidden(False)

        if self.__grid[x][y].is_bomb():
            # Révèle le plateau dans son intégralité
            for x in self.__grid:
                for y in x:
                    y.set_hidden(False)
            return True  # Game over
        else:
            self.propagate_from(x, y)

    def toggle_flagged(self, x: int, y: int) -> None:
        self.__grid[x][y].set_flagged(not self.__grid[x][y].is_flagged())
        # MAJ Du compteur de mines
        if self.__grid[x][y].is_bomb():
            if self.__grid[x][y].is_flagged():
                self.__remaining_bombs += 1
            else:
                self.__remaining_bombs -= 1

    def is_flagged(self, x: int, y: int) -> bool:
        return self.__grid[x][y].is_flagged()

    def populate(self) -> None:
        seed()
        nb_bombs = self.__bombs
        for i in range(nb_bombs):
            x = randint(0, self.__size_x - 1)  # Hideuse idée, c'est un coup a finir avec trop peu de mines
            y = randint(0, self.__size_y - 1)
            
            if not self.__grid[x][y].is_bomb():
                self.__grid[x][y].set_bomb(True)
                for x_adjacent in range(-1, 2):  # TODO prettify
                    for y_adjacent in range(-1, 2):
                        if (0 <= x+x_adjacent < self.__size_x) and (0 <= y + y_adjacent < self.__size_y):
                            self.__grid[x+x_adjacent][y+y_adjacent].set_nearby_bombs( self.__grid[x+x_adjacent][y+y_adjacent].get_nearby_bombs() + 1)

    def propagate_from(self, x: int, y: int, r: int = 0) -> None:
        # Au sujet de l'argument r
        # 
        # Python impose une limite au nombre de récusions possibles (990) pour éviter les récursions infinies
        # Cela permet d'afficher une erreur claire au lieu d'attendre que la pile soit pleine et que le programme crash sans explications (comme en C)
        # ==> On limite manuellement le nombre de récursions possibles afin d'éviter de créer des opportunités de crash en augmentant la limite

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

    def get_remaining_bombs(self) -> int:
        """
        Renvoie le nombre de mines qu'il reste a trouver
        :return: le nombre de mines restantes
        """
        return self.__remaining_bombs
