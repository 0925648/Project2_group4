import pygame
 
pygame.init()

width = 1280
height = 720
 
black = (0,0,0)
white = (255,255,255)
 

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Battleport')


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Battleport", largeText)
        TextRect.center = ((width/2),(height/2))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

game_intro()
pygame.quit()
quit()
