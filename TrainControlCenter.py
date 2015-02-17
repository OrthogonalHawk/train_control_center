#!/usr/bin/python
#!/bin/env python

import pygame
import source.Configuration
import sys
import time

window_size = (480, 272)

def printUsage():
    print "%s <configurationFilePath>" % (sys.argv[0])

# define a main function
def main():
    
    # check the number of input arguments
    if (len(sys.argv) != 2):
        printUsage()
        sys.exit(-1)

    # initialize the pygame module
    pygame.init()

    # read the provided configuration file
    config = source.Configuration.Configuration(sys.argv[1])

    # create the display screen; set FULL SCREEN 
    screen = pygame.display.set_mode(window_size, pygame.FULLSCREEN)
    
    # load the provided background image
    backgroundImage = pygame.image.load(config.getBackgroundImagePath()).convert()

    # set the background image
    screen.blit(backgroundImage, (0,0))

    # update the displayed screen
    pygame.display.update()

    # define a variable to control the main loop
    running = True
    
    # main loop
    while running:

        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:

                # change the value to False, to exit the main loop
                running = False

        # use a sleep to prevent CPU hogging
        time.sleep(1)    

    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

