import pygame
import time
from setuptools.command import rotate

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

image_file = "schip1.png"
background = pygame.image.load("battleship-045.jpg")
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Battleport')
clock = pygame.time.Clock()

def grid():
    for y in range(20):
        for x in range(20):
            rect = pygame.Rect(x * gridSize + width / 2 - gridX * gridSize / 2, y * gridSize + height / 2 - gridY * gridSize / 2, tileSize, tileSize)
            pygame.draw.rect(screen, white, rect)

def Menu():
    game_intro()

def SelecteerBootje():
    return 0

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
    #print(click)
    
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

# de logica om te kijken of een bootje geselecteerd is hetzelfde als de logic van de button die hierboven beschreven staat.
# if click[0] == 1 -> is de logica om te kijken of er op de button is geklikt. Hieronder wordt een action() uitgevoerd
# zorg er voor dat deze action de functionaliteit bevat om een bootje te bewegen, zodat als je op het bootje klikt je vervolgens het bootje kan bewegen.




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

class bootje:
    def __init__ (self, ship_x, ship_y, maxSteps):
        self.ship_x = ship_x
        self.ship_y = ship_y
        self.maxSteps = maxSteps
        self.rotate = rotate
        self.ship_active = False
    
    def ship(self, w, h, ic, ac, action=None):
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
    
        if self.ship_x + w > mouse[0] > self.ship_x and self.ship_y + h > mouse[1] > self.ship_y:
            pygame.draw.rect(screen, ac,(self.ship_x, self.ship_y, w, h))
            if click[0] == 1:
                self.ship_active = True
                return
        else:
            if click[0] == 1:
                self.ship_active = False

        if self.ship_active:
             pygame.draw.rect(screen, blue,(self.ship_x, self.ship_y, w, h))
        else:
             pygame.draw.rect(screen, ic,(self.ship_x, self.ship_y, w, h))

    def move(self):
        if not self.maxSteps == 0:
            if self.ship_active:
                keys = pygame.key.get_pressed()
                if keys [pygame.K_LEFT]:
                    self.ship_x = self.ship_x - 25
                    self.ship_active = False
                    self.maxSteps = self.maxSteps - 1
                    screen.fill(black)
                    grid()            
                if keys[pygame.K_RIGHT]:
                    self.ship_x = self.ship_x + 25
                    self.ship_active = False
                    self.maxSteps = self.maxSteps - 1
                    screen.fill(black)
                    grid()
                if keys[pygame.K_UP]:
                    self.ship_y = self.ship_y - 25
                    self.ship_active = False
                    self.maxSteps = self.maxSteps - 1
                    screen.fill(black)
                    grid()
                if keys[pygame.K_DOWN]:
                    self.ship_y = self.ship_y + 25
                    self.ship_active = False
                    self.maxSteps = self.maxSteps - 1
                    screen.fill(black)
                    grid()
                if keys[pygame.K_SPACE]:
                    ????

# process events
def process_events():
    #boot = b
    #global ship_x
    #global ship_y
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        return False


# game program
def program():
    screen.fill(black)       
    grid()
    bootje1 = bootje(390, 110, 3)
    bootje2 = bootje(440, 110, 2)
    bootje3 = bootje(490, 110, 2)
    bootje4 = bootje(540, 110, 1)

    bootje5 = bootje(390, 560, 3)
    bootje6 = bootje(440, 535, 2)
    bootje7 = bootje(490, 535, 2)
    bootje8 = bootje(540, 510, 1)


    while not process_events():

        bootje1.ship(20, 45, red, green, None)
        bootje2.ship(20, 70, red, green, None)
        bootje3.ship(20, 70, red, green, None)
        bootje4.ship(20, 95, red, green, None)

        bootje5.ship(20, 45, red, green, None)
        bootje6.ship(20, 70, red, green, None)
        bootje7.ship(20, 70, red, green, None)
        bootje8.ship(20, 95, red, green, None)

        bootje1.move()
        bootje2.move()
        bootje3.move()
        bootje4.move()

        bootje5.move()
        bootje6.move()
        bootje7.move()
        bootje8.move()


        button("Menu", 1120, 10, 150, 60, white, green, 5, Menu)
        pygame.display.flip()
        clock.tick(fps)




game_intro()
program()
pygame.quit()
quit()