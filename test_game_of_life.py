import pytest

from game_of_life import GameOfLife


def test_empty_grid():
    """Test that empty grids are properly handled."""
    game = GameOfLife([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ])
    assert game.run_and_get_next_state() == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]


def test_living_cell_with_no_neighbors_dies():
    """Test that a single cell with no neighbors dies."""
    game = GameOfLife([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ])
    assert game.run_and_get_next_state()[1][1] == 0
    assert game.run_and_get_next_state() == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]


def test_dead_cell_with_no_neighbors_stays_dead():
    """Test that a dead cell with no neighbors stays dead."""
    game = GameOfLife([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ])
    assert game.run_and_get_next_state()[1][1] == 0
    assert game.run_and_get_next_state() == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

def test_a_living_cell_with_one_neighbors_dies():
    """Test that a living cell with less than two neighbors dies."""
    game = GameOfLife([
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0],
    ])
    assert game.run_and_get_next_state()[1][1] == 0
    assert game.run_and_get_next_state() == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

def test_a_dead_cell_with_one_neighbors_stays_dead():
    """Test that a dead cell with less than two neighbors stays dead."""
    game = GameOfLife([
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 0],
    ])
    assert game.run_and_get_next_state()[1][1] == 0
    assert game.run_and_get_next_state() == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

def test_a_living_cell_with_two_neighbors_survives():
    """Test that a living cell with two neighbors survives."""
    game = GameOfLife([
        [1, 0, 0],
        [0, 1, 1],
        [0, 0, 0],
    ])
    assert game.run_and_get_next_state()[1][1] == 1


def test_a_dead_cell_with_two_neighbors_stays_dead():
    """Test that a dead cell with two neighbors stays dead."""
    game = GameOfLife([
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 1],
    ])
    assert game.run_and_get_next_state()[1][1] == 0

def test_a_living_cell_with_three_neighbors_survives():
    """Test that a living cell with three neighbors survives."""
    game = GameOfLife([
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
    ])
    assert game.run_and_get_next_state()[1][1] == 1

def test_a_dead_cell_with_three_neighbors_becomes_alive():
    """Test that a dead cell with three neighbors becomes alive."""
    game = GameOfLife([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
    ])
    assert game.run_and_get_next_state()[1][1] == 1

def test_living_cell_with_more_than_three_neighbors_dies():
    """Test that a living cell with more than three neighbors dies."""
    game = GameOfLife([
        [1, 1, 0],
        [0, 1, 1],
        [0, 1, 0],
    ])
    assert game.run_and_get_next_state()[1][1] == 0

def test_a_dead_cell_with_more_than_three_neighbors_stays_dead():
    """Test that a dead cell with more than three neighbors stays dead."""
    game = GameOfLife([
        [1, 1, 0],
        [0, 0, 1],
        [0, 1, 0],
    ])
    assert game.run_and_get_next_state()[1][1] == 0

def test_two_iterations():
    """Test that the game state is correctly updated after two iterations."""
    game = GameOfLife([
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ])
    game.run_and_get_next_state()
    assert game.run_and_get_next_state() == [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]


# def test_a_living_cell_with_bottom_left_neighbor_survives():
#     """Test that a living cell with a bottom left neighbor survives."""
#     game = GameOfLife([
#         [0, 0, 0],
#         [0, 0, 0],
#         [1, 1, 1],
#     ])
#     assert game.run_and_get_next_state()[2][1] == 1





