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
mx, my = pygame.mouse.get_pos()
        
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mx, my = pygame.mouse.get_pos()
        game_display.blit(schip, [mx,my])
    schip = pygame.image.load("schip1.png")
          
                                                                                 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
"""
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



 
pygame.quit()
"""