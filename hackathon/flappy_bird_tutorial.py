import pygame  # pygame is a set of Python mudules that is designed for writing videogames
import neat  # machine learning software
import time
import os
import random
import birdClass

#Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800



###############################################################################################

#Draw the window of the game
def draw_window(bird, win):
    win.blit(birdClass.BG_IMG, (0,0)) # draw the background image on the frame
    bird.draw(win)
    pygame.display.update()


def main():
    #Create objects
    bird = birdClass.Bird(200, 200)
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    run = True
    while run:
        for event in pygame.event.get(): #if there is a click event
            if event.type == pygame.QUIT: #if they want to quit the game
                run = False # exit condition for loop
        draw_window(bird, win)
    pygame.quit()
    quit()

main()