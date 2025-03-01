def manhattan_distance(state1, state2):
    """
    Calculates the Manhattan distance between two states.

    Args:
        state1 (tuple): The first state (x1, y1).
        state2 (tuple): The second state (x2, y2).

    Returns:
        float: The Manhattan distance between the two states.
    """
    x1, y1 = state1
    x2, y2 = state2
    return abs(x1 - x2) + abs(y1 - y2)