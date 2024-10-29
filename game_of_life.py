# game_of_life.py
from typing import List, Set, Tuple
import copy
import pdb
from itertools import product


class GameOfLife:
    def __init__(self, grid: List[List[int]]):
        """Initialize the game with a grid where 1 represents live cells and 0 represents dead cells."""
        self.grid = grid

    def _validate_grid(self):
        """Validate the grid to ensure it is a valid grid."""
        if not self.grid:
            raise ValueError("Grid is empty")

    def _empty_grid(self) -> List[List[int]]:
        """Return an empty grid of the same size as the current grid."""
        return [[0 for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]

    def run(self, iterations: int = 1) -> List[List[int]]:
        """Run the game of life for the grid."""
        for _ in range(iterations):
            next_grid = self.get_next_state()
            self.grid = next_grid
        return next_grid

    def get_next_state(self) -> List[List[int]]:
        """Calculate and return the next state of the grid based on Conway's Game of Life rules."""
        if len(self.grid) == 0:
            return [[]]

        next_grid = self._empty_grid()
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self._get_neighbors(row, col) == 2:
                    next_grid[row][col] = self.grid[row][col]
                elif self.grid[row][col] == 0 and self._get_neighbors(row, col) == 3:
                    next_grid[row][col] = 1
                elif self.grid[row][col] == 1 and self._get_neighbors(row, col) == 3:
                    next_grid[row][col] = 1
                elif self.grid[row][col] == 1 and self._get_neighbors(row, col) >= 4:
                    next_grid[row][col] = 0
        return next_grid

    def _get_neighbors(self, row: int, col: int) -> int:
        """Get all valid neighbor coordinates for a given cell."""
        # Generate all possible combinations of -1, 0, 1 for row and column offsets
        offsets = list(product([-1, 0, 1], repeat=2))
        # Remove (0,0) as it's the cell itself
        offsets.remove((0, 0))
        
        # Generate neighbor coordinates and filter invalid ones
        neighbors = [
            (row + dx, col + dy) 
            for dx, dy in offsets 
            if self._is_valid_neighbor((row + dx, col + dy))
        ]
        
        # Count live neighbors
        return sum(self.grid[n_row][n_col] for n_row, n_col in neighbors)

    def _is_valid_neighbor(self, position: Tuple[int, int]) -> bool:
        """Check if a neighbor is within the grid boundaries."""
        return 0 <= position[0] < len(self.grid) and 0 <= position[1] < len(self.grid[position[0]])
