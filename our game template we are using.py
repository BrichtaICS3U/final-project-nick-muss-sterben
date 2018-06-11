# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
pygame.init()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load("songone.wav")
pygame.mixer.music.play(-1) 
from sprite import donaldTrump, Button, createBullet
from vector2d import Vec2d

#-------------------------- Colors / Setup Stuff ----------------------------------#
donald_image = pygame.image.load("donald_trump_8bit.jpg")
donald = donaldTrump(donald_image, 100)
Background = pygame.image.load("bground.png")
MenuBackground = pygame.image.load("trump.png")
Levelone = pygame.image.load("level.png")
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

SCREENWIDTH = 1200
SCREENHEIGHT = 800
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

level = 1
carryOn = True
clock = pygame.time.Clock()
#----------------------------------------------------------------------------------#

#-------------------------------- Functions ---------------------------------------#
#---------------- Level Functions ----------------#
def shell_function():
    """A generic function that prints something in the shell"""
    print('Fire the nukes!')
#---------------#   
def nextLevel_function():
    """A function that advances to the next level"""
    global level
    level += 1
#---------------#
def play_function():
    """A function that leads you to the play screen"""
    global level
    level = 8
#---------------#
def mainMenu_function():
    """A function that retreats to the main menu"""
    global level
    level = 1
#---------------#
def settings_function():
    """A function that brings you to the settings screen"""
    global level
    level = 4
#---------------#
def howTo_function():
    """A function that explains how to play (controls)"""
    global level
    level = 2
#---------------#
def missionScreen_function():
    """A function that explains the mission (objective of the game)"""
    global level
    level = 3
#---------------#
def northKorea_function():
    """A function that "fires the nukes" like North Korea"""
    global level
    level = 5
#---------------#
def quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()
#--------------- Other Functions ---------------#
def mousebuttondown(level):
    """A function that checks which button was pressed"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in mainMenu_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 2:
        for button in settings_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 3:
        for button in settings_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 4:
        for button in settings_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
#----------------------------------------------------------------------------------#

#------------------------------- Button Setup -------------------------------------#
button_01 = Button("PLAY", (1072, 440), play_function, WHITE)
button_02 = Button("Main Menu", (1072, 770), mainMenu_function)
button_03 = Button("Quit", (1072, 620), quit_function, RED )
button_04 = Button("Settings", (1072, 500), settings_function, RED)
button_05 = Button("Mission Objective", (1072, 560), howTo_function, WHITE)
button_06 = Button("How to Play", (1072, 680), missionScreen_function, WHITE)
button_07 = Button("Nukes Button", (1072, 740), northKorea_function, RED)
button_08 = Button("Nukes Have Been Fired", (1072, 740), play_function, RED)

#--------------- Button List For Menu ---------------#
mainMenu_buttons = [button_01, button_03, button_04, button_05, button_06, button_07]
settings_buttons = [button_02]
howToPlay_buttons = [button_02]
missionScreen_buttons = [button_02]
nukesFiredScreen = [button_01, button_03, button_04, button_05, button_06, button_08]

bullet_list = pygame.sprite.Group()

#----------------------------------------------------------------------------------#

#----------------------------- Main Program Loop ----------------------------------#
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)

    # --- Game logic goes here

    # --- Draw code goes here
    
    # Clear the screen to white
    screen.fill(WHITE)
    screen.blit(MenuBackground, (0,0))

    # Draw buttons
    if level == 1:
        for button in mainMenu_buttons:
            button.draw(screen)
    elif level == 2:
        screen.fill(WHITE)
        screen.blit(Background, (0,0))
        for button in howToPlay_buttons:
            button.draw(screen)
        font = pygame.font.Font(None, 36)
        text = font.render("The evil James Comey has caused a zombie appocalyspse in an act of revenge for his firing", 1, (10, 10, 10))
        screen.blit(text, (50,50))
        font = pygame.font.Font(None, 36)
        text = font.render("The Objective of the game is you(Donald Trump) Must eliminate all the zombies ", 1, (10, 10, 10))
        screen.blit(text, (50,100))
        font = pygame.font.Font(None, 36)
        text = font.render("by any means possible, If so much as one zombie remains you will lose and the world will die.", 1, (10, 10, 10))
        screen.blit(text, (50,150))
        font = pygame.font.Font(None, 36)
        text = font.render("The entire fate of the world rests in your orange hands Donald...", 1, (10, 10, 10))
        screen.blit(text, (50,200))
        font = pygame.font.Font(None, 36)
        text = font.render("Good luck and Godspeed", 1, (10, 10, 10))
        screen.blit(text, (600,250))
        font = pygame.font.Font(None, 36)
        text = font.render("-Benjamin Solomon Carson Sr.", 1, (10, 10, 10))
        screen.blit(text, (600,300))
    elif level == 3:
        screen.fill(WHITE)
        screen.blit(Background, (0,0))
        for button in settings_buttons:
            button.draw(screen)
        font = pygame.font.Font(None, 60)
        text = font.render("UP arrow will move you up the screen", 1, (10, 10, 10))
        screen.blit(text, (50,50))
        font = pygame.font.Font(None, 60)
        text = font.render("DOWN arrow will move you down the screen", 1, (10, 10, 10))
        screen.blit(text, (50,150))
        font = pygame.font.Font(None, 60)
        text = font.render("LEFT arrow will move you to the left", 1, (10, 10, 10))
        screen.blit(text, (50,250))
        font = pygame.font.Font(None, 60)
        text = font.render("RIGHT arrow will move you to the right", 1, (10, 10, 10))
        screen.blit(text, (50,350))
        font = pygame.font.Font(None, 60)
        text = font.render("SPACEBAR to shoot", 1, (10, 10, 10))
        screen.blit(text, (50,450))
    elif level == 4:
        screen.fill(WHITE)
        screen.blit(Background, (0,0))
        for button in settings_buttons:
            button.draw(screen)
    elif  level == 5:
        for button in nukesFiredScreen:
            button.draw(screen)
    elif level == 8: #Actual Game Screen
        screen.blit(Levelone, (0,0))
        keys = pygame.key.get_pressed()
        bullet_list.update()
        donald.display(screen)
        bullet_list.draw(screen)
        
        if keys[pygame.K_LEFT]:
            donald.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            donald.moveRight(5)
        if keys[pygame.K_UP]:
            donald.moveUp(5)
        if keys[pygame.K_DOWN]:
            donald.moveDown(5)
        if keys[pygame.K_SPACE]:
            donald.shoot(bullet_list)
            #for bullets in bullet_list:
            #    bullets.move()
            
        

    
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
#----------------------------------------------------------------------------------#
