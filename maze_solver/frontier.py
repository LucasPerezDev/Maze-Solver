from node import Node

class Frontier():
    """
    A base class representing a frontier in a search algorithm. The frontier is the collection of 
    nodes that need to be explored. It provides basic operations such as adding a node, checking 
    if a state exists in the frontier, and checking if the frontier is empty.

    Attributes:
        frontier (list): A list that holds nodes (objects of the Node class) to be explored.

    Methods:
        add(node): Adds a new node to the frontier.
        contains_state(state): Checks if a node with the given state is in the frontier.
        empty(): Returns True if the frontier is empty, otherwise False.
    """

    def __init__(self):
        """
        Initializes the frontier as an empty list.

        Example:
            frontier = Frontier()
        """
        self.frontier = []  # The frontier is initialized as an empty list.

    def add(self, node):
        """
        Adds a node to the frontier.

        Args:
            node (Node): The node to be added to the frontier.

        Example:
            frontier.add(Node(state=(0, 0), parent=None, action="start"))
        """
        self.frontier.append(node)  # Adds the node to the list of frontier nodes.

    def contains_state(self, state):
        """
        Checks if the frontier contains a node with a given state.

        Args:
            state (tuple): The state to check for in the frontier.

        Returns:
            bool: True if the frontier contains a node with the state, False otherwise.
        
        Example:
            frontier.contains_state((1, 2))
        """
        return any(node.state == state for node in self.frontier)  # Checks for the state in the frontier.

    def empty(self):
        """
        Checks if the frontier is empty.

        Returns:
            bool: True if the frontier is empty, False otherwise.

        Example:
            frontier.empty()  # Returns True if no nodes are in the frontier.
        """
        return len(self.frontier) == 0  # Returns True if the frontier has no nodes.


class StackFrontier(Frontier):
    """
    A subclass of Frontier that implements a stack-based frontier, 
    where nodes are added and removed in a Last In, First Out (LIFO) manner.

    Methods:
        remove(): Removes and returns the last node added to the frontier.
    """

    def remove(self):
        """
        Removes and returns the last node added to the frontier (LIFO order).

        Returns:
            Node: The last node in the frontier.

        Raises:
            Exception: If the frontier is empty, an exception is raised.
        
        Example:
            node = stack_frontier.remove()
        """
        if self.empty():
            raise Exception("empty frontier")  # Raises an error if the frontier is empty.
        else:
            node = self.frontier[-1]  # Gets the last node.
            self.frontier = self.frontier[:-1]  # Removes the last node from the frontier.
            return node  # Returns the node.


class QueueFrontier(Frontier):
    """
    A subclass of Frontier that implements a queue-based frontier,
    where nodes are added and removed in a First In, First Out (FIFO) manner.

    Methods:
        remove(): Removes and returns the first node added to the frontier.
    """

    def remove(self):
        """
        Removes and returns the first node added to the frontier (FIFO order).

        Returns:
            Node: The first node in the frontier.

        Raises:
            Exception: If the frontier is empty, an exception is raised.
        
        Example:
            node = queue_frontier.remove()
        """
        if self.empty():
            raise Exception("empty frontier")  # Raises an error if the frontier is empty.
        else:
            node = self.frontier[0]  # Gets the first node.
            self.frontier = self.frontier[1:]  # Removes the first node from the frontier.
            return node  # Returns the node.
