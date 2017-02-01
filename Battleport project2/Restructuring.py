import pygame
pygame.init()

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
light_blue = (65,105,225)
light_red = (240,128,128)
class Grid:
    def __init__(self,x,y):
        self.X = x
        self.Y = y
        self.Width = 20
        self.Tile_width = 25
        self.Color = white

        self.Tiles = [''] * 20

        tile_x = self.X
        tile_y = self.Y
        for x in range(0,self.Width):
            self.Tiles[x] = [''] * 20
            for y in range(0,self.Width):
                self.Tiles[x][y] = Tile(tile_x + 2.5, tile_y + 2.5, self.Tile_width - 5, self.Color)
                tile_y = tile_y + self.Tile_width
            tile_x = tile_x + self.Tile_width
            tile_y = self.Y

    def Draw(self):
        for x in self.Tiles:
            for y in x:
                y.Draw()

    def Change_color(self, x, y, color):
        self.Tiles[x][y].Color = color


class Tile:
    def __init__(self, x, y, w, color):
        self.X = x
        self.Y = y
        self.Width = w
        self.Color = color
    def Draw(self):
        pygame.draw.rect(game.Display, self.Color, (self.X, self.Y, self.Width, self.Width))


class Game:
    def __init__(self):
        self.FPS = 30
        self.Clock = pygame.time.Clock()
        self.Exit = False

        self.Width = 1280
        self.Height = 720
        self.Display = pygame.display.set_mode((self.Width, self.Height))

        self.Level = "menu"
        self.Turn = 1
    def End_turn(self):
        if self.Turn == 1: self.Turn = 2
        else: self.Turn = 1
    def Draw(self): self.Display.fill((0,0,0))
    def Tick(self): self.Clock.tick(self.FPS)
    def Loop(self):
        while not self.Exit:
            if self.Level == "menu":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.Exit = True
                    self.Draw() # DRAW JE SHIT HIER:
                    grid.Draw()


                    pygame.display.update()
                    self.Tick()
            elif self.Level == "game":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.Exit = True
                    self.Draw() # DRAW JE SHIT HIER:
                    



                    pygame.display.update()
                    self.Tick()
            else: game.Exit = True
# GLOBALE FUNCTIES HIERZO:




game = Game()
# INSTANTIERINGEN HIERZO:
grid = Grid(game.Width/2 - 250,game.Height / 2 - 250)




game.Loop()
pygame.quit()
quit()