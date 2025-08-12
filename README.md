## Sudoku Solver

An interactive Sudoku game and visual backtracking solver built with `pygame`.

This app can generate puzzles at multiple difficulty levels, lets you play by entering numbers, and can visualize solving the puzzle step-by-step using a classic recursive backtracking algorithm.

### Features
- **Playable grid**: Click to select cells; type numbers to play.
- **Solver visualization**: Watch the backtracking algorithm explore possibilities.
- **Puzzle generator**: Create new puzzles in **Easy**, **Medium**, and **Hard** modes.
- **Controls**: Buttons to Solve/Clear and switch difficulty.
- **Clean architecture**: Separated modules for game loop, grid logic, rendering, and constants.

### Demo (Controls)
- **Select**: Click a cell
- **Enter number**: Press `1`-`9`
- **Clear cell**: Press `0`
- **Buttons**:
  - `SOLVE`: Run the visual solver
  - `CLEAR`: Clear all user-entered values
  - `EASY` / `MEDIUM` / `HARD`: Generate a new puzzle at that difficulty

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup
```bash
python -m venv venv
venv\\Scripts\\activate  # On Windows PowerShell
# source venv/bin/activate  # On macOS/Linux

pip install -r requirements.txt
```

## Run
```bash
python main.py
```

## How it works

### Architecture
- `main.py`: Application entry point; starts the game loop.
- `game.py`: `SudokuGame` – handles the event loop, input, and high-level actions.
- `grid.py`: `SudokuGrid` – board state, generator, validator, and backtracking solver.
- `renderer.py`: `SudokuRenderer` – draws the grid, numbers, buttons, and status text with `pygame`.
- `constants.py`: Sizes, colors, and layout constants.
- `enums.py`: `CellState` to distinguish given, user-entered, solving, and empty cells.

### Generation algorithm
1. **fill_grid**: Creates a full valid 9×9 Sudoku using recursive backtracking with randomized number order for variety.
2. **remove_numbers**: Removes a target number of cells depending on difficulty:
   - Easy: ~35 removals
   - Medium: ~45 removals
   - Hard: ~55 removals

### Solving algorithm
- A standard **recursive backtracking** approach. During solving, the current cell is marked as `SOLVING` and rendered in a different style so you can observe the search process.

## Configuration
You can tweak visuals and layout in `constants.py`:
- **Grid and cell size**: `GRID_SIZE`, `SUBGRID_SIZE`, `CELL_SIZE`
- **Window dimensions**: `WINDOW_WIDTH`, `WINDOW_HEIGHT`
- **Colors**: `Colors` class

## Troubleshooting
- **Pygame window doesn’t appear or crashes**:
  - Ensure you’re running inside an activated virtual environment.
  - Update graphics drivers (Windows) and make sure Python and `pygame` architectures match (both 64-bit).
  - Try reinstalling pygame: `pip install --upgrade --force-reinstall pygame`.
- **No text or odd fonts**: The app uses `pygame.font.Font(None, size)` which relies on system defaults. Ensure system fonts are available.
- **Performance issues**: Solver runs at 60 FPS rendering; older hardware may struggle. Reduce frame rate or simplify rendering if needed.

## Contributing
Pull requests and suggestions are welcome. Please keep code clear and modular. If you add features, consider adding a short note in this README to document usage.

## License
This project is released under the terms of the license found in `LICENSE`.
