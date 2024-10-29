# game_of_life.py
from typing import List, Set, Tuple
import copy


class GameOfLife:
    def __init__(self, grid: List[List[int]]):
        """Initialize the game with a grid where 1 represents live cells and 0 represents dead cells."""
        self.grid = grid
    
    def get_next_state(self) -> List[List[int]]:
        """Calculate and return the next state of the grid based on Conway's Game of Life rules."""
        next_state = copy.deepcopy(self.grid)
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self._get_number_of_live_neighbors(row, col) == 2:
                    pass
                elif self._get_number_of_live_neighbors(row, col) == 3:
                    next_state[row][col] = 1
                else:
                    next_state[row][col] = 0
        self.grid = next_state
        return self.grid


    def _get_number_of_live_neighbors(self, row: int, col: int) -> int:
        """Count the number of live neighbors for a given cell."""
        return sum(
            self.grid[n_row][n_col] for n_row, n_col in self._get_neighbors(row, col)
        )
    
    def _get_neighbors(self, row: int, col: int) -> set:
        """Get all valid neighbor coordinates for a given cell."""
        
        neighbors = set()
        for n_row in range(row-1, row+2):
            for n_col in range(col-1, col+2):
                if (n_row, n_col) != (row, col) and self._is_valid_neighbor((n_row, n_col)):
                    neighbors.add((n_row, n_col))
        return neighbors

    def _is_valid_neighbor(self, position: Tuple[int, int]) -> bool:
        """Check if a neighbor is within the grid boundaries."""
        return 0 <= position[0] < len(self.grid) and 0 <= position[1] < len(self.grid[position[0]])

    def run(self, number_of_iterations: int):
        """Run the game for a given number of iterations."""
        for _ in range(number_of_iterations):
            self.get_next_state()
        return self.grid
