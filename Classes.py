import pygame

class Character:
    spite = []
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.position = [[0,0],[0,0]] #0,0 is the center
        self.spiteNum = 0
        PastSelf.attempt += 1
    
    def PicIncrement(self, x, y):
        self.position[0][0] = self.position[0][0] + x
        self.position[0][1] = self.position[0][1] + y
        
    def PositionIncrement(self, x, y):
        self.position[1][0] = self.position[1][0] + x
        self.position[1][1] = self.position[1][1] + y
        
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, size, frameSize, path): #path

        # Player image and animation
        self.images = []
        for i in path:
            self.images.append(pygame.image.load(path[i]))
        self.maxImage = len(self.images)
        self.currentImage = 0

        self.rect = pygame.Rect(x, y, size, size)
        # self.rect = self.images[0].get_rect()
        # self.rect.x = x
        # self.rect.y = y

        # self.timeTarget = 10
        # self.timeNum = 1

        self.velX = 0
        self.velY = 0
        
        self.isAttacking = False
        
        self.health = 1000
        self.position = [0,0]#0,0 is the center. Frame #
        # For x, y refere to self.rect.x/y

        # Jump and gravity
        # self.vSpeed = 3
        # self.maxVspeed = 3
        
    # Jump inputs
    def handle_events(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                if not self.isAttacking:
                    self.isAttacking = True

            elif event.key == pygame.K_a:
                self.velX = -5
                

            elif event.key == pygame.K_d:
                self.velX = +5
                
            elif event.key == pygame.K_s:
                self.velY = -5

            elif event.key == pygame.K_w:
                self.velY = +5

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_d):
                self.velX = 0
            
            elif event.key in (pygame.K_w, pygame.K_s):
                self.velY = 0

    def attack(self, enemy, damage, distance, img):
        if enemy.position[0] == self.position[0]:
            if enemy.rect.x-self.rect.x <= distance and enemy.rect.y-self.rect.y <= distance:
                enemy.health -= damage
                enemy.render(enemy, img)
                Zombie.ifDead()
    
    
    # PLayer updates
    def update(self, enemies, wall, img, frame, numPixel):

        keys = pygame.key.get_pressed()

        self.rect.x += self.velX
        self.rect.y += self.velY
        
        self.render(self.rect)

         # Jumping

        if self.isAttacking:
            if time == None:
                time = pygame.time.get_ticks()
                self.attack(enemies, 15, 40, img)
            if pygame.time.get_ticks() - time < 500:
                self.isAttacking == True
                
            else:
                self.isAttacking = False

        #print "isJumping:", self.isJumping
        #Check if monkey is on a platform
        for platform in wall:
            if self.rect.collicolliderect(platform):
                self.rect.x -= self.velX
                self.rect.y -= self.velY
                self.velY = 0
                self.velX = 0
                break
                
                

		#Generate new platforms every time the ground is touched (won't generate if there are enough platforms)

        # Animations
        # Screen wrap
        if self.rect.right > frame[0] and self.position[0]<numPixel[0]:
            self.rect.x = 0
            self.position[0] += 1

        elif self.rect.left < 0 and self.position[0]>0:
            self.rect.right = frame[0]
            self.position[0] -= 1

        if self.rect.top > frame[1] and self.position[1]<numPixel[1]:
            self.rect.y = 0
            self.position[1] += 1

        elif self.rect.bottom < 0 and self.position[1]>0:
            self.rect.bottom = frame[1]
            self.position[1] -= 1
            
    def render(self, surface):
        surface.blit(self.images[self.currentImage], self.rect)

class Background():

    def __init__(self, path, maze):

        self.path = path
        self.maze = maze

    def update(self, character, TILE_SIZE, screen):
        self.cMaze = self.maze[character.position[0], character.position[1]]
        for row in range(len(self.cMaze)):
            for column in range(len(self.cMaze[row])):
                x = column * TILE_SIZE
                y = row * TILE_SIZE
                tile = self.path[self.cMaze[row][column]]
                screen.blit(tile, (x, y))

class Zombie():

    def __init__(self, x, y):

        self.image = pygame.image.load('images/zombie.png')
        #~ self.image = pygame.image.load('ball2.png')
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.direction_left = True
        self.health = 500

    def update(self, surface_rect, character):
        if self.direction_left:
            self.rect.x -= 1
            if self.rect.left <= surface_rect.left:
                self.direction_left = not self.direction_left
        else:
            self.rect.x += 1
            if self.rect.right >= surface_rect.right:
                self.direction_left = not self.direction_left
        
        if(character.rect.collicolliderect(self.rect)):
            character.health -= 20
            

    def render(self, surface):
        surface.blit(self.image, self.rect)
    def ifDead(self):
        if self.health <= 0:
            del self
            

class PastSelf(Character):
    attempt = 0
    spite = []
    
    def __init__(self, num):
        self.num = num
        self.health = 100
        self.position = [[0,0],[0,0]] #0,0 is the center
        self.spiteNum = 0
    