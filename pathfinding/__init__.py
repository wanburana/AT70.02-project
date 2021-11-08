import pygame
from configs import *

class Spot:
    def __init__(self, screen, row, col, width, total_rows):
        self.screen = screen
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_path(self):
        self.color = PURPLE

    def make_start(self):
        self.color = ORANGE
    
    def make_end(self):
        self.color = TURQUOISE

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


class Grid:
    def __init__(self, screen, rows, cols):
        self.screen = screen
        self.rows = rows
        self.cols = cols
        self._start = None # spot
        self._end = None # spot
        self._spots = []
        self.initial_elements()

    def get_start(self) -> Spot:
        return self._start

    def set_start(self, spot):
        self._start = spot
        return self._start

    def get_end(self) -> Spot:
        return self._end

    def set_end(self, spot):
        self._end = spot
        return self._end

    def get_spots(self):
        return self._spots

    def initial_elements(self):
        self._spots = []
        gap = self.cols // self.rows
        for i in range(self.rows):
            self._spots.append([])
            for j in range(self.rows):
                spot = Spot(self.screen, i, j, gap, self.rows)
                self._spots[i].append(spot)
    
    def _draw_grid(self):
        gap = self.cols // self.rows
        for i in range(self.rows):
            pygame.draw.line(self.screen, GREY, (0, gap * i), (self.cols, gap * i))
        for j in range(self.rows):
            pygame.draw.line(self.screen, GREY, (gap * j, 0), (gap * j, self.cols))

    def _draw_spot(self):
        for rows in self._spots:
            for spot in rows:
                spot.draw()

    def draw(self):
        # win.fill(WHITE)
        self._draw_spot()
        self._draw_grid()
        pygame.display.update()
    
    def get_spot_by_pos(self, pos) -> Spot:
        row, col = self._get_pos(pos)
        return self._spots[row][col]

    def _get_pos(self, pos):
        gap = self.cols // self.rows
        y, x = pos
        row = y // gap
        col = x // gap
        return row, col

    def update_spot_neighbors(self):
        for rows in self._spots:
            for spot in rows:
                spot.update_neighbors(self._spots)