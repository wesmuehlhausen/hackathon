import pygame  # pygame is a set of Python mudules that is designed for writing videogames
import neat  # machine learning software
import time
import os
import random

#Import Images as an array of the three bird images
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
#Import the pipe image 
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))


#Class for the Bird object
class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    #Constructor for Bird Object
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0] # initial bird frame is first one

    #Function in bird class for jumping
    def jump(self):
        self.vel = -10.5 # remember that going UP on the screen is a negative y direction
        self.tick_count = 0
        self.height = self.y

    #Called every frame of the game
    def move(self):
        self.tick_count += 1 #increment tick every frame

        #displacement = how many frames we're moving up or down this frame
        #when we jump, the velocity is -10.5 and the tick count is low, so that means were going up
        #the right hand side of the equation has a magnitude of n^2 so eventually it will override it
        #and start making the bird go down faster and faster
        displ = self.vel*self.tick_count + 1.5*self.tick_count**2

        #Terminal velocity
        if displ >= 16:#if were moving downwards at more than 16, cap it at 16
            displ = 16
        #helps fine tune the jump 
        if displ < 0: 
            displ -= 2
        
        #Update the y position 
        self.y = self.y + displ

        #Tilt the flappy bird
        if displ < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    #used to draw the image on the window
    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:   
            self.img = self.IMGS[1] 
        elif self.img_count < self.ANIMATION_TIME*3:   
            self.img = self.IMGS[2] 
        elif self.img_count < self.ANIMATION_TIME*4:   
            self.img = self.IMGS[1] 
        elif self.img_count == self.ANIMATION_TIME*4 + 1:   
            self.img = self.IMGS[0] 
            self.img_count = 0
    
        #Nose dive 
        if self.tilt <= -80:
            self.img = self.IMGS[1] 
            self.img_count = self.ANIMATION_TIME*2

        #Actually apply the tilting to the image
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    #
    def get_mask(self):
        return pygame.mask.from_surface(self.img)

    # class Pipe:
    #     GAP = 200
    #     VEL = 5

