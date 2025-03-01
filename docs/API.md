# Maze Solver API Documentation

## Overview
This document provides an overview of the Maze Solver API, detailing the classes and methods used in the project. The classes are designed to load a maze from a file, solve it using various pathfinding algorithms, and visualize the solution.

## Class: `Maze`

### Description
The `Maze` class provides functionality to load, validate, and print a maze from a text file. The maze must have exactly one start point ('A') and one goal point ('B'). The maze layout is represented by a 2D list where walls are marked as `True` and open paths are marked as `False`.

### Attributes

- **`start` (tuple)**: Coordinates of the start point `(row, column)`.
- **`goal` (tuple)**: Coordinates of the goal point `(row, column)`.
- **`height` (int)**: The number of rows in the maze.
- **`width` (int)**: The number of columns in the maze.
- **`walls` (list)**: A 2D list representing the maze layout. Each element is `True` for a wall and `False` for an open path.
- **`solution` (list)**: A list containing two lists, one for the actions to reach the goal and one for the cells visited on the solution path.

### Methods

#### `__init__(filename)`
```python
def __init__(self, filename)
```
- **Parameters**:
  - `filename` (str): Path to the maze file.
- **Description**: 
  - Reads the contents of the maze file.
  - Validates that the file contains exactly one start point ('A') and one goal point ('B').
  - Determines the maze's dimensions (`height` and `width`).
  - Constructs a 2D list `walls` to represent the maze.
- **Raises**:
  - `Exception`: If the maze file does not contain exactly one start point ('A') and one goal point ('B').
  - `FileNotFoundError`: If the maze file does not exist.
  - `ValueError`: If the maze file contains invalid characters or malformed lines.

#### `print()`
```python
def print(self)
```
- **Description**: 
  - Prints the maze to the console in a human-readable format.
  - The start point is marked with 'A', the goal point with 'B', walls with '█', and open paths with spaces (' ').
  - If a solution exists, the solution path will be printed, with the start and goal points displayed.
- **Returns**:
  - `None`

#### `neighbors(state)`
```python
def neighbors(self, state)
```
- **Parameters**:
  - `state` (tuple): A tuple representing the current state `(row, column)`.
  
- **Returns**:
  - A list of tuples, each representing a valid neighbor (up, down, left, right) of the current state.
  - If a neighboring cell is a wall, it is not included in the list.
  
- **Description**:
  - For each direction (up, down, left, right), it checks if the neighboring cell is within the bounds of the maze and if it's an open path (not a wall).

## Class: `Solver`

### Description
The `Solver` class implements a pathfinding algorithm (such as DFS, BFS, or A*) to solve the maze. It finds a path from the start point to the goal point.

### Attributes

- **`maze` (Maze)**: The maze object to be solved.
- **`num_explored` (int)**: The number of states that were explored during the solving process.
- **`explored` (set)**: A set containing all the explored states.

### Methods

#### `__init__(maze)`
```python
def __init__(self, maze)
```
- **Parameters**:
  - `maze` (Maze): The maze object to be solved.
- **Description**:
  - Initializes the solver with the given maze.
  - Sets up the initial number of explored states and the explored set.

#### `solve()`
```python
def solve(self)
```
- **Description**:
  - Solves the maze using a search algorithm.
  - Tracks the path taken from the start to the goal and saves the solution in `self.solution`.
  - If no solution is found, raises an exception.
  
- **Returns**:
  - `None` if the solution is found, and the solution is stored in `self.solution`.

## Class: `Node`

### Description
The `Node` class represents a state in the maze and stores information about the current state, the action taken to reach it, and its parent node. It is used to keep track of the states explored during the pathfinding process.

### Attributes

- **`state` (tuple)**: A tuple representing the current state in the maze (row, column).
- **`parent` (Node or None)**: The parent node from which this node was reached, or `None` if it is the root node (start point).
- **`action` (str or None)**: The action taken to reach the current state. This can be `None` for the root node or a string representing the move (e.g., 'up', 'down', 'left', 'right').
- **`g` (float)**: The cost from the start node to this node.
- **`h` (float)**: The heuristic cost estimate from this node to the goal.

### Methods

#### `__init__(state, parent, action, g=0, h=0)`
```python
def __init__(self, state, parent=None, action=None, g=0, h=0)
```
- **Parameters**:
  - `state` (tuple): The current state `(row, column)`.
  - `parent` (Node or None): The parent node from which this state was reached.
  - `action` (str or None): The action taken to reach this state.
  - `g` (float): The cost from the start node to this node.
  - `h` (float): The heuristic cost estimate from this node to the goal.
  
- **Description**:
  - Initializes a new node with the given state, parent, action, g, and h.

#### `f`
```python
@property
def f(self)
```
- **Description**:
  - Returns the total cost (f = g + h) for the node.
- **Returns**:
  - `float`: The total cost.

## Class: `Frontier`

### Description
The `Frontier` class is an abstract base class for frontier structures used in pathfinding algorithms. It manages the frontier of nodes that need to be explored.

### Attributes

- **`frontier` (list)**: A list that holds the nodes in the frontier.

### Methods

#### `__init__()`
```python
def __init__(self)
```
- **Description**: Initializes an empty frontier.

#### `add(node)`
```python
def add(self, node)
```
- **Parameters**:
  - `node` (Node): The node to be added to the frontier.
  
- **Description**:
  - Adds a node to the frontier.

#### `contains_state(state)`
```python
def contains_state(self, state)
```
- **Parameters**:
  - `state` (tuple): The state to check for in the frontier.
  
- **Returns**:
  - `True` if the frontier contains a node with the given state, otherwise `False`.
  
- **Description**:
  - Checks if a node with the given state exists in the frontier.

#### `empty()`
```python
def empty(self)
```
- **Returns**:
  - `True` if the frontier is empty, otherwise `False`.
  
- **Description**:
  - Checks if the frontier is empty.

## Class: `StackFrontier` (inherits from `Frontier`)

### Description
The `StackFrontier` class is a specific type of frontier that implements the behavior of a stack (LIFO - Last In, First Out). It removes the most recently added node.

### Methods

#### `remove()`
```python
def remove(self)
```
- **Returns**:
  - The most recently added node in the frontier.
  
- **Raises**:
  - `Exception`: If the frontier is empty.
  
- **Description**:
  - Removes and returns the most recently added node from the frontier.

## Class: `QueueFrontier` (inherits from `Frontier`)

### Description
The `QueueFrontier` class is a specific type of frontier that implements the behavior of a queue (FIFO - First In, First Out). It removes the earliest added node.

### Methods

#### `remove()`
```python
def remove(self)
```
- **Returns**:
  - The earliest added node in the frontier.
  
- **Raises**:
  - `Exception`: If the frontier is empty.
  
- **Description**:
  - Removes and returns the earliest added node from the frontier.

## Class: `AStarFrontier` (inherits from `Frontier`)

### Description
The `AStarFrontier` class is a specific type of frontier that implements the behavior of a priority queue. It removes the node with the lowest total cost (f = g + h).

### Methods

#### `__init__()`
```python
def __init__(self)
```
- **Description**: Initializes an empty priority queue frontier.

#### `add(node, cost)`
```python
def add(self, node, cost)
```
- **Parameters**:
  - `node` (Node): The node to be added to the frontier.
  - `cost` (float): The total cost (f = g + h) associated with the node.
  
- **Description**:
  - Adds a node to the frontier with a given cost.

#### `remove()`
```python
def remove(self)
```
- **Returns**:
  - The node with the lowest cost in the frontier.
  
- **Raises**:
  - `Exception`: If the frontier is empty.
  
- **Description**:
  - Removes and returns the node with the lowest cost.

## Class: `MazeVisualizer`

### Description
The `MazeVisualizer` class is responsible for visualizing a maze, its solution, and the explored cells. It uses the Python Imaging Library (PIL) to create a visual representation of the maze.

### Attributes

- **`maze` (Maze)**: The maze object that contains the layout and structure to be visualized.
- **`solution` (tuple or None)**: The solution to the maze, consisting of a list of actions and a list of cells visited along the path. Defaults to `None`.
- **`explored` (set)**: A set containing all the explored cells during the pathfinding process. Defaults to an empty set if `None` is provided.
- **`cell_size` (int)**: The size of each cell in the maze visualization (in pixels). Defaults to 50 pixels.
- **`cell_border` (int)**: The thickness of the border around each cell in the maze. Defaults to 2 pixels.

### Methods

#### `__init__(self, maze, solution=None, explored=None)`
```python
def __init__(self, maze, solution=None, explored=None)
```
- **Parameters**:
  - `maze` (Maze): The maze to be visualized.
  - `solution` (tuple or None): The solution to the maze, consisting of a list of actions and a list of cells visited. Defaults to `None`.
  - `explored` (set): A set of explored cells during the search process. Defaults to an empty set if `None` is provided.
  
- **Description**:
  - Initializes the `MazeVisualizer` object with the maze, solution, and explored cells (if provided).
  
#### `draw_maze(self, filename, show_solution=True, show_explored=False)`
```python
def draw_maze(self, filename, show_solution=True, show_explored=False)
```
- **Parameters**:
  - `filename` (str): The name of the output image file.
  - `show_solution` (bool): Whether to display the solution path on the maze. Defaults to `True`.
  - `show_explored` (bool): Whether to display the explored cells. Defaults to `False`.

- **Description**:
  - Draws the maze to an image file.

## Utility Functions

### `manhattan_distance(state1, state2)`
```python
def manhattan_distance(state1, state2)
```
- **Parameters**:
  - `state1` (tuple): The first state `(x1, y1)`.
  - `state2` (tuple): The second state `(x2, y2)`.
  
- **Returns**:
  - `float`: The Manhattan distance between the two states.
  
- **Description**:
  - Calculates the Manhattan distance between two states.