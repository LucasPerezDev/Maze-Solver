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
    
    Methods:
        __init__(filename): Initializes the maze by reading the file, validating the start and goal points,
                             and determining the maze's dimensions and layout.
        print(): Prints the maze to the console with 'A' for the start point, 
                 'B' for the goal, and '█' for walls.
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

    def print(self):
        """
        Prints the maze to the console in a visually formatted manner. 
        The start point ('A') and goal point ('B') are displayed at their 
        respective positions, walls are represented by '█', and open spaces 
        are represented by spaces.
        """
        print()  # Print a blank line before starting
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")  # Wall
                elif (i, j) == self.start:
                    print("A", end="")  # Start point
                elif (i, j) == self.goal:
                    print("B", end="")  # Goal point
                else:
                    print(" ", end="")  # Empty space
            print()  # New line at the end of each row
        print()  # Blank line after the maze is printed
