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


def test_a_living_cell_with_two_neighbors_survives():
    """Test that a living cell with two neighbors survives."""
    game = GameOfLife([
        [0, 1, 0],
        [0, 1, 1],
        [0, 0, 0],
    ])
    assert game.get_next_state()[1][1] == 1


def test_a_living_cell_with_bottom_left_neighbor_survives():
    """Test that a living cell with a bottom left neighbor survives."""
    game = GameOfLife([
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1],
    ])
    assert game.get_next_state()[2][1] == 1


def test_a_living_cell_with_less_than_two_neighbors_dies():
    """Test that a living cell with less than two neighbors dies."""
    game = GameOfLife([
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 0],
    ])
    assert game.get_next_state()[0][1] == 0


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


