class Node:
    """
    This class represents a node in the search tree. Each node contains a state,
    a reference to its parent node, and the action taken to reach that state.
    It is primarily used in search algorithms to build the search tree or graph.

    Attributes:
        state (tuple): The current state represented by a tuple (row, column) or any other form
                       depending on the problem context (e.g., maze coordinates).
        parent (Node): A reference to the parent node from which this node was reached.
        action (str): The action taken to reach this node from its parent (e.g., 'up', 'down', 'left', 'right').
        g (float): The cost from the start node to this node.
        h (float): The heuristic cost estimate from this node to the goal.

    Methods:
        __init__(state, parent, action, g, h): Initializes a new node with the provided state, parent, action, g, and h.
    """

    def __init__(self, state, parent=None, action=None, g=0, h=0):
        """
        Initializes a new node with the given state, parent, action, g, and h. This node represents a
        specific state in the search process, and is linked to its parent node to maintain
        the path taken to reach it.

        Args:
            state (tuple): The current state represented by a tuple (row, column) or other context-specific form.
            parent (Node): A reference to the parent node that leads to the current state.
            action (str): The action taken from the parent node's state to the current state.
            g (float): The cost from the start node to this node.
            h (float): The heuristic cost estimate from this node to the goal.
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g
        self.h = h

    @property
    def f(self):
        """
        Returns the total cost (f = g + h) for the node.

        Returns:
            float: The total cost.
        """
        return self.g + self.h