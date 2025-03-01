import os
import sys
from maze import Maze
from search import Solver
from visualizer import MazeVisualizer

# Example usage: python .\maze_solver\main.py .\data\maze2.txt

def main():
    """
    Main function to load a maze from a file, solve it using the Solver class, 
    and print the maze before and after solving. 

    The function expects a command-line argument specifying the path to the maze file.

    Exits with an error message if the correct number of arguments is not provided.
    """
    # Check if the correct number of arguments is passed (should be 2 arguments: the script and the maze file)
    if len(sys.argv) != 2:
        sys.exit("Usage: python main.py maze.txt")  # If not, show usage and exit.

    # Load the maze from the file provided in the command-line argument.
    maze = Maze(sys.argv[1])  
    maze.print()  # Print the maze layout before solving

    print("Solving...")  # Indicate the solving process is starting
    
    # Create a Solver object to solve the maze.
    solver = Solver(maze)  
    solver.solve()  # Solve the maze using the solver
    
    # Print the number of states explored during the solving process.
    print("States Explored:", solver.num_explored)
    
    # Print the maze layout again, this time with the solution path.
    maze.print()  # Print the solution path on the maze

     # Create the 'images' directory if it does not exist
    if not os.path.exists('images'):
        os.makedirs('images')

    # Visualize and save the maze with the solution and explored cells
    visualizer = MazeVisualizer(maze, solution=maze.solution, explored=solver.explored)
    visualizer.draw_maze(os.path.join('images', "maze.png"), show_solution=True, show_explored=True)



# Ensure that the main function is executed only if this script is run directly.
if __name__ == "__main__":
    main()
