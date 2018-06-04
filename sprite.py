import pygame, random, math
from vector2d import Vec2d

#--------------------------------- Colors -----------------------------------------#
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (240, 101, 67)
SEA = (11, 83, 81)
SKY = (0, 178, 149)
YELLOW = (227, 181, 5)
SAND = (184, 180, 45)
#----------------------------------------------------------------------------------#

#------------------------------ Button Class --------------------------------------#
class Button():
    """This is a class for a generic button.
       txt = text on the button
       location = (x,y) coordinates of the button's centre
       action = name of function to run when button is pressed
       bg = background colour (default is white)
       fg = text colour (default is black)
       size = (width, height) of button
       font_name = name of font
       font_size = size of font
    """
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(255, 60), font_name="Segoe Print", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self, screen):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        """Checks if mouse is over button using rect collision"""
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GRAY  # mouseover color

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()
#----------------------------------------------------------------------------------#

#------------------------------- Bullet Class -------------------------------------#
class createBullet(pygame.sprite.Sprite):

    def __init__(self, damage, speed, position, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.damage = damage
        self.speed = Vec2d(speed)
        self.position = Vec2d(position)
        self.color = color
        self.width = width
        self.height = height

        pygame.draw.rect(self.image, color, [0,0, width, height])
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        self.position = self.position.__add__(self.speed)
        self.rect.center = self.position
        if (self.position.x > 1200) or (self.position.x < -5) or (self.position.y > 800) or (self.position.y < -5):
            self.speed = (0,0)

#----------------------------------------------------------------------------------#
        
#---------------------------- Donald Trump Class ----------------------------------#
class donaldTrump(pygame.sprite.Sprite):
    """
    Variables:
        - xpos, ypos
        - xspeed, yspeed
        - picture
        - health
    Methods:
        - display
        - move
        - jump
        - shoot
    """

    def __init__(self, picture, health, position=(500, 500), direction=1):
        super().__init__()
        self.image = pygame.transform.scale(picture, (111, 162))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.picture = picture
        self.health = health
        self.position = Vec2d(position)
        self.direction = direction
        """
        Directions:
            - Up:    1
            - Left:  2
            - Down:  3
            - Right: 4
        """

        self.rect = self.image.get_rect()

    def display(self, screen):
        #donald_image = pygame.image.load("donald_trump_8bit.jpg")
        screen.blit(self.picture, self.position)

    def moveLeft(self, xspeed):
        self.direction = 2
        tempMovement = (-xspeed, 0)
        movement = Vec2d(tempMovement)
        self.position = self.position.__add__(movement)

    def moveRight(self, xspeed):
        self.direction = 4
        tempMovement = (xspeed, 0)
        movement = Vec2d(tempMovement)
        self.position = self.position.__add__(movement)

    def moveUp(self, yspeed):
        self.direction = 1
        tempMovement = (0, -yspeed)
        movement = Vec2d(tempMovement)
        self.position = self.position.__add__(movement)

    def moveDown(self, yspeed):
        self.direction = 3
        tempMovement = (0, yspeed)
        movement = Vec2d(tempMovement)
        self.position = self.position.__add__(movement)

    def shoot(self, bullet_list):
        if self.direction == 1: #Up
            bullet = createBullet(20, (0, -6), self.position, BLACK, 5, 5)
            #bullet.update()
            bullet_list.add(bullet)
            print('up')
        if self.direction == 2: #Left
            bullet = createBullet(20, (-6, 0), self.position, BLACK, 5, 5)
            #bullet.update()
            bullet_list.add(bullet)
            print('left')
        if self.direction == 3: #Down
            bullet = createBullet(20, (0, 6), self.position, BLACK, 5, 5)
            #bullet.update()
            bullet_list.add(bullet)
            print('down')
        if self.direction == 4: #Right
            bullet = createBullet(20, (6, 0), self.position, BLACK, 5, 5)
            #bullet.update()
            bullet_list.add(bullet)
            print('right')
