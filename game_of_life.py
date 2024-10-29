from typing import List, Set, Tuple
import copy
import pdb
from itertools import product
from abc import ABC, abstractmethod


class Cell(ABC):
    @abstractmethod
    def next_state(self, neighbors: int) -> int:
        pass

class CellFactory:
    @staticmethod
    def get_cell(state: int) -> Cell:
        return LiveCell() if state == 1 else DeadCell()

class DeadCell(Cell):
    def next_state(self, neighbors: int) -> int:
        return 1 if neighbors == 3 else 0

class LiveCell(Cell):
    def next_state(self, neighbors: int) -> int:
        return 1 if neighbors in [2, 3] else 0

class Grid:
    def __init__(self, data: List[List[int]]):
        self._validate(data)
        self.data = data

    def _validate(self, data: List[List[int]]) -> None:
        """Validate the grid to ensure it is a valid grid."""
        if not data:
            return [[]]

    def create_empty_grid(self) -> 'Grid':
        """Return an empty grid of the same size as the current grid."""
        return Grid([[0 for _ in range(len(self.data[0]))] for _ in range(len(self.data))])

    def get_neighbors(self, row: int, col: int) -> int:
        """Get all valid neighbor coordinates for a given cell."""
        raw_neighbors = [
            (row+1,col),
            (row-1,col),
            (row,col+1),
            (row,col-1),
            (row+1,col+1),
            (row+1,col-1),
            (row-1,col+1),
            (row-1,col-1)
        ]

        neighbors = [(row,col) if self._is_valid_neighbor((row, col)) else None for row, col in raw_neighbors]
        neighbors = [n for n in neighbors if n is not None]
        
        def _count():
            count = 0
            for n_row, n_col in neighbors:
                count += self.data[n_row][n_col]
            return count
        
        return _count()

    def _is_valid_neighbor(self, position: Tuple[int, int]) -> bool:
        """Check if a neighbor is within the grid boundaries."""
        return 0 <= position[0] < len(self.data) and 0 <= position[1] < len(self.data[position[0]])

class GameOfLife:
    def __init__(self, grid: List[List[int]]):
        """Initialize the game with a grid where 1 represents live cells and 0 represents dead cells."""
        self.grid = Grid(grid)

    def run(self, iterations: int = 1) -> List[List[int]]:
        """Run the game of life for the grid."""
        for _ in range(iterations):
            next_grid = self.get_next_state()
            self.grid = next_grid
        return next_grid.data

    def get_next_state(self) -> Grid:
        """Calculate and return the next state of the grid based on Conway's Game of Life rules."""
        if len(self.grid.data) == 0:
            return Grid([[]])

        next_grid = self.grid.create_empty_grid()
        for row in range(len(self.grid.data)):
            for col in range(len(self.grid.data[row])):
                cell = CellFactory.get_cell(self.grid.data[row][col])
                neighbors = self.grid.get_neighbors(row, col)
                next_grid.data[row][col] = cell.next_state(neighbors)
        return next_grid
