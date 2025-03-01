from PIL import Image, ImageDraw

class MazeVisualizer:
    """
    A class responsible for visualizing a maze, its solution, and explored cells.
    Uses PIL (Python Imaging Library) to create a visual representation of the maze.
    """

    def __init__(self, maze, solution=None, explored=None):
        """
        Initializes the MazeVisualizer with the maze, solution, and explored cells.

        Parameters:
        maze (Maze): The maze to be visualized.
        solution (tuple): The solution to the maze, consisting of a list of actions and a list of cells. Defaults to None.
        explored (set): A set of explored cells during the search process. Defaults to an empty set if None.
        """
        # Store passed parameters
        self.maze = maze
        self.solution = solution
        # Assign an empty set if 'explored' is not provided
        self.explored = explored if explored is not None else set()
        # Cell size and border thickness
        self.cell_size = 50
        self.cell_border = 2

    def draw_maze(self, filename, show_solution=True, show_explored=False):
        """
        Draws the maze to an image file, optionally displaying the solution and explored cells.

        Parameters:
        filename (str): The name of the output image file.
        show_solution (bool): Whether to show the solution path on the maze. Defaults to True.
        show_explored (bool): Whether to show the explored cells. Defaults to False.
        """
        # Calculate the image dimensions based on the maze size
        width = self.maze.width * self.cell_size
        height = self.maze.height * self.cell_size
        
        # Create a new image with a black background
        img = Image.new("RGBA", (width, height), "black")
        draw = ImageDraw.Draw(img)

        # Iterate through each cell in the maze
        for i, row in enumerate(self.maze.walls):
            for j, col in enumerate(row):
                if col:
                    # Walls are drawn in grey
                    fill = (40, 40, 40)
                elif (i, j) == self.maze.start:
                    # Start (A) is drawn in red
                    fill = (255, 0, 0)
                elif (i, j) == self.maze.goal:
                    # Goal (B) is drawn in green
                    fill = (0, 171, 28)
                # If a solution exists and solution cells need to be displayed
                elif self.solution is not None and show_solution and (i, j) in self.solution[1]:
                    fill = (220, 235, 113)  # Gold color for solution cells
                # If explored cells need to be displayed
                elif show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)  # Red for explored cells
                else:
                    # Empty spaces are drawn in light grey
                    fill = (237, 240, 252)

                # Draw the rectangle for each cell
                draw.rectangle(
                    [
                        (j * self.cell_size + self.cell_border, i * self.cell_size + self.cell_border),
                        ((j + 1) * self.cell_size - self.cell_border, (i + 1) * self.cell_size - self.cell_border)
                    ],
                    fill=fill
                )
        
        # Save the generated image with the provided filename
        img.save(filename)
