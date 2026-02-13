from utils.distances import manhattan_distance

def test_manhattan():
    assert manhattan_distance((0, 0), (0, 0)) == 0
    assert manhattan_distance((0, 0), (1, 1)) == 2
    assert manhattan_distance((0, 0), (1, 0)) == 1
    assert manhattan_distance((0, 0), (0, 1)) == 1
    assert manhattan_distance((0, 0), (-1, 0)) == 1
    assert manhattan_distance((0, 0), (0, -1)) == 1
    assert manhattan_distance((0, 0), (-1, -1)) == 2
    assert manhattan_distance((0, 0), (1, -1)) == 2
    assert manhattan_distance((0, 0), (-1, 1)) == 2
