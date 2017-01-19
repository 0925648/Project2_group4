import pygame
import time
pygame.init()

# Screen resolution
width = 1250
height = 720

# colors
black = (0,0,0)
white = (255,255,255)
yellow = (200, 200, 0)
bright_yellow = (255, 255, 0)

background = pygame.image.load("battleship-045.jpg")
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Battleport')
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()



# defining button: x & y = location top left position, 
# w = button width, h = button height, ic = inactive color, ac = active color
def button(text, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x, y, w, h))
    smallText = pygame.font.SysFont("bauhaus93",20)
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)



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

        # Mouse position
        mouse = pygame.mouse.get_pos()
        #print(mouse)
        # Buttons which don't work yet
        button("Start Game", 150, 550, 150, 50, yellow, bright_yellow) #game_loop
        button("Instructions", 350, 550, 150, 50, yellow, bright_yellow)
        button("Highscores", 550, 550, 150, 50, yellow, bright_yellow)
        button("Settings", 750, 550, 150, 50, yellow, bright_yellow)
        button("Quit",950,550,150,50,yellow,bright_yellow, quit)
        


        pygame.display.update()
        clock.tick(60)


game_intro()
pygame.quit()
quit()
