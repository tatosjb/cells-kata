# game_of_life.py
from typing import List, Set, Tuple
import copy


class GameOfLife:
    def __init__(self, grid: List[List[int]]):
        """Initialize the game with a grid where 1 represents live cells and 0 represents dead cells."""
        self.grid = grid

    def get_next_state(self) -> List[List[int]]:
        """Calculate and return the next state of the grid based on Conway's Game of Life rules."""
        # TODO: Implement this method

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                self.grid[row][col] = 1 if self._get_neighbors(row, col) == 2 else 0

        return self.grid

    # def count_live_neighbors(self, row: int, col: int) -> int:
    #     """Count the number of live neighbors for a given cell."""
    #     # TODO: Implement this method
    #     pass

    def _get_neighbors(self, row: int, col: int) -> int:
        """Get all valid neighbor coordinates for a given cell."""
        # TODO: Implement this method

        from itertools import product

        possible_neighbors = list(set([row, col, row - 1, col - 1, row + 1, col + 1]))
        neighbors = list(filter(self._is_valid_neighbor, product(possible_neighbors, repeat=2)))
        neighbors.remove((row, col))

        return sum(
            self.grid[n_row][n_col] for n_row, n_col in neighbors
        )

    def _is_valid_neighbor(self, position: Tuple[int, int]) -> bool:
        """Check if a neighbor is within the grid boundaries."""
        return 0 <= position[0] < len(self.grid) and 0 <= position[1] < len(self.grid[position[0]])
