import pygame
import sys

tile_size = 30
screen_size = 18
maze_block = []

SCREEN_WIDTH = tile_size * screen_size
SCREEN_HEIGHT = tile_size* screen_size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

tileX = 0
tileY = 0
tile_dict = {0: pygame.image.load("Counterspell\image\cave2.png"),    1: pygame.image.load("Counterspell\image\caveore2.png"), 3: pygame.image.load("Counterspell\image\wall2.png"), 4: pygame.image.load("Counterspell\image\path2.png"), 7: pygame.image.load("Counterspell\image\easure2.png"), 8: pygame.image.load("Counterspell\image\ontgreyattack2.png")}

map00 = [[0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 3, 3, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 3, 4, 3, 4, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 3, 4, 4, 4, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 3, 4, 8, 4, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 3, 3, 4, 3, 3, 4, 3, 3, 3, 3, 3, 3, 0, 0, 0],
[3, 3, 3, 0, 3, 4, 4, 3, 7, 3, 4, 4, 4, 3, 0, 0, 0, 0],
[3, 4, 3, 3, 3, 3, 4, 3, 3, 3, 4, 3, 3, 3, 0, 0, 0, 0],
[3, 4, 4, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3, 3, 0, 0, 0, 0],
[3, 3, 4, 4, 8, 4, 3, 3, 3, 3, 3, 4, 4, 3, 0, 0, 0, 0],
[0, 3, 3, 3, 4, 4, 4, 4, 3, 0, 3, 4, 8, 3, 3, 3, 3, 3],
[0, 3, 3, 3, 4, 3, 4, 4, 3, 0, 3, 4, 4, 3, 4, 4, 4, 3],
[0, 3, 4, 4, 4, 3, 4, 4, 3, 3, 3, 3, 4, 3, 4, 4, 4, 3],
[0, 3, 3, 3, 3, 3, 4, 4, 4, 3, 4, 4, 4, 8, 4, 4, 4, 3],
[0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3],
[0, 0, 0, 0, 3, 4, 4, 4, 4, 3, 3, 3, 3, 1, 0, 0, 0, 0],
[0, 0, 1, 0, 3, 3, 3, 3, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 1]]

for x in map00:
    for y in x:
        screen.blit(tile_dict[y], (tileX, tileY))
        tileX = tileX+30
    tileX = 0
    tileY += 30
    
while(1):
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()