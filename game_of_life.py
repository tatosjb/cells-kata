# game_of_life.py
from typing import List, Set, Tuple
import copy


class GameOfLife:
    def __init__(self, grid: List[List[int]]):
        """Initialize the game with a grid where 1 represents live cells and 0 represents dead cells."""
        self.grid = grid

    def run_and_get_next_state(self) -> List[List[int]]:
        """Calculate and return the next state of the grid based on Conway's Game of Life rules."""
        # TODO: Implement this method

        # Create a copy of the grid to store the next state
        next_state = copy.deepcopy(self.grid)

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self._get_neighbors(row, col) == 3:
                    next_state[row][col] = 1
                elif self._get_neighbors(row, col) == 2 and self.grid[row][col] == 1:
                    next_state[row][col] = 1
                else:
                    next_state[row][col] = 0

        return next_state

    # def count_live_neighbors(self, row: int, col: int) -> int:
    #     """Count the number of live neighbors for a given cell."""
    #     # TODO: Implement this method
    #     pass

    def _get_neighbors(self, row: int, col: int) -> int:
        """Get all valid neighbor coordinates for a given cell."""
        # TODO: Implement this method

        alive_count = 0
        for dx in range(row - 1, row + 2):
            for dy in range(col - 1, col + 2):
                if self._is_valid_neighbor((dx, dy)) and (dx, dy) != (row, col):
                    alive_count += self.grid[dx][dy]

        return alive_count

    def _is_valid_neighbor(self, position: Tuple[int, int]) -> bool:
        """Check if a neighbor is within the grid boundaries."""
        return 0 <= position[0] < len(self.grid) and 0 <= position[1] < len(self.grid[position[0]])
