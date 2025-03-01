import sys
from maze import Maze
# python .\maze_solver\main.py .\data\maze2.txt

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python main.py maze.txt") # python .\maze_solver\main.py .\data\maze2.txt
maze = Maze(sys.argv[1])  
maze.print()  # Print the maze
