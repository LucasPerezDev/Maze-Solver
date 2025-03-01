
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

#### `print()`
```python
def print(self)
```
- **Description**: 
  - Prints the maze to the console in a human-readable format.
  - The start point is marked with 'A', the goal point with 'B', walls with '█', and open paths with spaces (' ').
  
