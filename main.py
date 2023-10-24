import pygame, sys
pygame.init()
import random

#Def colours
BLACK= (0,0,0)
WHITE= (255, 255, 255)
GREEN= (0,255,0)
RED= (255, 0 ,0)
BLUE= (0,0,255)

size = (800,500)

#Create window
screen= pygame.display.set_mode(size)

#Speed of objects
speed_x=3
speed_y=3

#Coords of circle
cord_x=100
cord_y=300



while True:
    for event in pygame.event.get():
        print(event)
        if event.type== pygame.QUIT:
            sys.exit()
    screen.fill(WHITE) #Background screen
### Drawing area
    #pygame.draw.line(screen, GREEN, [0, 100], [100, 300], 20) 
    #pygame.draw.ellipse(screen, BLACK, ([200, 50], [550,250]))
    for x in range (100, 700, 100):
        pygame.draw.circle(screen, (random.randrange(0, 255,1),random.randrange(0, 255,1),random.randrange(0, 255,1)), [(x+(x/2)), 300], (1+(x/12)))

### Drawing area
    pygame.display.flip() #Update screen
