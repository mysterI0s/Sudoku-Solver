# game.py

import sys
import pygame
from constants import *
from grid import SudokuGrid
from renderer import SudokuRenderer
from enums import CellState

class SudokuGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Sudoku Solver")
        self.clock = pygame.time.Clock()
        self.grid = SudokuGrid()
        self.renderer = SudokuRenderer(self.screen)
        self.running = True

    def handle_click(self, pos, buttons):
        x, y = pos
        solve_rect, clear_rect, easy_rect, med_rect, hard_rect = buttons
        if y < GRID_HEIGHT:
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                self.grid.selected_cell = (row, col)
        elif solve_rect.collidepoint(pos):
            self.solve_puzzle()
        elif clear_rect.collidepoint(pos):
            self.clear_user_input()
        elif easy_rect.collidepoint(pos):
            self.grid.generate_random_puzzle("easy")
        elif med_rect.collidepoint(pos):
            self.grid.generate_random_puzzle("medium")
        elif hard_rect.collidepoint(pos):
            self.grid.generate_random_puzzle("hard")

    def handle_keypress(self, key: int):
        if self.grid.selected_cell is None:
            return
        row, col = self.grid.selected_cell
        if pygame.K_0 <= key <= pygame.K_9:
            number = key - pygame.K_0
            self.grid.set_cell_value(row, col, number)
        elif pygame.K_KP0 <= key <= pygame.K_KP9:
            number = key - pygame.K_KP0
            self.grid.set_cell_value(row, col, number)

    def solve_puzzle(self):
        if self.grid.solve_step_by_step():
            print("Puzzle solved successfully!")
        else:
            print("No solution exists for this puzzle.")

    def clear_user_input(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid.cell_states[i][j] == CellState.USER_INPUT:
                    self.grid.grid[i][j] = 0
                    self.grid.cell_states[i][j] = CellState.EMPTY

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos, self.renderer.draw_buttons())
                elif event.type == pygame.KEYDOWN:
                    self.handle_keypress(event.key)
            self.renderer.draw_grid(self.grid)
            buttons = self.renderer.draw_buttons()
            self.renderer.draw_status(self.grid)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()
