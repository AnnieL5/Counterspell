import pygame
import Classes
from Classes import Player, Zombie, Background
import random

class Game():

    def __init__(self):
        pygame.init()

        # A few variables
        self.gravity = .50
        self.ground = pygame.Rect(0, 640, 1280, 80)

        # Screen
        size = (1280, 720)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Moon Survival!')

        # Moon / Background
        self.moon = Background()

        # Zombies
        self.zombies = []
        for i in range(10):
            self.zombies.append( Zombie(random.randint(0,1280), random.randint(0,720)) )

        # Player
        self.player = Classes.Player(25, 320, self.gravity)

        self.treasure = pygame.image.load('images/zombie.png').get_rect()
        # Font for text
        self.font = pygame.font.SysFont(None, 72)

        # Pause - center on screen
        self.pause_text = self.font.render("PAUSE", -1, (255,0,0))
        self.pause_rect = self.pause_text.get_rect(center = self.screen.get_rect().center)
    def GameOver():
        pass
    def run(self):

        clock = pygame.time.Clock()

        # "state machine" 
        RUNNING   = True
        PAUSED    = False 
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

                    elif event.key == pygame.K_p:
                        PAUSED = not PAUSED

                # Player/Zomies events  

                if not PAUSED and not GAME_OVER:
                    self.player.handle_events(event)

            # (all) Movements / Updates

            if not PAUSED and not GAME_OVER:
                self.player.update(self.ground)
                for z in self.zombies:
                    z.update(self.screen.get_rect())
                if self.player.health >= 0:
                    self.GameOver()

            # (all) Display updating

            self.moon.render(self.screen)

            for z in self.zombies:
                z.render(self.screen)

            self.player.render(self.screen)

            if PAUSED:
                self.screen.blit(self.pause_text, self.pause_rect)

            pygame.display.update()

            # FTP

            clock.tick(100)

        # --- the end ---
        pygame.quit()

#---------------------------------------------------------------------

Game().run()