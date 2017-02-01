import pygame
import time
# import psycopg2


#database

# Use the database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=Battleport user=postgres password=hoi")
    cursor = connection.cursor()
    
    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass
    print(results)
    # Close connection
    cursor.close()
    connection.close()
    
    return results


# Uploads a score into the hiscore table
#def upload_score(name, score):
#    interact_with_database("UPDATE score SET score = {} WHERE name = '{}'"
#                           .format(score, name))


# Downloads score data from database
def download_scores(statement):
    return interact_with_database(statement)


# Downloads the top score from database
#def download_top_score():
#    result = interact_with_database("SELECT * FROM score ORDER BY score")[0][1]
#    return result



pygame.init()

width = 1280
height = 720
fps = 60

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
light_blue = (65,105,225)
light_red = (240,128,128)

# Grids
gridY = 20
gridX = 20
gridSize = 25
tileSize = 20

turnPlayer1 = True
turnPlayer2 = False

img = pygame.image.load("Naamloos.png")
special = {"1": "!","2": "@","3": "#","4": "$","5": "%","6": "^","7": "&","8": "*","9": "(","0": ")","`": "~","-": "_","=": "+",",": "<",".": ">","/": "?",";": ":","'": chr(34),"[": "{","]": "}",chr(92): "|"}
myfont=pygame.font.SysFont(None,30)
background = pygame.image.load("battleship-045.jpg")
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Battleport')
clock = pygame.time.Clock()


def grid():
    for y in range(20):
        for x in range(20):
            rect = pygame.Rect(x * gridSize + width / 2 - gridX * gridSize / 2, y * gridSize + height / 2 - gridY * gridSize / 2, tileSize, tileSize)
            pygame.draw.rect(screen, white, rect)

def text(message):
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
        my_string = message 
        my_rect = pygame.draw.rect(screen, black,[325,105,630,490])
    
        rendered_text = render_textrect(my_string, my_font, my_rect, (216, 216, 216), (48, 48, 48), 0)

        if rendered_text:
            screen.blit(rendered_text, my_rect.topleft)

        pygame.display.update()

def Menu():
    game_intro()

def SelecteerBootje():
    return 0

def Verder():
    size = (width, height)
    pygame.init()
    screen.blit(background, [0, 0])
    pygame.draw.rect(screen, white,[320,100,640,500])

    text("Regels \n\n\nblabla\n\nTekst moet nog gewijzigd worden.\n\nBattleport kan gezien worden als een mix van Zeeslag en Hearthstone. Dit omdat de gameplay lijkt op dat van Zeeslag, maar kunnen de boten nu ook verplaatst worden. Ook zijn er twee decks met kaarten die jou helpen om van je tegenstander te winnen.\n\nBeide spelers hebben vier boten en een hand met kaarten. De bedoeling van dit strategische spel in om alle schepen van je tegenstander uit te schakelen. Zet tactische zetten en gebruik je kaarten slim. Doe dit beter dan je tegenstander en de winst is voor jou.")

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

    text("Instructies \n\n\nBattleport kan gezien worden als een mix van Zeeslag en Hearthstone. Dit omdat de gameplay lijkt op dat van Zeeslag, maar kunnen de boten nu ook verplaatst worden. Ook zijn er twee decks met kaarten die jou helpen om van je tegenstander te winnen.\n\nBeide spelers hebben vier boten en een hand met kaarten. De bedoeling van dit strategische spel in om alle schepen van je tegenstander uit te schakelen. Zet tactische zetten en gebruik je kaarten slim. Doe dit beter dan je tegenstander en de winst is voor jou.")

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
    message_display("Highscores",'bauhaus93',75,white)
    highscore1 = download_scores(" SELECT * FROM highscore WHERE name = 'Sven'")
    highscore2 = download_scores(" SELECT * FROM highscore WHERE name = 'Maaike'")
    highscore3 = download_scores(" SELECT * FROM highscore WHERE name = 'Jennifer'")

    font = pygame.font.SysFont('bauhaus93', 50)
    score_text1 = font.render((str(highscore1)),1, (255, 255, 255))
    score_text2 = font.render((str(highscore2)),1, (255, 255, 255))
    score_text3 = font.render((str(highscore3)),1, (255, 255, 255))
    screen.blit(score_text1, (475, 300))
    screen.blit(score_text2, (475, 400))
    screen.blit(score_text3, (475, 500))
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
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text,font,size,color):
    largeText = pygame.font.SysFont(font,size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((width/2), (height/3.5))
    screen.blit (TextSurf, TextRect)


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
    textSurf, textRect = text_objects(text, smallText, white)
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
        message_display("Battleport","bauhaus93",130,white)    
        message_display("Battleport","bauhaus93",125,black)  

        mouse = pygame.mouse.get_pos()

        button("Start Spel", 150, 550, 150, 50, white, green, 5, name_input)
        button("Instructies", 350, 550, 150, 50, white, green, 5, instructies)
        button("Highscores", 550, 550, 150, 50, white, green, 5, highscores)
        button("Instellingen", 750, 550, 150, 50, white, green, 5, instellingen)
        button("Stop Spel", 950, 550, 150, 50, white, green, 5, quit)
        

        pygame.display.update()
        clock.tick(fps)

class vloot:
    def __init__(self,team):
        self.team = team
        self.Total = 4

        if self.team == red:
            self.Boats = [\
            bootje(390, 110, 2, red,2),\
            bootje(440, 110, 3, red,3),\
            bootje(490, 110, 3, red,3),\
            bootje(540, 110, 4, red,4)]
        else:
            self.Boats = [\
            bootje(390, 560, 2, blue,2),\
            bootje(440, 535, 3, blue,3),\
            bootje(490, 535, 3, blue,3),\
            bootje(540, 510, 4, blue,4)]

    def ships(self, action = None):
        if action == "move":
            if self.team == blue:
                for ship in self.Boats:
                    ship.ship(self.team,green,light_blue, ship.move)
            else:
                for ship in self.Boats:
                    ship.ship(self.team,green,light_red, ship.move)
        elif action == "attack":
            if self.team == blue:
                for ship in self.Boats:
                    ship.ship(self.team,green,light_blue, ship.attack)
            else:
                for ship in self.Boats:
                    ship.ship(self.team,green,light_red, ship.attack)
        else:
            if self.team == blue:
                for ship in self.Boats:
                    ship.ship(self.team,green,light_blue)
            else:
                for ship in self.Boats:
                    ship.ship(self.team,green,light_red)



class bootje:
    def __init__ (self, ship_x, ship_y, length, team, hp):
        self.ship_x = ship_x
        self.ship_y = ship_y
        self.width = 20
        self.height = length * 20 + (length - 1) * 5
        self.ship_active = False
        self.zetten = 0
        self.steps = (5-length)
        self.length = length
        self.bonus = 0
        self.stance = "attack"
        self.team = team
        self.hp = length
        self.damage = 1
        

    def ship(self, ic, ac, mc, action=None):
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.ship_x + self.width > mouse[0] > self.ship_x and self.ship_y + self.height > mouse[1] > self.ship_y:
            screen.blit(img,[0,0])
            hp_str = "HP:"+str(self.hp)
            texttt=myfont.render(hp_str,True,[255,0,0]) 
            screen.blit(texttt,[20,20])
            pygame.draw.rect(screen, mc,(self.ship_x, self.ship_y, self.width, self.height))
            if click[0] == 1 and action != None:
                self.ship_active = True
                if self.hp <= 0:
                    self.ship_active = False
        else:
            if click[0] == 1 and action != None:
                self.ship_active = False
        if self.steps == 0:
            pygame.draw.rect(screen, ic,(self.ship_x, self.ship_y, self.width, self.height))
        else:
            if self.ship_active:
                pygame.draw.rect(screen, ac,(self.ship_x, self.ship_y, self.width, self.height)) 
            elif self.ship_x + self.width > mouse[0] > self.ship_x and self.ship_y + self.height > mouse[1] > self.ship_y:
                pygame.draw.rect(screen, mc,(self.ship_x, self.ship_y, self.width, self.height))
            else:
                pygame.draw.rect(screen, ic,(self.ship_x, self.ship_y, self.width, self.height))

        if self.ship_active:
            action()


    def change_stance(self):
        if self.team == red:
            print("red")
            if self.stance == "attack":
                print("defense")
                self.ship_y += (self.length - 1) * 20 + (self.length - 2) * 5 + 5
                w = self.width
                h = self.height
                self.height = w
                self.width = h
                self.stance = "defense"
                self.ship_active = False
                screen.fill(black)
                grid()
            else:
                print("attack")
                self.ship_y -= (self.length - 1) * 20 + (self.length - 2) * 5 + 5
                w = self.width
                h = self.height
                self.height = w
                self.width = h
                self.stance = "attack"
                self.ship_active = False
                screen.fill(black)
                grid()
        if self.team == blue:
            print("blue")
            if self.stance == "attack":
                print("defense")
                self.ship_y += (self.length - 1) * -5 + (self.length - 2) * 5 + 5
                w = self.width
                h = self.height
                self.height = w
                self.width = h
                self.stance = "defense"
                self.ship_active = False
                screen.fill(black)
                grid()
            else:
                print("attack")
                self.ship_y -= (self.length - 1) * -5 + (self.length - 2) * 5 + 5
                w = self.width
                h = self.height
                self.height = w
                self.width = h
                self.stance = "attack"
                self.ship_active = False
                screen.fill(black)
                grid()

    def attack(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            print("z")
            if self.ship_active == True:
                print("ouch")
                self.hp = self.hp - 1
                print("attacking")
                self.ship_active = False
            
            if self.hp <= 0:
                print("boom")
                self.ship_active = False
                self.destroyed()


    def destroyed(self):
        self.ship_active = False
        print("derp")
        if self.team == blue:
            blueteam.Total -= 1
            print("lost ship")
        if self.team == red:
            redteam.Total -= 1
            print("lost shippp")
    

    def move(self):
        if self.zetten != self.steps +self.bonus:
            if self.ship_active:
                keys = pygame.key.get_pressed()
                if keys [pygame.K_LEFT]:
                    print("left")
                    if self.ship_x - 25 >= 385:
                        self.ship_x = self.ship_x - 25
                        self.zetten = self.zetten + 1
                        self.ship_active = False
                        screen.fill(black)
                        grid()            
                elif keys[pygame.K_RIGHT]:
                    print("right")
                    if self.ship_x + 45 <= 880:
                        self.ship_x = self.ship_x + 25
                        self.zetten = self.zetten + 1
                        self.ship_active = False
                        screen.fill(black)
                        grid()
                elif keys[pygame.K_UP]:
                    print("up")
                    if self.ship_y - 25 >= 105:
                        self.ship_y = self.ship_y - 25
                        self.zetten = self.zetten + 1
                        self.ship_active = False
                        screen.fill(black)
                        grid()
                elif keys[pygame.K_DOWN]:
                    print("down")
                    if self.ship_y + 20 * (self.length - 1) + 25 <= 600:
                        self.ship_y = self.ship_y + 25
                        self.zetten = self.zetten + 1
                        self.ship_active = False
                        screen.fill(black)
                        grid()
                elif keys[pygame.K_SPACE]:
                    print("key pressed")
                    self.change_stance()

blueteam = vloot(blue)
redteam = vloot(red)

# process events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        return False

def name_input():
    class input_page:
        def __init__(self):
            self.lst = []
            self.current = 0

        def get_input(self,event,mouse_pos):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_TAB:
                    if self.current < len(self.lst)-1:
                        self.current += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(self.lst)):
                    if self.lst[i].rect.collidepoint(mouse_pos):
                        self.lst[i].current = True
                        self.current = i
                        for g in range(len(self.lst)):
                            if g != i:
                                self.lst[g].current = False

            for i in range(len(self.lst)):
                if i == self.current:
                    self.lst[i].current = True
                    self.lst[i].get_input(event)
                    for g in range(len(self.lst)):
                        if g != i:
                            self.lst[g].current = False

        def render(self,screen):
            for i in range(len(self.lst)):
                self.lst[i].render(screen)

    class text_box:
        def __init__(self,location,width,height,question = None,text_color = (255,255,255), font = None,font_size = 20):
            self.location = location
            self.text = ""
            self.question = question
            self.current = False
            self.rect = pygame.Rect((location),(width,max(height,25)))
            self.font_size = font_size
            self.font = pygame.font.Font(font,font_size)
            self.text_color = text_color
            self.outline = (255,255,255)
            self.rect_color = (0,0,0)

        def render(self,screen):
            if self.current == True:
                temp = (self.rect[0]-3,self.rect[1]-3,self.rect[2]+6,self.rect[3]+6)
                pygame.draw.rect(screen,(255,105,34),temp)
            pygame.draw.rect(screen,self.rect_color,self.rect)
            pygame.draw.rect(screen,self.outline,self.rect,1)
            screen.blit(self.font.render(self.question,1,self.text_color),(self.location[0]-self.font.size(self.question)[0]-100,self.location[1]+4))
            screen.blit(self.font.render(self.text,1,self.text_color),(self.location[0]+2,self.location[1]+4))
        def get_input(self,event):
            if event.type == pygame.KEYDOWN:
                if 31<event.key<127 and event.key != 8:
                    if event.mod & (pygame.KMOD_SHIFT | pygame.KMOD_CAPS):
                        if chr(event.key) in special.keys():
                            self.text += special[chr(event.key)]
                        else:
                            self.text += chr(event.key).upper()
                    else:
                        self.text += chr(event.key)
                if event.key == 8:
                    self.text = self.text[0:-1]
                if event.key == 127:
                    self.text = ""
                if self.font.size(self.text)[0] > self.rect.size[0]-5:
                    self.text = self.text[0:-1]
    inp = input_page()
    text = text_box((int(width/1.75),height/2-25),200,25,"Player 1 Name: ")
    text2 = text_box((int(width/1.75),height/2+25),200,25,"Player 2 Name: ")
    global text
    global text2
    inp.lst = [text,text2]

    done = False
    while done == False:
        screen.fill((0,0,0))
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            inp.get_input(event,pos)

        inp.render(screen)
        button("Menu", 1120, 10, 150, 60, white, green, 5, Menu)
        button("Ready!", 1120, 650, 150, 60,white,green,5, program)
        pygame.display.flip()
        clock.tick(fps)

def program():
    screen.fill(black)  
    grid()

    while not process_events():
        screen.blit(img,[765,0])
        redships = "Ships left:"+str(redteam.Total)
        texttt=myfont.render(redships,True,[255,0,0]) 
        screen.blit(texttt,[770,60])

        screen.blit(img,[770,645])
        blueships = "Ships left:"+str(blueteam.Total)
        texttt=myfont.render(blueships,True,[255,0,0]) 
        screen.blit(texttt,[770,645])

        if turnPlayer1 == True:
            redteam.ships("move")
            blueteam.ships("attack")

        if turnPlayer2 == True:
            redteam.ships("attack")
            blueteam.ships("move")

        button("Menu", 1120, 10, 150, 60, white, green, 5, Menu)
        button("Pass turn", 10, 650, 175, 60,white,green,5, turn_change)
        button(text.text, 375, 30, 150, 75, black, black, 5)
        button(text2.text, 375, 620, 150, 75, black, black, 5)

        if blueteam.Total <= 0:
            win()
        if redteam.Total <= 0:
            win()

        pygame.display.flip()
        clock.tick(fps)

def player2True():
    global turnPlayer1
    global turnPlayer2
    turnPlayer2 = True
    turnPlayer1 = False
    program()
def player1True():
    global turnPlayer1
    global turnPlayer2
    turnPlayer2 = False
    turnPlayer1 = True
    program()
def turn_change():
    screen.fill(black)

    for ship in blueteam.Boats:
        ship.zetten = 0
    for ship in redteam.Boats:
        ship.zetten = 0

    while not process_events():
        if turnPlayer1 == True:
            button("Ready P2", 500,500,300,50, white, green, 5, player2True)
        if turnPlayer2 == True:
            button("Ready P1", 500,500,300,50, white, green, 5, player1True)

        pygame.display.flip()
   
def win():
    if blueteam.Total <= 0:
        size = (width, height)
        pygame.init()
        screen.blit(background, [0, 0])
        message_display("JE HEBT GEWONNEN" + (text.text),"bauhaus93",130,white)    
        message_display("JE HEBT GEWONNEN" + (text.text),"bauhaus93",125,black)
        button("Terug naar menu", 1120, 10, 150, 60, white, green, 5, Menu)
        
        
        
        
        
             
game_intro()
program()


pygame.quit()
quit()