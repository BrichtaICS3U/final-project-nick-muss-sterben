import pygame, random

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

    def __init__(self, picture, health):
        super().__init__()
        self.image = pygame.transform.scale(picture, (111, 162))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.picture = picture
        self.health = health

        self.rect = self.image.get_rect()

    def display(self, screen, x, y):
        donald_image = pygame.image.load("donald_trump_8bit.jpg")
        screen.blit(donald_image, (x, y))

    def moveLeft(self, xspeed):
        self.rect.x -= xspeed

    def moveRight(self, xspeed):
        self.rect.x += xspeed
