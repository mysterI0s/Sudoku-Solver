# grid.py

import random
from typing import List, Tuple, Optional
from constants import GRID_SIZE, SUBGRID_SIZE
from enums import CellState

class SudokuGrid:
    def __init__(self):
        self.grid: List[List[int]] = [
            [0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)
        ]
        self.cell_states: List[List[CellState]] = [
            [CellState.EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)
        ]
        self.selected_cell: Optional[Tuple[int, int]] = None
        self.generate_random_puzzle(difficulty="medium")

    def generate_random_puzzle(self, difficulty="medium"):
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.cell_states = [
            [CellState.EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)
        ]
        self.fill_grid()
        self.remove_numbers(difficulty)
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] != 0:
                    self.cell_states[i][j] = CellState.GIVEN

    def fill_grid(self) -> bool:
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True
        row, col = empty_cell
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for num in numbers:
            if self.is_valid_move(row, col, num):
                self.grid[row][col] = num
                if self.fill_grid():
                    return True
                self.grid[row][col] = 0
        return False

    def remove_numbers(self, difficulty="medium"):
        if difficulty == "easy":
            cells_to_remove = 35
        elif difficulty == "hard":
            cells_to_remove = 55
        else:
            cells_to_remove = 45
        attempts = cells_to_remove
        while attempts > 0:
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            if self.grid[row][col] != 0:
                self.grid[row][col] = 0
                self.cell_states[row][col] = CellState.EMPTY
                attempts -= 1

    def is_valid_move(self, row: int, col: int, num: int) -> bool:
        for c in range(GRID_SIZE):
            if c != col and self.grid[row][c] == num:
                return False
        for r in range(GRID_SIZE):
            if r != row and self.grid[r][col] == num:
                return False
        start_row = (row // SUBGRID_SIZE) * SUBGRID_SIZE
        start_col = (col // SUBGRID_SIZE) * SUBGRID_SIZE
        for r in range(start_row, start_row + SUBGRID_SIZE):
            for c in range(start_col, start_col + SUBGRID_SIZE):
                if (r != row or c != col) and self.grid[r][c] == num:
                    return False
        return True

    def find_empty_cell(self) -> Optional[Tuple[int, int]]:
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None

    def solve_step_by_step(self) -> bool:
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True
        row, col = empty_cell
        self.cell_states[row][col] = CellState.SOLVING
        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.grid[row][col] = num
                if self.solve_step_by_step():
                    self.cell_states[row][col] = CellState.USER_INPUT
                    return True
                self.grid[row][col] = 0
        self.cell_states[row][col] = CellState.EMPTY
        return False

    def set_cell_value(self, row: int, col: int, value: int) -> bool:
        if self.cell_states[row][col] == CellState.GIVEN:
            return False
        if value == 0:
            self.grid[row][col] = 0
            self.cell_states[row][col] = CellState.EMPTY
            return True
        if self.is_valid_move(row, col, value):
            self.grid[row][col] = value
            self.cell_states[row][col] = CellState.USER_INPUT
            return True
        return False

    def is_complete(self) -> bool:
        return self.find_empty_cell() is None
