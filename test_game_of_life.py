import pytest

from game_of_life import GameOfLife


def test_empty_grid():
    """Test that empty grids are properly handled."""
    game = GameOfLife([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ])
    assert game.run() == [
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
    assert game.run()[1][1] == 1


def test_a_living_cell_with_bottom_left_neighbor_survives():
    """Test that a living cell with a bottom left neighbor survives."""
    game = GameOfLife([
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1],
    ])
    assert game.run()[2][1] == 1


def test_a_living_cell_with_less_than_two_neighbors_dies():
    """Test that a living cell with less than two neighbors dies."""
    game = GameOfLife([
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 0],
    ])
    assert game.run()[0][1] == 0


def test_a_living_cell_with_three_neighbors_survives():
    """Test that a living cell with less than two neighbors dies."""
    game = GameOfLife([
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0],
    ])
    assert game.run()[1][1] == 1


def test_a_living_cell_with_two_neighbors_survives_whole_matrix():
    """Test that a living cell with less than two neighbors dies."""
    game = GameOfLife([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ])
    assert game.run() == [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ]


def test_a_dead_cell_with_three_neighbors_becomes_alive():
    """Test that a dead cell with three neighbors becomes alive."""
    game = GameOfLife([
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0],
    ])
    assert game.run() == [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]


def test_a_living_cell_with_four_neighbors_dies():
    """Test that a living cell with four neighbors dies."""
    game = GameOfLife([
        [0, 1, 0],
        [1, 1, 0],
        [1, 1, 0],
    ])
    assert game.run() == [
        [1, 1, 0],
        [0, 0, 1],
        [1, 1, 0],
    ]


def test_a_living_cell_with_more_than_four_neighbors_dies():
    """Test that a living cell with more than four neighbors dies."""
    game = GameOfLife([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ])
    assert game.run()[1][1] == 0
    game = GameOfLife([
        [1, 1, 1],
        [0, 1, 1],
        [0, 0, 1],
    ])
    assert game.run()[1][1] == 0
    game = GameOfLife([
        [1, 1, 1],
        [0, 1, 1],
        [0, 1, 1],
    ])
    assert game.run()[1][1] == 0


def test_assert_empty_grid():
    game = GameOfLife([])
    assert game.run() == [[]]


def test_multiple_runs():
    game = GameOfLife([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ])
    assert game.run(2) == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

def test_10_rounds():
    game = GameOfLife([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ])
    assert game.run(10) == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
