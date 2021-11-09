import pygame
from queue import PriorityQueue
from .interface import AlgorithmModule

class Dijkstra(AlgorithmModule):

    def reconstruct_path(self, came_from, current, draw):
        while current in came_from:
            current = came_from[current]
            current.make_path()
            draw()

    def forward(self, grid):
        draw = lambda: grid.draw()
        start = grid.get_start()
        end = grid.get_end()
        spots = grid.get_spots()
        count = 0
        open_set = PriorityQueue() 
        open_set.put((0, count, start))
        came_from = {}
        score = {spot: float('inf') for rows in spots for spot in rows}
        score[start] = 0
        open_set_hash = {start}

        while not open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            current = open_set.get()[2]
            open_set_hash.remove(current)

            # create a shortest path from end to start
            if current == end:
                self.reconstruct_path(came_from, end, draw)
                end.make_end()
                return True

            for neighbor in current.neighbors:
                temp_score = score[current] + 1

                if temp_score < score[neighbor]:
                    came_from[neighbor] = current
                    score[neighbor] = temp_score

                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.make_open()
            draw()
            if current != start:
                current.make_closed()
        return False
