# renderer.py

import pygame
from constants import *
from enums import CellState
from grid import SudokuGrid

class SudokuRenderer:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)

    def draw_grid(self, grid: SudokuGrid):
        self.screen.fill(Colors.WHITE)
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x = j * CELL_SIZE
                y = i * CELL_SIZE
                cell_color = Colors.WHITE
                if grid.selected_cell == (i, j):
                    cell_color = Colors.YELLOW
                elif grid.cell_states[i][j] == CellState.SOLVING:
                    cell_color = Colors.LIGHT_GRAY
                pygame.draw.rect(self.screen, cell_color, (x, y, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(self.screen, Colors.BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)
                if grid.grid[i][j] != 0:
                    self.draw_number(x, y, grid.grid[i][j], grid.cell_states[i][j])
        for i in range(0, GRID_SIZE + 1, SUBGRID_SIZE):
            pygame.draw.line(self.screen, Colors.BLACK, (0, i * CELL_SIZE), (GRID_WIDTH, i * CELL_SIZE), 3)
            pygame.draw.line(self.screen, Colors.BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, GRID_HEIGHT), 3)

    def draw_number(self, x: int, y: int, number: int, state: CellState):
        color = Colors.BLACK
        font = self.font_large
        if state == CellState.USER_INPUT:
            color = Colors.BLUE
        elif state == CellState.SOLVING:
            color = Colors.RED
            font = self.font_medium
        text = font.render(str(number), True, color)
        text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
        self.screen.blit(text, text_rect)

    def draw_buttons(self):
        button_y = GRID_HEIGHT + 10
        solve_rect = pygame.Rect(10, button_y, 100, BUTTON_HEIGHT - 10)
        pygame.draw.rect(self.screen, Colors.GREEN, solve_rect)
        self.screen.blit(self.font_medium.render("SOLVE", True, Colors.WHITE), solve_rect.move(10, 5))

        clear_rect = pygame.Rect(120, button_y, 100, BUTTON_HEIGHT - 10)
        pygame.draw.rect(self.screen, Colors.RED, clear_rect)
        self.screen.blit(self.font_medium.render("CLEAR", True, Colors.WHITE), clear_rect.move(10, 5))

        easy_rect = pygame.Rect(230, button_y, 80, BUTTON_HEIGHT - 10)
        pygame.draw.rect(self.screen, Colors.ORANGE, easy_rect)
        self.screen.blit(self.font_small.render("EASY", True, Colors.WHITE), easy_rect.move(15, 10))

        med_rect = pygame.Rect(320, button_y, 90, BUTTON_HEIGHT - 10)
        pygame.draw.rect(self.screen, Colors.BLUE, med_rect)
        self.screen.blit(self.font_small.render("MEDIUM", True, Colors.WHITE), med_rect.move(10, 10))

        hard_rect = pygame.Rect(420, button_y, 80, BUTTON_HEIGHT - 10)
        pygame.draw.rect(self.screen, Colors.GRAY, hard_rect)
        self.screen.blit(self.font_small.render("HARD", True, Colors.WHITE), hard_rect.move(15, 10))

        return solve_rect, clear_rect, easy_rect, med_rect, hard_rect

    def draw_status(self, grid: SudokuGrid):
        if grid.is_complete():
            status_text = "Puzzle Solved! Congratulations!"
            color = Colors.GREEN
        else:
            status_text = "Click a cell and press 1-9 to enter numbers, 0 to clear"
            color = Colors.BLACK
        text = self.font_small.render(status_text, True, color)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 5))
        self.screen.blit(text, text_rect)
