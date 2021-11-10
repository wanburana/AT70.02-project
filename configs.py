'''
    Application setting.
'''
PYGAME_TITLE = "A* Path Finding Algorithm"


'''
    - Press `S` key to save map, the message will be shown in terminal, then update config and restart the game.
    - None = have no any file to load
    - If file does not exist, error will be thown.
    - Use just filename + extension, path will be auto assigned.
    - Map is stored in `maps` folder.
    - Map is not uploaded to Github.
'''
LOAD_MAP_NAME=None
# LOAD_MAP_NAME='map-50x50.json' # None or filename


'''
    Auto Generate Map (AGM) will be disabled, if LOAD feature is used.
'''
GENERATE_BARRIER=False


'''
    - Set model that is used for shortest path finding.
    - Case-Insensitive.
    - Models: AStar, Dijkstra, Bellman.
    - Default is AStar.
'''
MODEL_NAME="Dijkstra"


'''
    Constants config.
'''
WIDTH = 600
ROWS = 50
RANDOM_BARRIER_THRESHOLD = 0.3
MAP_DIRECTORY="maps"
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE= (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)