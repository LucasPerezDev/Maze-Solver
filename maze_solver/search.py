from node import Node
from frontier import StackFrontier
from frontier import QueueFrontier
from frontier import AStarFrontier
from utils import manhattan_distance

class Solver:
    """
    This class is responsible for solving the maze using a search algorithm. 
    It finds a path from the start ('A') to the goal ('B') by exploring 
    states using a frontier, keeping track of explored states to avoid cycles.

    Attributes:
        maze (Maze): The maze to solve.
        num_explored (int): The number of states explored during the solution process.
        explored (set): A set of states that have been explored.
    
    Methods:
        solve(): Solves the maze and stores the solution path in the maze.
    """

    def __init__(self, maze):
        """
        Initializes the solver with the given maze.

        Args:
            maze (Maze): The maze object to solve.
        """
        self.maze = maze  # The maze to solve
        self.num_explored = 0  # Counter for the number of states explored
        self.explored = set()  # Set to store explored states

    def solve(self):
        """
        Solves the maze using a depth-first search algorithm.
        
        The algorithm starts at the start point ('A'), explores the maze by 
        moving through neighboring cells, and backtracks when necessary. 
        If the goal ('B') is found, it stores the actions and the sequence 
        of cells leading to the goal in the maze's solution attribute.

        Raises:
            Exception: If no solution is found, an exception is raised.
        """
        # Start at the 'A' point in the maze and create the initial node
        start = Node(state=self.maze.start, parent=None, action=None)
        frontier = AStarFrontier()  # Use a stack frontier (depth-first search) oa queue frontier (breadth-first search)
        frontier.add(start, start.f)  # Add the start node to the frontier

        # Explore nodes until the frontier is empty
        while True:
            if frontier.empty():  # If the frontier is empty, there's no solution
                raise Exception("No solution")

            # Remove a node from the frontier
            node = frontier.remove()
            self.num_explored += 1  # Increment the number of states explored

            # Check if the goal has been reached
            if node.state == self.maze.goal:
                actions = []  # List to store the actions to take to reach the goal
                cells = []  # List to store the sequence of cells from start to goal
                while node.parent is not None:
                    actions.append(node.action)  # Add the action leading to this state
                    cells.append(node.state)  # Add the current state (cell)
                    node = node.parent  # Move to the parent node
                actions.reverse()  # Reverse the actions to get the path from start to goal
                cells.reverse()  # Reverse the cells to get the path from start to goal
                self.maze.solution = (actions, cells)  # Store the solution in the maze
                return  # Return the solution

            # Add the current state to the explored set
            self.explored.add(node.state)

            # Explore the neighbors of the current state
            for action, state in self.maze.neighbors(node.state):
                # If the state is not in the frontier or already explored, add it to the frontier
                if not frontier.contains_state(state) and state not in self.explored:
                    g = node.g + 1  # Assuming each move has a cost of 1
                    h = manhattan_distance(state, self.maze.goal)
                    child = Node(state=state, parent=node, action=action, g=g, h=h)  # Create a child node
                    frontier.add(child, child.f)  # Add the child node to the frontier
