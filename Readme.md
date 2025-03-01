# Maze Solver Project

## Description
This project implements a pathfinding algorithm to solve different mazes. The goal is to create an efficient solution for solving mazes of varying sizes.

## Objectives
- **Short-term Goals**: Generate a PNG representation of the solution and implement the A* algorithm.

## Project Structure
```
Maze-solver-methods/
 │── maze_solver/ 
 │ ├── main.py # Entry point of the program 
 │ ├── maze.py # Maze class for reading and displaying the maze
 │ ├── search.py # Solver class and search algorithms (DFS, BFS, etc.)
 │ ├── node.py # Node class used in search algorithms
 │ ├── frontier.py # Frontier class used to manage nodes to be explored 
 │── data/ # Directory for maze data files (e.g., maze1.txt) 
 │── docs/ # Project documentation (e.g., API.md)
```
## Usage
To run the project, execute:
```bash
python .\maze_solver\main.py .\data\maze_example.txt
```
### Input File:
Make sure you have a valid maze file inside the ```data/``` folder.

The input maze file (`maze_example.txt`) should follow a specific format where:
- `A` represents the start point.
- `B` represents the goal point.
- `#` represents a wall.
- A space (` `) represents a free path.

## Algorithms

### Depth-First Search (DFS)
- Explores as deep as possible along each branch before backtracking.
- Uses a stack (LIFO) to explore nodes.

### Breadth-First Search (BFS)
- Explores all possible moves level by level.
- Uses a queue (FIFO) to explore nodes.
