import pygame
import sys


pygame.init()  

SCREEN_WIDTH = 600  
SCREEN_HEIGHT = 600 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Tile from Tileset")

tileset = pygame.image.load("cloud_1.jpg").convert_alpha()


clock = pygame.time.Clock()  

while True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()    

    screen.fill((255, 0, 255))


    screen.blit(
        tileset,
        (0, 0)
    )

  
    pygame.display.flip()

    clock.tick(60)