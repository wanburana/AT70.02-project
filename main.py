import pygame
from configs import *
import pathfinding as pf
import pathfinding.algorithms as algor

def get_model(model_name):
    name = model_name.lower()
    if name == 'dijkstra':
        return algor.Dijkstra()
    return algor.AStar()


def run_game(screen):
    grid = pf.Grid(screen, rows=ROWS, cols=WIDTH, generate_barrier=GENERATE_BARRIER, load_filename=LOAD_MAP_NAME)
    model = get_model(MODEL_NAME) # AStar, Dijkstra, Bellman algorithms

    # Event loop
    while 1:
        grid.draw() # draw grid and spots

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return

            start = grid.get_start()
            end = grid.get_end()

            # left, middle, right mouse
            (mouse1, mouse2, mouse3) = pygame.mouse.get_pressed()
            if mouse1:
                pos = pygame.mouse.get_pos()
                spot = grid.get_spot_by_pos(pos) # get spot object from clicked mouse position
                if not start and spot != end:
                    grid.set_start(spot).make_start()
                elif not end and spot != start:
                    grid.set_end(spot).make_end()
                elif spot != start and spot != end:
                    spot.make_barrier()

            elif mouse3:
                pos = pygame.mouse.get_pos()
                spot = grid.get_spot_by_pos(pos) # get spot object from clicked mouse position
                spot.reset()
                if spot == start:
                    grid.set_start(None)
                elif spot == end:
                    grid.set_end(None)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    # for every spot in grid, put its valid adjecent spot to its neighbors list
                    grid.update_spot_neighbors()
                    # execute algorithm
                    model.forward(grid)
                if event.key == pygame.K_c:
                    grid = pf.Grid(screen, rows=ROWS, cols=WIDTH, generate_barrier=GENERATE_BARRIER, load_filename=LOAD_MAP_NAME)
                if event.key == pygame.K_s:
                    grid.save()
                    print('Saved successfully.')


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption(PYGAME_TITLE)

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    run_game(screen)

if __name__ == '__main__':
    main()