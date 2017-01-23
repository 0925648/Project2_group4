"""import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()

width = 1280
height = 720 
size = (width,height)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

done = False
 
clock = pygame.time.Clock()

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
   
    screen.fill(WHITE)
    for y in range(20):
            for x in range(20):
                rect = pygame.Rect(x*(30+5), y*(30+5), 30, 30)
                pygame.draw.rect(screen, BLACK, (570,0, 30, 30), 0) # (570,0, 30, 30), 0 -----> WAS EERST rect
          
                                                                                 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()"""

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()

width = 1280
height = 720 
size = (width,height)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

done = False
 
clock = pygame.time.Clock()

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
   
    screen.fill(WHITE)

height1 = 20
width1 = 20
block_size = 20

for y in range(height1):
    for x in range(width1):
        rect = pygame.Rect(x*(block_size+1), y*(block_size+1), block_size, block_size)
        pygame.draw.rect(screen, color, rect)
        
        pygame.display.update()
        clock.tick(60)
 
pygame.quit()