
# Intelligent N-Puzzle Solver

This project is a Python-based implementation of the N-Puzzle problem, developed as part of an Artificial Intelligence course.

## Overview

The Intelligent N-Puzzle Solver applies multiple search algorithms to solve the classic N-Puzzle problem, where the goal is to arrange a grid of numbers in the correct order by sliding tiles. 

The implemented algorithms include:
- **Breadth-First Search (BFS)**
- **Iterative Deepening Depth-First Search (IDDFS)**
- **Greedy Best-First Search (GBFS)** with a custom heuristic
- **A* Search** with a heuristic function for optimization

The program evaluates the performance of each algorithm by tracking the solution path and the number of nodes expanded.

## Features

- Solves the N-Puzzle problem for any 3x3 grid configuration.
- Uses efficient data structures such as queues, sets, and heaps.
- Custom heuristic to enhance the performance of GBFS and A* Search.
- Input validation to ensure robust and error-free execution.
- Outputs detailed results, including the solution path and expanded node count for each algorithm.

## Usage

### Requirements
- Python 3.x
- Standard Python libraries (`sys`, `collections`, `heapq`)

### Run the Program
1. Clone the repository to your local machine.
2. Run the program using the command line:
   ```bash
   python Tiles.py num1 num2 num3 num4 num5 num6 num7 num8 num9
   ```
   Replace `num1` to `num9` with unique numbers from 0 to 8 representing the puzzle's initial state.

### Example
```bash
python Tiles.py 1 2 3 4 5 6 7 8 0
```

### Output
The program prints the solution path and the number of nodes expanded for each algorithm.

## File Structure

- `Tiles.py`: Main script containing all implemented algorithms and the program logic.

## Skills Demonstrated

- Algorithm design and implementation
- Data structures and memory management
- Problem-solving and optimization

## License

This project is licensed under the MIT License - see the LICENSE file for details.

