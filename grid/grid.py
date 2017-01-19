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
    for y in range(20):
            for x in range(20):
                rect = pygame.Rect(x*(30+5), y*(30+5), 30, 30)
                pygame.draw.rect(screen, BLACK, (570,0, 30, 30), 0) # (570,0, 30, 30), 0 -----> WAS EERST rect
          
                                                                                 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()