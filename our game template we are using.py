# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
from sprite import donaldTrump, Button
pygame.init()

#-------------------------- Colors / Setup Stuff ----------------------------------#
donald_image = pygame.image.load("donald_trump_8bit.jpg")
donald = donaldTrump(donald_image, 100)

MenuBackground = pygame.image.load("trump.png")

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
    level = 2
#---------------#
def howTo_function():
    """A function that explains how to play (controls)"""
    global level
    level = 3
#---------------#
def missionScreen_function():
    """A function that explains the mission (objective of the game)"""
    global level
    level = 4
#---------------#
def nuke_function():
    """A function that brings you to the nuke firing screen"""
    global level
    level = 5
#---------------#
def northKorea_function():
    """A function that "fires the nukes" like North Korea"""
    global level
    level = 6
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
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 2:
        for button in level2_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
#----------------------------------------------------------------------------------#

#------------------------------- Button Setup -------------------------------------#
button_01 = Button("PLAY", (1072, 440), play_function, SKY)
button_02 = Button("Main Menu", (SCREENWIDTH/2, SCREENHEIGHT/3), mainMenu_function)
button_03 = Button("Quit", (1072, 620), quit_function, SEA )
button_04 = Button("Settings", (1072, 500), settings_function, ORANGE)
button_05 = Button("How to Play", (1072, 560), howTo_function, YELLOW)
button_06 = Button("Mission Objective", (1072, 680), missionScreen_function, BLUE)
button_07 = Button("Nukes Button", (1072, 740), nuke_function, RED)
button_08 = Button("The Nukes Have Been Fired", (1072, 740), northKorea_function, GRAY)

#--------------- Button List For Menu ---------------#
level1_buttons = [button_01, button_03, button_04, button_05, button_06, button_07]
level2_buttons = [button_01, button_03, button_04, button_05, button_06, button_07, button_08]
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
        for button in level1_buttons:
            button.draw()
    elif level == 2:
        for button in level2_buttons:
            button.draw()
    elif level == 3:
        donald.display(400, 600, screen);

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
#----------------------------------------------------------------------------------#
