#!/usr/bin/python
#!/bin/env python

import pygame
import external.pygbutton as pygbutton
import source.Configuration
import sys
import time

# constants
ORIGIN = (0, 0)
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 272

def printUsage():
    print "%s <configurationFilePath>" % (sys.argv[0])

# define a main function
def main():
    
    # check the number of input arguments
    if (len(sys.argv) != 2):
        printUsage()
        sys.exit(-1)

    # initialize the game module and clock
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    # read the provided configuration file
    config = source.Configuration.Configuration(sys.argv[1])

    # create the display screen; set FULL SCREEN 
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
    
    # load and set the provided background image
    backgroundImage = pygame.image.load(config.getBackgroundImagePath()).convert()
    SCREEN.blit(backgroundImage, ORIGIN)

    # create buttons for user input
    leftButton = pygbutton.PygButton(config.getLeftButtonRect(),
                                     normal=config.getLeftButtonImage(),
                                     down=config.getLeftButtonImage(),
                                     highlight=config.getLeftButtonImage())  

    middleButton = pygbutton.PygButton(config.getMiddleButtonRect(),
                                       normal=config.getMiddleButtonImage(),
                                       down=config.getMiddleButtonImage(),
                                       highlight=config.getMiddleButtonImage())

    rightButton = pygbutton.PygButton(config.getRightButtonRect(),
                                      normal=config.getRightButtonImage(),
                                      down=config.getRightButtonImage(),
                                      highlight=config.getRightButtonImage())

    ticks = 0

    # main loop
    while True:

        # load and set the provided background image if it is time
        if ticks % (config.getFPS() * 5) == 0:
            SCREEN.fill((255,255,255))
            backgroundImage = pygame.image.load(config.getBackgroundImagePath()).convert()
            SCREEN.blit(backgroundImage, ORIGIN)

        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # handle left button events
            leftButtonEvents = leftButton.handleEvent(event)
            if 'click' in leftButtonEvents:
                pygame.mixer.music.load(config.getLeftFile())
                pygame.mixer.music.play(0)

            middleButtonEvents = middleButton.handleEvent(event)
            if 'click' in middleButtonEvents:
                pygame.mixer.music.load(config.getMiddleFile())
                pygame.mixer.music.play(0)

            rightButtonEvents = rightButton.handleEvent(event)
            if 'click' in rightButtonEvents:
                pygame.mixer.music.load(config.getRightButtonFile())
                pygame.mixer.music.play(0)

        # add the button(s) to the display
        leftButton.draw(SCREEN)
        middleButton.draw(SCREEN)
        rightButton.draw(SCREEN)

        # update the screen and sleep for a short period
        pygame.display.update()
        FPSCLOCK.tick(config.getFPS())
        ticks += 1    

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

