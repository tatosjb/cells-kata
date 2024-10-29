import pytest

from game_of_life import GameOfLife


def test_empty_grid():
    """Test that empty grids are properly handled."""
    game = GameOfLife([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ])
    assert game.get_next_state() == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]




# def test_single_cell_with_no_neighbors_dies():
#     """Test that a single cell with no neighbors dies."""
#     game = GameOfLife([
#         [0, 0, 0],
#         [0, 1, 0],
#         [0, 0, 0],
#     ])
#     assert game.get_next_state() == [
#         [0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0],
#     ]


