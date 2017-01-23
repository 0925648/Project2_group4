import pygame
import time

clock=pygame.time.Clock()
background_image = pygame.image.load("battleship_045.jpg")
pygame.init()
game_width = 1280
game_height = 720
size = (game_width, game_height)
game_display = pygame.display.set_mode(size)

gridY = 20
gridX = 20
gridSize = 25
tileSize = 20

White = (255,255,255)
Black = (0,0,0)
Blue = (0,0,255)
Red = (255,0,0)
Green = (0,255,0)

def Verder():
    game_width = 1280
    game_height = 720
    size = (game_width, game_height)
    pygame.init()
    game_display.blit(background_image, [0,0])
    while not process_events():
        pygame.display.update()
        pygame.draw.rect(game_display, White,[320,100,640,500])
        pygame.draw.rect(game_display, Black,[325,105,630,490])

        largeText = pygame.font.SysFont('Bauhaus93',30)
        TextSurf, TextRect = text_objects("Hoe werkt het? Voorbereiding: Elke speler begint met vier boten en twee kaarten. Eerst pakken beide spelers twee kaarten van basis stapel.plaatsen beide spelers omstebeurt hun boten met de achterkant tegen eigen haven. We zijn nu klaar om te beginnen. Aanvallen en verdedigen: Tijdens het spelen van Battleport, kunnen de schepen in twee verschillende posities staan, aanvalspositie en verdedigingspositie. Aanvallend is simpel gezien de standaardpositie. Als je schip in deze positie staat, kan je normaal bewegen en aanvallen. Verdedigend maakt je schip geschikter om te verdedigen. Zo krijgt een schip in verdediging +1 range en heeft het een groter aanvals veld voor zich. Maar in verdediging mag niet meer bewegen. Een verdedigend schip mag ook alleen verticaal aanvallen.", largeText)
        TextRect.center = ((game_width/2),(game_height/2.5))
        game_display.blit(TextSurf, TextRect)
                                          
        button("Menu",1120,10,150,60,White,Green,5,Menu)
        pygame.display.flip()
        clock.tick(60)


def Menu():
    game_intro()

def instructies():
    game_width = 1280
    game_height = 720
    size = (game_width, game_height)
    pygame.init()
    game_display.blit(background_image, [0,0])
    pygame.draw.rect(game_display, White,[320,100,640,500])
    pygame.draw.rect(game_display, Black,[325,105,630,490])

    while not process_events():
        pygame.display.update()
        largeText = pygame.font.SysFont('Bauhaus93',30)
        TextSurf, TextRect = text_objects("Wat is battleport? Battleport kan gezien worden als een mix van Zeeslag en Hearthstone." + "\n" + "Dit omdat de gameplay lijkt op dat van Zeeslag, maar kunnen de boten nu ook verplaatst worden. Ook zijn er twee decks met kaarten die jou helpen om van je tegenstander te winnen. Beide spelers hebben vier boten en een hand met kaarten. De bedoeling van dit strategische spel in om alle schepen van je tegenstander uit te schakelen. Zet tactische zetten en gebruik je kaarten slim. Doe dit beter dan je tegenstander en de winst is voor jou", largeText)
        TextRect.center = ((game_width/2),(game_height/2.5))
        game_display.blit(TextSurf, TextRect)
        button("Menu",1120,10,150,60,White,Green,5,Menu)
        button("Verder",1120,650,150,60,White,Green,5,Verder)
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
        
        button("Start Spel",170,540,150,60,White,Green,5,program)
        button("Instellingen",770,540,150,60,White,Green,5,instellingen)
        button("Instructies",370,540,150,60,White,Green,5,instructies)
        button("Highscores",570,540,150,60,White,Green,5,highscores)
        button("Stop Spel",970,540,150,60,White,Green,5,quit_game)

        pygame.display.update()
        clock.tick(15)

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

'''
def message_display(text,font,size):
    largeText = pygame.font.Font(font,size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((game_width/2), (game_height/2))
    game_display.blit (TextSurf, TextRect)
'''

def program():
    game_width = 1280
    game_height = 720
    size = (game_width, game_height)
    pygame.init()
    game_display = pygame.display.set_mode(size)
    while not process_events():
        pygame.display.update()
        for y in range(gridY):
            for x in range(gridX):
                rect = pygame.Rect(x * gridSize + game_width / 2 - gridX * gridSize / 2, y * gridSize + game_height / 2 - gridY * gridSize / 2, tileSize, tileSize)
                pygame.draw.rect(game_display, White, rect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + tileSize  > click[0] > x and y + tileSize > click[1] > y:
            if click[0] == 1 and action != None:
                pygame.draw.rect(game_display, Blue,(x,y,tileSize,tileSize))

        pygame.draw.rect(game_display, White,[900,110,130,70])
        pygame.draw.rect(game_display, White,[900,195,130,70])
        pygame.draw.rect(game_display, White,[900,280,130,70])
        pygame.draw.rect(game_display, White,[900,365,130,70])
        pygame.draw.rect(game_display, White,[900,450,130,70])
        pygame.draw.rect(game_display, White,[900,535,130,70])
        pygame.draw.rect(game_display, White,[245,110,130,70])
        pygame.draw.rect(game_display, White,[245,195,130,70])
        pygame.draw.rect(game_display, White,[245,280,130,70])
        pygame.draw.rect(game_display, White,[245,365,130,70])
        pygame.draw.rect(game_display, White,[245,450,130,70])
        pygame.draw.rect(game_display, White,[245,535,130,70])

        pygame.draw.rect(game_display, Black,[905,115,120,60])
        pygame.draw.rect(game_display, Black,[905,200,120,60])
        pygame.draw.rect(game_display, Black,[905,285,120,60])
        pygame.draw.rect(game_display, Black,[905,370,120,60])
        pygame.draw.rect(game_display, Black,[905,455,120,60])
        pygame.draw.rect(game_display, Black,[905,540,120,60])
        pygame.draw.rect(game_display, Black,[250,115,120,60])
        pygame.draw.rect(game_display, Black,[250,200,120,60])
        pygame.draw.rect(game_display, Black,[250,285,120,60])
        pygame.draw.rect(game_display, Black,[250,370,120,60])
        pygame.draw.rect(game_display, Black,[250,455,120,60])
        pygame.draw.rect(game_display, Black,[250,540,120,60])
        button("Menu",1120,10,150,60,White,Green,5,Menu)
        pygame.display.flip()
        clock.tick(60)

game_intro()        
program()