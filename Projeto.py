import pygame
class Jogador(object):
    
    def __init__(self):
        
        self.sprite=pygame.image.load("data\ps1.png")
        
        self.x=340
        self.y=340
  

    def draw(self, surface):
       surface.blit(self.sprite, (self.x, self.y))

    def move(self, dx, dy):
        
        
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
     
        
        self.x += dx
        self.y += dy

       
       
class Wall(object):
    
     def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 30, 30)

pygame.init()
tela=pygame.display.set_mode((1920,1080))
icon=pygame.image.load('data\MARK.jpg')
x=627
y=900
ativo=False
walls=[]
level1 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                  W       K                                                 W",
"W                                                                            W",
"W                                                                            W",
"W   W     WWWWWW   W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                                                            W",
"W                                                                            W",
"W   W         WWW         WW     W                                           W",
"W                                                                            W",
"WWWWW  WWWWWWWWWWWW                    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                                                            W",
"W                  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W             WWW                                                            W",
"W                       WWWWWWWWWW                                           W",
"W                                                                            W",
"W               W     W       WWWWWWWW     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                                                            W",
"WWWWW W         W     W                                                      W",
"W               W  WWWWWWWWWWWWWWWWWWW WWWWWWWWWWWWWWWWWWWW                  W",
"W WWWW WWWW   WWW                                                    WWWWWWWWW",
"W                                                                            W",
"W                                                                            W",
"W     W        WWWWWWWWWWWWWWWWWWWWWW      WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",                                      
"W     W                                                                      W",
"W                                                                            W",
"W     WWWWWWWWWWWWWWWWW                                                      W",
"W                        WWWWW     WW  WWWWWWWWWWWWWWWWWWWWWWWW      WWWWWWWWW",
"W     WWWWWWWWWWWWWWWWWWW                                                    W",
"W                         WW                                                 W",
"W  WWWWWWWWWWWW               WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W              WWWWWWWWWWWWWWWWWWW                                           W",
"W                                                                            W",
"W                                                                            W",
"WWWWWWWWWWWWWWWWW      WWWWWWWWWWWWWWWW                                      W",
"W                                                                            W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]
pygame.display.set_icon(icon)
def Menu ():

#menu=pygame.image.load ('menu.jpg')
#tela.blit(menu,(0,0))
 tela.fill('red') 

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
gamestate="menu"
nivel=False
rodar=True
jogador=Jogador()
rodar=True
while rodar:
    
    for controle in pygame.event.get():
        if controle.type==pygame.QUIT:
            rodar=False
        if controle.type == pygame.KEYDOWN and controle.key == pygame.K_ESCAPE:
            rodar=False
    
        if gamestate=="menu":
             Menu()
             ponteiro=menu=pygame.image.load ('data\psMenu.png')
             tela.blit(ponteiro,(x,y))
             if controle.type == pygame.KEYDOWN and controle.key == pygame.K_RIGHT :
                
                if x==100:
                    x=627
                    y=900
                elif x==627:
                    x=1170
                    y=900
             if controle.type == pygame.KEYDOWN and controle.key == pygame.K_LEFT :
                
                if x==1170:
                    x=627
                    y=900
                elif x==627:
                    x=100
                    y=900
             if x==627 and controle.type == pygame.KEYDOWN and controle.key == pygame.K_SPACE:
                   gamestate="nivel"
                   
                   nivel=True
             pygame.display.flip()

        if gamestate=="nivel":
            tela.fill('black')
            for wall1 in walls:
                 pygame.draw.rect(tela, ("blue"), wall1.rect)
            jogador.draw(tela)
            ativo=True
            
        if ativo:  
           
        
         
          key = pygame.key.get_pressed()
          if key[pygame.K_LEFT]:
            jogador.move((-4), 0)
          if key[pygame.K_RIGHT]:
            jogador.move(4, 0)
          if key[pygame.K_UP]:
            jogador.move(0, -4)
          if key[pygame.K_DOWN]:
            jogador.move(0, 4)
                 
        pygame.display.update()

        
                 

pygame.quit()








