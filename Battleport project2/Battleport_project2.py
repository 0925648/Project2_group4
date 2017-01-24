import pygame
import pygame.font
from pygame.locals import *
import time

pygame.init()

width = 1280
height = 720
fps = 60

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


def Verder():
    size = (width, height)
    pygame.init()
    screen.blit(background, [0, 0])
    pygame.draw.rect(screen, white,[320,100,640,500])


    def render_textrect(string, font, rect, text_color, background, justification=0):
    
        final_lines = []
        requested_lines = string.splitlines()

        for requested_line in requested_lines:
            if font.size(requested_line)[0] > rect.width:
                words = requested_line.split(' ')
                # Start a new line
                accumulated_line = ""
                for word in words:
                    test_line = accumulated_line + word + " "
                    # Build the line while the words fit.    
                    if font.size(test_line)[0] < rect.width:
                        accumulated_line = test_line 
                    else: 
                        final_lines.append(accumulated_line) 
                        accumulated_line = word + " " 
                final_lines.append(accumulated_line)
            else: 
                final_lines.append(requested_line) 

        # Let's try to write the text out on the surface.

        surface = pygame.Surface(rect.size) 
        surface.fill(black) 

        accumulated_height = 0 
        for line in final_lines: 
            if accumulated_height + font.size(line)[1] >= rect.height:
                raise TextRectException
            if line != "":
                tempsurface = font.render(line, 1, text_color)
                if justification == 0:
                    surface.blit(tempsurface, (0, accumulated_height))
                elif justification == 1:
                    surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
                elif justification == 2:
                    surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
                else:
                    raise TextRectException 
            accumulated_height += font.size(line)[1]
        return surface
    # text has  to be editted. Not correct yet! 
    if __name__ == '__main__':
        my_font = pygame.font.Font(None, 30)
        my_string = "Regels \n\n\nblabla\n\nTekst moet nog gewijzigd worden.\n\nBattleport kan gezien worden als een mix van Zeeslag en Hearthstone. Dit omdat de gameplay lijkt op dat van Zeeslag, maar kunnen de boten nu ook verplaatst worden. Ook zijn er twee decks met kaarten die jou helpen om van je tegenstander te winnen.\n\nBeide spelers hebben vier boten en een hand met kaarten. De bedoeling van dit strategische spel in om alle schepen van je tegenstander uit te schakelen. Zet tactische zetten en gebruik je kaarten slim. Doe dit beter dan je tegenstander en de winst is voor jou."
        my_rect = pygame.draw.rect(screen, black,[325,105,630,490])
    
        rendered_text = render_textrect(my_string, my_font, my_rect, (216, 216, 216), (48, 48, 48), 0)

        if rendered_text:
            screen.blit(rendered_text, my_rect.topleft)

        pygame.display.update()

    while not process_events():
        pygame.display.update()                        
        button("Menu",1120,10,150,60,white,green,5,Menu)
        button("Vorige", 10, 650, 150, 60,white,green,5,Vorige)
        pygame.display.flip()
        clock.tick(fps)



def Vorige():
    size = (width, height)
    pygame.init()
    screen.blit(background, [0, 0])

    while not process_events():
        instructies()



# instructions menu
def instructies():
    size = (width, height)
    pygame.init()
    screen.blit(background, [0,0])
    pygame.draw.rect(screen, white,[320,100,640,500])


    def render_textrect(string, font, rect, text_color, background, justification=0):
    
        final_lines = []
        requested_lines = string.splitlines()

        for requested_line in requested_lines:
            if font.size(requested_line)[0] > rect.width:
                words = requested_line.split(' ')
                # Start a new line
                accumulated_line = ""
                for word in words:
                    test_line = accumulated_line + word + " "
                    # Build the line while the words fit.    
                    if font.size(test_line)[0] < rect.width:
                        accumulated_line = test_line 
                    else: 
                        final_lines.append(accumulated_line) 
                        accumulated_line = word + " " 
                final_lines.append(accumulated_line)
            else: 
                final_lines.append(requested_line) 

        # Let's try to write the text out on the surface.

        surface = pygame.Surface(rect.size) 
        surface.fill(black) 

        accumulated_height = 0 
        for line in final_lines: 
            if accumulated_height + font.size(line)[1] >= rect.height:
                raise TextRectException
            if line != "":
                tempsurface = font.render(line, 1, text_color)
                if justification == 0:
                    surface.blit(tempsurface, (0, accumulated_height))
                elif justification == 1:
                    surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
                elif justification == 2:
                    surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
                else:
                    raise TextRectException 
            accumulated_height += font.size(line)[1]
        return surface



    if __name__ == '__main__':
        my_font = pygame.font.Font(None, 30)
        my_string = "Instructies \n\n\nBattleport kan gezien worden als een mix van Zeeslag en Hearthstone. Dit omdat de gameplay lijkt op dat van Zeeslag, maar kunnen de boten nu ook verplaatst worden. Ook zijn er twee decks met kaarten die jou helpen om van je tegenstander te winnen.\n\nBeide spelers hebben vier boten en een hand met kaarten. De bedoeling van dit strategische spel in om alle schepen van je tegenstander uit te schakelen. Zet tactische zetten en gebruik je kaarten slim. Doe dit beter dan je tegenstander en de winst is voor jou."
        my_rect = pygame.draw.rect(screen, black,[325,105,630,490])
    
        rendered_text = render_textrect(my_string, my_font, my_rect, (216, 216, 216), (48, 48, 48), 0)

        if rendered_text:
            screen.blit(rendered_text, my_rect.topleft)

        pygame.display.update()

       

    while not process_events():
        pygame.display.update()
        button("Menu", 1120, 10, 150, 60, white, green, 5, Menu)
        button("Verder", 1120, 650, 150, 60,white,green,5,Verder)
        pygame.display.flip()
        clock.tick(fps)


# highscores menu
def highscores():
    size = (width, height)
    pygame.init()
    screen.blit(background, [0,0])

    while not process_events():
        pygame.display.update()
        button("Menu", 1120, 10, 150, 60, white, green, 5, Menu)
        pygame.display.flip()
        clock.tick(fps)

# settings menu
def instellingen():
    size = (width, height)
    pygame.init()
    screen.blit(background, [0,0])

    while not process_events():
        pygame.display.update()
        button("Menu", 1120, 10, 150, 60, white, green, 5, Menu)
        pygame.display.flip()
        clock.tick(fps)


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
        clock.tick(fps)



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

        button("Menu", 1120, 10, 150, 60, white, green, 5, Menu)
        pygame.display.flip()
        clock.tick(fps)





game_intro()
program()
pygame.quit()
quit()