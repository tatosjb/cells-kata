from game_of_life import GameOfLife

""""
A living cell with less than two neighbors dies. ok
A living cell with two or three neighbors survives. ok
A living cell with more than three neighbors dies. ok
A dead cell with exactly three neighbors becomes alive. ok
"""
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

def test_a_living_cell_with_less_than_two_neighbors_dies():
    """Test that a living cell with less than two neighbors dies."""
    game = GameOfLife([
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0],
    ])
    assert game.get_next_state()[1][1] == 0

def test_a_living_cell_with_two_or_three_neighbors_survives():
    """Test that a living cell with two or three neighbors survives."""
    game = GameOfLife([
        [0, 1, 0],
        [0, 1, 1],
        [0, 0, 0],
    ])
    assert game.get_next_state()[1][1] == 1

def test_a_living_cell_with_more_than_three_neighbors_dies():
    """A living cell with more than three neighbors dies."""
    game = GameOfLife([
        [1, 1, 1],
        [0, 1, 1],
        [0, 0, 0],
    ])
    assert game.get_next_state()[1][1] == 0

def test_a_dead_cell_with_exactly_three_neighbors_survives():
    """A living cell with more than three neighbors dies."""
    game = GameOfLife([
        [0, 1, 1],
        [0, 0, 1],
        [0, 0, 0],
    ])
    assert game.get_next_state()[1][1] == 1

def test_get_neighbors_for_the_middle_cell():
    """A living cell with more than three neighbors dies."""
    game = GameOfLife([
        # randomize the surrounds of the 1,1 cell
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ])
    assert game._get_neighbors(1,1) == {
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 2), (2, 0),
        (2, 1), (2, 2)
    }

def test_get_neighbors_for_the_corner_cell():
    """A living cell with more than three neighbors dies."""
    game = GameOfLife([
        # randomize the surrounds of the 1,1 cell
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ])
    assert game._get_neighbors(2,2) == {
        (1,1), (1,2), (2,1)
    }

def test_get_neighbors_for_the_edge_cell():
    """A living cell with more than three neighbors dies."""
    game = GameOfLife([
        # randomize the surrounds of the 1,1 cell
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ])
    print(game._get_neighbors(1,2))
    assert game._get_neighbors(1,2) == {
        (1,1), (2,2), (0,2), (0,1), (2,1)
    }

def test_dead_cell_with_two_neighbors():
    """A dead cell with two neighbors remains dead."""
    game = GameOfLife([
        [0, 1, 1],
        [0, 0, 0],
        [0, 0, 0],
    ])
    assert game.get_next_state()[1][1] == 0

def test_run_two_iterations():
    """Test that the game can run for two iterations."""
    game = GameOfLife([
        [0, 1, 1],
        [0, 0, 0],
        [0, 0, 0],
    ])
    assert game.run(2) == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

def test_5_by_5_grid():
    game = GameOfLife([
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [1, 1, 1, 1],   
    ])
    assert game.get_next_state() == [
        [0, 1, 1, 0],
        [1, 0, 0, 0],
        [1, 0, 1, 1],
    ]        
