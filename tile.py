import pygame
import sys



OFFSET_X = 0
OFFSET_Y = 0       
TILE_SIZE_X = 600
TILE_SIZE_Y = 600

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600




pygame.init()  

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Tile from Tileset")

tileset = pygame.image.load("cloud_1.png")
tileset.set_colorkey((255, 255, 0))

tile_rect = pygame.Rect(
    OFFSET_X, 
    OFFSET_Y,  
    TILE_SIZE_X,            
    TILE_SIZE_Y         
)


tile_image = tileset.subsurface(tile_rect)



clock = pygame.time.Clock() 

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            sys.exit()   

    screen.fill((255, 0, 255))


    screen.blit(
        tile_image,
        (0, 0)
    )


    pygame.display.flip()

    clock.tick(60)
