
# Maze Solver API Documentation

## Overview
This document provides an overview of the Maze Solver API, detailing the class `Maze` and its methods. The class is designed to load a maze from a file, validate its contents, and display it in the console.

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
-**Returns**:
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
The `Solver` class implements a pathfinding algorithm (such as DFS or BFS) to solve the maze. It finds a path from the start point to the goal point.

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

### Methods

#### `__init__(state, parent, action)`
```python
def __init__(self, state, parent, action)
```
- **Parameters**:
  - `state` (tuple): The current state `(row, column)`.
  - `parent` (Node or None): The parent node from which this state was reached.
  - `action` (str or None): The action taken to reach this state.
  
- **Description**:
  - Initializes a new node with the given state, parent, and action.


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
