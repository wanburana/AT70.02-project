import pygame
from configs import *
import pathfinding as pf
import pathfinding.algorithms as algor

def get_model(model_name):
    name = model_name.lower()
    if name == 'dijkstra':
        return algor.Dijkstra()
    return algor.AStar()

def initial_variables(screen=None):
    grid = pf.Grid(screen=screen, rows=ROWS, cols=WIDTH, generate_barrier=GENERATE_BARRIER, generate_start_stop=GENERATE_START_STOP, load_filename=LOAD_MAP_NAME)
    model = get_model(MODEL_NAME) # AStar, Dijkstra, Bellman algorithms
    return grid, model

def execute_model(grid, model):
    # for every spot in grid, put its valid adjecent spot to its neighbors list
    grid.update_spot_neighbors()
    # execute algorithm
    is_found_stop = model.forward(grid)
    print(f"{MODEL_NAME}: Spot closed (RED): {model.total_closed}, Time taken: {model.taken_time}, End?: {is_found_stop}")
    return is_found_stop

def run_game_without_gui():
    grid, model = initial_variables()
    is_found_stop = execute_model(grid, model)
    return model, is_found_stop

def auto_run(max_iter=10):
    times, counts, ends = [], [], []
    round = 0
    while round < max_iter:
        model, is_found_stop = run_game_without_gui()
        if is_found_stop or AUTO_INCLUDED_FAIL:
            times.append(model.taken_time)
            counts.append(model.total_closed)
            ends.append(is_found_stop)
            round += 1
    print(times)
    print(counts)

def run_game(screen):
    grid, model = initial_variables(screen)

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
                    execute_model(grid, model)
                if event.key == pygame.K_c:
                    grid, model = initial_variables(screen)
                if event.key == pygame.K_s:
                    grid.save()
                    print('Saved successfully.')


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption(f"{PYGAME_TITLE} - {MODEL_NAME}")

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
    if AUTO_RUN:
        auto_run(max_iter=AUTO_MAX_ITER)
    else:
        main()