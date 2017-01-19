import pygame

import time
clock=pygame.time.Clock()
background_image = pygame.image.load("battleship_045.jpg")
pygame.init()
game_width = 1280
game_height = 720
size = (game_width, game_height)
game_display = pygame.display.set_mode(size)
display_width = 1280
display_height = 720
White = (255,255,255)
Black = (0,0,0)
Blue = (0,0,255)
Red = (255,0,0)
Green = (0,255,0)

def Menu():
    game_intro()

def instructies():
    game_width = 1280
    game_height = 720
    size = (game_width, game_height)
    pygame.init()
    game_display.blit(background_image, [0,0])

    while not process_events():
        pygame.display.update()
        button("Menu",1120,10,150,60,White,Green,5,Menu)
        pygame.display.flip()
        clock.tick(60)

def highscores():
    game_width = 1280
    game_height = 720
    size = (game_width, game_height)
    pygame.init()
    game_display.blit(background_image, [0,0])

    while not process_events():
        pygame.display.update()
        button("Menu",1120,10,150,60,White,Green,5,Menu)
        pygame.display.flip()
        clock.tick(60)

def instellingen():
    game_width = 1280
    game_height = 720
    size = (game_width, game_height)
    pygame.init()
    game_display.blit(background_image, [0,0])

    while not process_events():
        pygame.display.update()
        button("Menu",1120,10,150,60,White,Green,5,Menu)
        pygame.display.flip()
        clock.tick(60)

def quit_game():
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, White)
    return textSurface, textSurface.get_rect()

def text_objects1(text, font):
    textSurface = font.render(text, True, Black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,l,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(game_display, ac,(x,y,w,h),l)
        if click[0] == 1 and action != None:
            action()
    else:     
        pygame.draw.rect(game_display, ic,(x,y,w,h),l)

    smallText = pygame.font.SysFont("Bauhaus93",20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    game_display.blit(TextSurf, TextRect)

mouse = pygame.mouse.get_pos()

def game_intro(): 

    intro = False

    while not intro:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = True
                 
        game_display.blit(background_image, [0,0])
        largeText = pygame.font.SysFont('Bauhaus93',155)
        TextSurf, TextRect = text_objects("Battleport", largeText)
        TextRect.center = ((game_width/2),(game_height/2.5))
        game_display.blit(TextSurf, TextRect)
                                          
        largeText = pygame.font.SysFont('Bauhaus93',150)
        TextSurf, TextRect = text_objects1("Battleport", largeText)
        TextRect.center = ((game_width/2),(game_height/2.5))
        game_display.blit(TextSurf, TextRect)
        
        button("Instellingen",490,540,150,60,White,Green,5,instellingen)
        button("Instructies",690,540,150,60,White,Green,5,instructies)
        button("Highscores",910,540,150,60,White,Green,5,highscores)
        button("Start Spel",270,540,150,60,White,Green,5,program)
        button("Stop Spel",1120,650,150,60,White,Green,5,quit_game)

        pygame.display.update()
        clock.tick(15)

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

'''
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((game_width/2), (game_height/2))
    game_display.blit (TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    program()
'''

def program():
    game_width = 1280
    game_height = 720
    size = (game_width, game_height)

    pygame.init()

    game_display = pygame.display.set_mode(size)

    while not process_events():
        pygame.display.update()
        game_display.fill(Black)
 

        for y in range(20):
            for x in range(20):
                rect = pygame.Rect(x*(20+5), y*(20+5), 20, 20)
                pygame.draw.rect(game_display, White, rect)
                rect.center = ((game_width/2), (game_height/2))
        button("Menu",1120,10,150,60,White,Green,5,Menu)
        pygame.display.flip()
        clock.tick(60)

game_intro()        
program()