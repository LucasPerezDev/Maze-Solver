class Node():
    """
    This class represents a node in the search tree. Each node contains a state,
    a reference to its parent node, and the action taken to reach that state.
    It is primarily used in search algorithms to build the search tree or graph.

    Attributes:
        state (tuple): The current state represented by a tuple (row, column) or any other form
                       depending on the problem context (e.g., maze coordinates).
        parent (Node): A reference to the parent node from which this node was reached.
        action (str): The action taken to reach this node from its parent (e.g., 'up', 'down', 'left', 'right').

    Methods:
        __init__(state, parent, action): Initializes a new node with the provided state, parent, and action.
    """

    def __init__(self, state, parent, action):
        """
        Initializes a new node with the given state, parent, and action. This node represents a
        specific state in the search process, and is linked to its parent node to maintain
        the path taken to reach it.

        Args:
            state (tuple): The current state represented by a tuple (row, column) or other context-specific form.
            parent (Node): A reference to the parent node that leads to the current state.
            action (str): The action taken from the parent node's state to the current state.

        Example:
            node = Node(state=(1, 2), parent=parent_node, action="right")
        """
        self.state = state  # The current state of the node (e.g., coordinates in the maze)
        self.parent = parent  # The parent node that leads to this node
        self.action = action  # The action taken to reach this node (e.g., "up", "down", etc.)
