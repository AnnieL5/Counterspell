import pygame

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

TILE_SIZE = 64

# Defining the window we will display our game on (in terms of pixels)
SCREEN_WIDTH = TILE_SIZE * 9
SCREEN_HEIGHT = TILE_SIZE * 9
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('Hungry Monkey')

tiles_img = ['empty', 'wall', 'goal']#change it to the path

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 2, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

player = None

def draw():
    screen.clear()
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = tiles_img[maze[row][column]]
            screen.blit(tile, (x, y))
            
player.draw()