import pygame
from queue import PriorityQueue
from .interface import AlgorithmModule

class AStar(AlgorithmModule):
    def __init__(self):
        super().__init__()

    def h(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        return abs(x1 - x2) + abs(y1 - y2)

    def reconstruct_path(self, came_from, current, draw):
        while current in came_from:
            current = came_from[current]
            current.make_path()
            draw()

    def forward(self, grid):
        super().start_timer()
        draw = lambda: grid.draw()
        start = grid.get_start()
        end = grid.get_end()
        spots = grid.get_spots()
        count = 0
        open_set = PriorityQueue() # sort value by the first value of tuple (f-score), if tie, sort by second value (count)
        open_set.put((0, count, start))
        came_from = {} # keep track of the previous spot 
        g_score = {spot: float('inf') for rows in spots for spot in rows} # initially assign every spot distance as infinity
        g_score[start] = 0 
        f_score = {spot: float('inf') for rows in spots for spot in rows} 
        f_score[start] = self.h(start.get_pos(), end.get_pos()) # initially assign heuristic score as the distance between start and end

        open_set_hash = {start}

        while not open_set.empty():
            if grid.has_gui():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
            current = open_set.get()[2]
            open_set_hash.remove(current)
            if current == end:
                self.reconstruct_path(came_from, end, draw)
                end.make_end()
                super().stop_timer()
                return True
            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1 # g_score increases as the algorithm steps
                
                # relaxing
                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + self.h(neighbor.get_pos(), end.get_pos())
                    
                    # add new instance to priority queue and set
                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.make_open()
            draw()
            if current != start:
                current.make_closed()
                super().count_closed()
        super().stop_timer()
        return False
