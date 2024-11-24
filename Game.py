import pygame
import Classes
from Classes import Player, Ghost, Background
import random
import numpy as np

# font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

tile_size = 64

maze = [[0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 3, 4, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 3, 4, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 3, 4, 4, 4, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 3, 4, 8, 4, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 3, 3, 4, 3, 3, 4, 3, 3, 3, 3, 3, 3, 0, 0, 0],
[3, 3, 3, 0, 3, 4, 4, 3, 7, 3, 4, 4, 4, 3, 0, 0, 0, 0],
[3, 4, 3, 3, 3, 3, 4, 3, 6, 3, 4, 3, 3, 3, 0, 0, 0, 0],
[3, 4, 4, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3, 3, 0, 0, 0, 0],
[3, 3, 4, 4, 8, 4, 3, 3, 3, 3, 3, 4, 4, 3, 0, 0, 0, 0],
[0, 3, 3, 3, 4, 4, 4, 4, 3, 0, 3, 4, 8, 3, 3, 3, 3, 3],
[0, 3, 3, 3, 4, 3, 4, 4, 3, 0, 3, 4, 4, 3, 4, 4, 4, 3],
[0, 3, 4, 4, 4, 3, 4, 4, 3, 3, 3, 3, 4, 3, 4, 4, 4, 3],
[0, 3, 3, 3, 3, 3, 4, 4, 4, 3, 4, 4, 4, 8, 4, 4, 4, 3],
[0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3],
[0, 0, 0, 0, 3, 4, 4, 4, 4, 3, 3, 3, 3, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 3, 3, 3, 6, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0]]

screen_size = 18
maze_block = []

SCREEN_WIDTH = tile_size * screen_size
SCREEN_HEIGHT = tile_size * screen_size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('Hungry Monkey')
p = "C:\Annie\code\Hackathon\Ccounterspell\Counterspell\image\wall.png"
background_img = [p, p]
player_img = [p, p, p, p]

        # Moon / Background


# Create a function to generate a 3x3 block for each element
# def create_block(value):
#     return np.full((3, 3), value)

# # Create a 2x2 matrix of blocks
# maze_block = np.empty((2, 2), dtype=object)
# for i in range(2):
#     for j in range(2):
#         maze_block[i, j] = create_block(maze[i, j])

for r in range(len(maze)//screen_size):
    for c in range(len(maze[1])//screen_size):
        block = []
        for i in range(screen_size):
            row = []
            row = maze[r+i][c:c+3]
            print(row)
            # for j in range(screen_size):
            #     row.append(maze[r+i][c+j])
            block.append(row)
        maze_block.append(block)
    
background = Classes.Background(background_img, maze_block, screen_size, screen_size, tile_size)


class Game():

    def __init__(self, screen, background, player_img):
        pygame.init()

        # Defining the window we will display our game on (in terms of pixels)
        self.screen = screen
        # pygame.display.set_caption('Hungry Monkey')

        # Moon / Background
        self.background = background

        # Zombies
        
        self.player = Player(7*tile_size, 15*tile_size, tile_size, player_img)

        # Font for text
        # self.font = pygame.font.SysFont(None, 72)

        # Pause - center on screen
        
    def run(self):

        clock = pygame.time.Clock()

        # "state machine" 
        RUNNING   = True
        GAME_OVER = False

        # Game loop
        while RUNNING:

            # (all) Events

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    RUNNING = False

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        RUNNING = False


                # Player/Zomies events  

                if not GAME_OVER:
                    self.player.handle_events(event)

            # (all) Movements / Updates

            if not GAME_OVER:
                self.background.update(self.player, tile_size, self.screen)
                self.ghostPos = background.ifGhost()
            
                self.player.update(self.ground)
                
                self.ghostPos = Classes.Background.ifGhost()
                if self.ghostPos != None:
                    self.ghost = Classes.Ghost(self.ghostPos[0], self.ghostPos[1])
                
                if(self.player.position == [8,6]):
                    self.treasure = pygame.image.load(background_img[6]).get_rect()
                    self.treasure.topleft = [8*tile_size, 6*tile_size]
                    
            
                if self.player.health >= 0:
                    Background.game_over_display()

            # (all) Display updating

            self.player.render(self.screen)

            # for z in self.zombies:
            #     z.render(self.screen)

            self.ghost.render(self.screen)
            pygame.display.update()

            # FTP

            clock.tick(100)

        # --- the end ---
        pygame.quit()

#---------------------------------------------------------------------

Game(screen, background, player_img).run()