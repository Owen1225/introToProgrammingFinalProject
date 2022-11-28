# Create a 2D game that is open world and the player can collect different items and fight different mobs
# Sources: 


# Libraries: 

import pygame, sys

#pygame setup
pygame.init()
WIDTH = 1200
HEIGHT = 700

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
ORANGE = (255, 98, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#load images
House1 = pygame.image.load('C:/Users/Owen.Du25/Downloads/Background/House1.jpg').convert_alpha()



#create function for drawing background
def draw_bg():
    screen.blit(House1, (0,0))


while True: 

    draw_bg()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    clock.tick(60)