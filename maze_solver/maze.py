from search import Solver

class Maze():
    """
    This class represents a maze and provides functionality to load, 
    validate, and print the maze. The maze is loaded from a text file 
    where 'A' represents the start point, 'B' represents the goal, 
    walls are represented by any non-space character, and spaces represent 
    open paths.

    Attributes:
        start (tuple): A tuple representing the coordinates of the start point (row, column).
        goal (tuple): A tuple representing the coordinates of the goal point (row, column).
        height (int): The height (number of rows) of the maze.
        width (int): The width (number of columns) of the maze.
        walls (list): A 2D list representing the maze layout. 
                      Each element is either `True` (wall) or `False` (open space).
        solution (list): A list representing the solution path, if available, containing coordinates of the path.
    
    Methods:
        __init__(filename): Initializes the maze by reading the file, validating the start and goal points,
                             and determining the maze's dimensions and layout.
        print(): Prints the maze to the console with 'A' for the start point, 
                 'B' for the goal, and '█' for walls.
        neighbors(state): Returns a list of possible neighboring states from the current position, 
                          considering the maze boundaries and open spaces.
    """

    def __init__(self, filename):
        """
        Initializes the maze by reading the contents of a file, validating the start ('A') and goal ('B') points,
        and creating the internal representation of the maze's walls and open spaces.

        Args:
            filename (str): The path to the maze file.
        
        Raises:
            Exception: If the maze file does not contain exactly one start ('A') and one goal ('B') point.
        """

        # Read the file content
        with open(filename) as f:
            contents = f.read()

        # Validate the presence of exactly one start ('A') and one goal ('B')
        if contents.count("A") != 1:
            raise Exception("Maze must have exactly one start point ('A').")
        if contents.count("B") != 1:
            raise Exception("Maze must have exactly one goal point ('B').")

        # Split contents into lines and determine maze dimensions
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Create an internal representation of the maze (walls and open spaces)
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    # Mark the start and goal positions as open space
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    # Mark walls and open paths
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    # Handle any index errors caused by uneven row lengths
                    row.append(False)
            self.walls.append(row)
        self.solution = None 

    def print(self):
        """
        Prints the maze to the console in a visually formatted manner. 
        The start point ('A') and goal point ('B') are displayed at their 
        respective positions, walls are represented by '█', and open spaces 
        are represented by spaces. If a solution exists, it is represented by '*'.
        """
        solution = self.solution[1] if self.solution is not None else None  # Get the solution path if it exists
        print()  # Print a blank line before starting
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")  # Wall
                elif (i, j) == self.start:
                    print("A", end="")  # Start point
                elif (i, j) == self.goal:
                    print("B", end="")  # Goal point
                elif solution is not None and (i, j) in solution:
                    print("*", end="")  # If part of the solution path, display '*'
                else:
                    print(" ", end="")  # Empty space
            print()  # New line at the end of each row
        print()  # Blank line after the maze is printed

    def neighbors(self, state):
        """
        Given a state (row, col), returns a list of possible neighboring states 
        considering the boundaries of the maze and walls. The neighbors are 
        valid if they are within the maze dimensions and not blocked by a wall.

        Args:
            state (tuple): A tuple representing the current state (row, column).

        Returns:
            list: A list of tuples containing valid neighboring actions and states.
                  Each tuple is of the form (action, (row, col)).
                  Valid actions are "up", "down", "left", and "right".
        """
        row, col = state  # Unpack the current state (row, col)
        # List of possible moves (actions) and their resulting positions
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []  # List to store valid neighboring states
        for action, (r, c) in candidates:
            # Check if the neighbor is within bounds and not a wall
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))  # Add valid neighbors to the result list
        return result