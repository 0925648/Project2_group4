import pygame
import time

pygame.init()

width = 1250
height = 720

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)

# Grids
gridY = 20
gridX = 20
gridSize = 25
tileSize = 20


background = pygame.image.load("battleship-045.jpg")
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Battleport')
clock = pygame.time.Clock()


def Menu():
    game_intro()


# instructions menu
def instructies():
    size = (width, height)
    pygame.init()
    screen.blit(background, [0,0])

    while not process_events():
        pygame.display.update()
        button("Menu", 1075, 10, 150, 60, white, green, 5, Menu)
        pygame.display.flip()
        clock.tick(60)


# highscores menu
def highscores():
    size = (width, height)
    pygame.init()
    screen.blit(background, [0,0])

    while not process_events():
        pygame.display.update()
        button("Menu", 1075, 10, 150, 60, white, green, 5, Menu)
        pygame.display.flip()
        clock.tick(60)

# settings menu
def instellingen():
    size = (width, height)
    pygame.init()
    screen.blit(background, [0,0])

    while not process_events():
        pygame.display.update()
        button("Menu", 1075, 10, 150, 60, white, green, 5, Menu)
        pygame.display.flip()
        clock.tick(60)


# intro "Battleport" text
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def text_objects1(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# button functionality
def button(text, x, y, w, h, ic, ac, l, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x, y, w, h), l)
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x, y, w, h), l)

    smallText = pygame.font.SysFont("bauhaus93",20)
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)



# menu screen
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.blit(background, [0,0])
        largeText = pygame.font.SysFont('bauhaus93',130)
        TextSurf, TextRect = text_objects("Battleport", largeText)
        TextRect.center = ((width/2),(height/3.5))
        screen.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont('Bauhaus93',125)
        TextSurf, TextRect = text_objects1("Battleport", largeText)
        TextRect.center = ((width/2),(height/3.5))
        screen.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        #print(mouse)

        button("Start Spel", 150, 550, 150, 50, white, green, 5, program)
        button("Instructies", 350, 550, 150, 50, white, green, 5, instructies)
        button("Highscores", 550, 550, 150, 50, white, green, 5, highscores)
        button("Instellingen", 750, 550, 150, 50, white, green, 5, instellingen)
        button("Stop Spel", 950, 550, 150, 50, white, green, 5, quit)
        

        pygame.display.update()
        clock.tick(60)



# process events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False




# game program
def program():
    while not process_events():
        pygame.display.update()
        screen.fill(black)

        for y in range(20):
            for x in range(20):
                rect = pygame.Rect(x * gridSize + width / 2 - gridX * gridSize / 2, y * gridSize + height / 2 - gridY * gridSize / 2, tileSize, tileSize)
                pygame.draw.rect(screen, white, rect)

        button("Menu", 1075, 10, 150, 60, white, green, 5, Menu)
        pygame.display.flip()
        clock.tick(60)



game_intro()
program()
pygame.quit()
quit()