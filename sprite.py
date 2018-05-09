import pygame, random
WHITE = (255, 255, 255)

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
        self.image = picture
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.picture = picture
        self.health = health

        self.rect = self.image.get_rect()

    def display(self, x, y, screen):
        screen.blit(self.image, (self.x, self.y))

    def moveLeft(self, xspeed):
        self.rect.x -= self.xspeed

    def moveRight(self, xspeed):
        self.rect.x += self.xspeed
