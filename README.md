# AT70.02 Project: Path Finding

Python implementation of Pathfinding algorithm using Pygame.

![alt-text](https://github.com/wanburana/AT70.02-project/blob/main/examples/astar_auto.gif)

## Description

This project is part of AIT's AT70.02 Data Strucure and Algorithm to demonstrate two pathfinding algorithm including
- A-star Algorithm
- Dijkstra Algorithm

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

```
git clone ...
cd ...
pip isntall ...

```

### Executing program

* How to run the program
* Step-by-step bullets
```
python main.py
```

## Help

### In-game shortcut
- `Left-click` to create `start`, `end`, and `barrier` (`start`, `end`, and `barrier` will be created respectively)  
- `Right-click` to remove/reset that spot  
- `SPACEBAR` to run the algorithm (`start` and `end` need to be already created.)  
- `c` to reset the whole program  
- `s` to save the current map  

### configs.py setting
- LOAD_MAP_NAME (String or None): path of the generated map, set to None to start with empty map
- GENERATE_BARRIER (Boolean): Whether the barrier will be generated randomly when the program start or not
- GENERATE_START_STOP (Boolean): Whether the start and stop will be generated randomly when the program start or not
- MODEL_NAME (String): Algorithm used in the program (AStar, Dijkstra)
- RANDOM_BARRIER_THRESHOLD (Float): the probability that a spot will be generated as a barrier (in case `GENERATE_BARRIER` is set to `True`)

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)


## Acknowledgments

Inspiration, code snippets, etc.
* [A* Pathfinding Visualization Tutorial - Python A* Path Finding Tutorial](https://www.youtube.com/watch?v=JtiK0DOeI4A) (A-star algorithm tuturial & Implementation guideline)
* [DomPizzie/README-Template.md](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc) (Awesome simple README template)
