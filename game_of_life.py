# game_of_life.py
from typing import List, Set, Tuple
import copy


class GameOfLife:
    def __init__(self, grid: List[List[int]]):
        """Initialize the game with a grid where 1 represents live cells and 0 represents dead cells."""


    def get_next_state(self) -> List[List[int]]:
        """Calculate and return the next state of the grid based on Conway's Game of Life rules."""
        # TODO: Implement this method
        return [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

    # def count_live_neighbors(self, row: int, col: int) -> int:
    #     """Count the number of live neighbors for a given cell."""
    #     # TODO: Implement this method
    #     pass

    # def get_neighbors(self, row: int, col: int) -> Set[Tuple[int, int]]:
    #     """Get all valid neighbor coordinates for a given cell."""
    #     # TODO: Implement this method
    #     pass