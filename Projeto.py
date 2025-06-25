import pygame
class Jogador(object):
    
    def __init__(self):
        
        self.sprite=pygame.image.load("data\ps1.png")
        self.x = 0
        self.y = 0
    def handle_keys(self):
        key = pygame.key.get_pressed()
        distancia = 5
        if key[pygame.K_DOWN]: 
            self.y += distancia 
        elif key[pygame.K_UP]: 
            self.y -= distancia 
        if key[pygame.K_RIGHT]: 
            self.x += distancia 
        elif key[pygame.K_LEFT]: 
            self.x -= distancia 

    def draw(self, surface):
       surface.blit(self.sprite, (self.x, self.y))
        
class Wall(object):
    
     def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 30, 30)

pygame.init()
tela=pygame.display.set_mode((1920,1080))
icon=pygame.image.load('data\MARK.jpg')
x=627
y=900
walls=[]
level1 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                  W       K           W", 
"W   W     WWWWWW   W WWWWWWWWWWWWWWWWWWW",
"W   W           W                 W    W",
"W   W         WWW         WW     W     W",
"WWWWW  WWWWWWWWWWWW                    W",
"W   W     W        WWWWWWWWWWWWWWWWWWWWW",
"W   W     W   WWW                      W",
"W   WWW WWW   W W       WWWWWWWWWW     W",
"W         W   W W     W       WWWWWWWW W",
"WWWWW W       W W     W                W",
"WW      WW      W  WWWWWWWWWWWWWWWWWWW W",
"W WWWW WWWW   WWW                      W",
"W     W        WWWWWWWWWWWWWWWWWWWWWW  W",                                      
"W     W                                W",
"W     WWWWWWWWWWWWWWWWW                W",
"W                        WWWWW     WW  W",
"W     WWWWWWWWWWWWWWWWWWW              W",
"W                         WW           W",
"W  WWWWWWWWWWWW               WWWWWWWWWW",
"W              WWWWWWWWWWWWWWWWWWW     W",
"W                                     W",
"WWWWWWWWWWWWWWWWW      WWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]
pygame.display.set_icon(icon)
def Menu ():

 menu=pygame.image.load ('menu.jpg')
 tela.blit(menu,(0,0))

 pygame.display.update()
def st1(level,):
 tela.fill((0,0,0))
 x = y = 0
 for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
       
     
        x += 30
    y +=30 
    x = 0

st1(level1)
menuOn=True
nivel=True
rodar=True
jogador=Jogador()
while rodar:
    
    for controle in pygame.event.get():
        if controle.type==pygame.QUIT:
            rodar=False
        if controle.type == pygame.KEYDOWN and controle.key == pygame.K_ESCAPE:
            rodar=False
    
        if menuOn:
             Menu()
             ponteiro=menu=pygame.image.load ('data\psMenu.png')
             tela.blit(ponteiro,(x,y))
             if controle.type == pygame.KEYDOWN and controle.key == pygame.K_RIGHT and menuOn==True:
                
                if x==100:
                    x=627
                    y=900
                elif x==627:
                    x=1170
                    y=900
             if controle.type == pygame.KEYDOWN and controle.key == pygame.K_LEFT and menuOn==True:
                
                if x==1170:
                    x=627
                    y=900
                elif x==627:
                    x=100
                    y=900
             pygame.display.flip()
     
        if x==627 and controle.type == pygame.KEYDOWN and controle.key == pygame.K_SPACE:
                 menuOn=False
                 tela.fill('black')
                 jogador.draw(tela)
                 jogador.handle_keys()
   
                 pygame.display.flip()

pygame.quit()




