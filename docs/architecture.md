# Maze Solver Architecture

## Overview
The Maze Solver project is designed to load, validate, and solve mazes using various pathfinding algorithms. It consists of multiple components working together to provide a solution to the maze problem. This document outlines the architecture of the system, explaining the various components and how they interact.

## Project Structure

### 1. `maze_solver/`
This is the main directory where the core program logic is located.
- **`main.py`**: The entry point of the application. It orchestrates the loading of the maze, the selection of the pathfinding algorithm, and outputs the results.
- **`maze.py`**: Contains the `Maze` class which is responsible for reading and representing the maze structure. It also includes methods to validate the maze and print it to the console.

### 2. `data/`
This directory contains maze data files (`.txt` format) that are used to test the solver. Each file represents a different maze layout.
- **`maze1.txt`, `maze2.txt`, ...**: Example maze files that will be used for testing the pathfinding algorithms.

### 3. `docs/`
This directory contains documentation for the project, including technical details, API documentation, and design decisions.
- **`API.md`**: Describes the public API, including classes and methods exposed by the project.
- **`architecture.md`**: This document, outlining the overall architecture and design decisions.
  
## Components

### 1. `Maze Class`
The `Maze` class is the central part of the application. It is responsible for:
- **Loading the maze** from a text file.
- **Validating the maze** to ensure it has one start point ('A') and one goal point ('B').
- **Representing the maze** as a 2D list of walls and open spaces.
- **Printing the maze** to the console.

### 2. Pathfinding Algorithms
In the future, different pathfinding algorithms (such as DFS, BFS, and A*) will be added to solve the maze. The `main.py` will handle the execution of these algorithms. Currently, the project supports:
- **DFS (Depth-First Search)**: A search algorithm that explores as far as possible along each branch before backtracking.
- **BFS (Breadth-First Search)**: A search algorithm that explores all possible paths level by level.

### 3. Main Flow (In `main.py`)
- **Maze Initialization**: The program begins by loading the maze from a file.
- **Pathfinding Execution**: The program will then run one of the pathfinding algorithms to find the shortest path from the start point ('A') to the goal ('B').
- **Output**: Once a solution is found, it will be printed or saved as a visual representation of the maze.

## Data Flow

1. **Input (Maze Data)**: The maze is loaded from a text file located in the `data/` directory.
2. **Processing**:
   - The `Maze` class loads and parses the maze file.
   - Pathfinding algorithms will take over, exploring the maze to find a path from start ('A') to goal ('B').
3. **Output (Maze Solution)**: 
   - The solution is displayed in the console, where the path is marked.
   - Eventually, the program will be extended to output the solution as a graphical image (e.g., PNG).

## Future Enhancements
- **A-star Algorithm**: The A* algorithm will be implemented for better efficiency in finding the shortest path.
- **Graphical Output**: The ability to save the solved maze as an image (PNG) for visualization.
- **GUI**: A graphical user interface could be added for interactive maze-solving.

## Conclusion
The architecture of the Maze Solver project is modular, allowing for the easy addition of new features, such as more algorithms or graphical output. The current system is based on a command-line interface, but future versions may include additional functionality for better user experience.

