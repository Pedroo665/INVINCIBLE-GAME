import pygame
class Jogador(object):
    
    def __init__(self):
        
        self.sprite=pygame.image.load("data\ps1.png")
        self.rect=self.sprite.get_rect()
        self.rect.x=340
        self.rect.y=340
  

    def draw(self, surface):
       surface.blit(self.sprite, (self.rect.x, self.rect.y))

    def move(self, dx, dy):
        
        
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
     
        
        self.rect.x += dx
        self.rect.y += dy
        
        # verifica se o sprite do jogador colidiu com um bloco do labirinto 
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: 
                    self.rect.right = wall.rect.left
                if dx < 0: 
                    self.rect.left = wall.rect.right
                if dy > 0: 
                    self.rect.bottom = wall.rect.top
                if dy < 0: 
                    self.rect.top = wall.rect.bottom
                if dy < 0:
                   self.rect.top = wall.rect.bottom
       
class Inimigo(object):
    
    def __init__(self):
        
        self.sprite=pygame.image.load("data\ene.png")
        self.rect=self.sprite.get_rect()
        self.rect.x=540
        self.rect.y=390
  

    def draw(self, surface):
       surface.blit(self.sprite, (self.rect.x, self.rect.y))

    def move(self, dx, dy):
        
        
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
            
    
       
    

    def Update(self):
     

        if  jogador.rect.x > self.rect.x :
            self.rect.x += 1
        if jogador.rect.x < self.rect.x :
            self.rect.x -= 1
        if jogador.rect.y > self.rect.y :
            self.rect.y += 1
        if jogador.rect.y < self.rect.y :
            self.rect.y -= 1

    

    
        

       
class Wall(object):
    
     def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 30, 30)



pygame.init()


tela=pygame.display.set_mode((1920,1080))
icon=pygame.image.load('data\MARK.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption("INVINCIBLE")

font = pygame.font.SysFont(None, 100)
text = ""
input_active = True
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


def textinho(texto,x,y,tamanho):
    
    
 
    font=pygame.font.Font('freesansbold.ttf', tamanho)
    text = font.render(texto, True, "black")
   

    textRect = text.get_rect()

    textRect.center = (x,y)
    tela.blit(text, textRect)
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

st1(level1) #aqui a gente ta chamando a função para construir o labirinto e alimentando (passando como argumento) com o desenho do nivel 1

gamestate="menu" #essa variavel vai verificar qual tela foi selecionada

rodar=True
jogador=Jogador()
inimigo=Inimigo()
rodar=True



while rodar:
    
    for controle in pygame.event.get():
        if controle.type==pygame.QUIT:
            rodar=False
        if controle.type == pygame.KEYDOWN and controle.key == pygame.K_ESCAPE:
            rodar=False
    
        if gamestate=="menu":
             tela.fill('red')
             jogador=Jogador() #toda vez que o voltar a tela principal, o jogador vai ser resetado para a posição inicial
             inimigo=Inimigo()
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
                    
                   #comando para selecionar a opção jogo (se x for igual a 627 e a tecla que for pressionada for space, então gamestate será igual a nivel 
             if x==627 and controle.type == pygame.KEYDOWN and controle.key == pygame.K_SPACE:
                   gamestate="nivel"
                   
                   #comando para selecionar a opção crédito
             if x==1170 and controle.type == pygame.KEYDOWN and controle.key == pygame.K_SPACE:
                   gamestate="creditos"

                   #comando para selecionar a opção configuração
             if x==100 and controle.type == pygame.KEYDOWN and controle.key == pygame.K_SPACE:
                   gamestate="configuração"
                   
             pygame.display.flip()

             #comando para voltar para o menu principal
        if controle.type == pygame.KEYDOWN and controle.key == pygame.K_BACKSPACE:
                  gamestate="menu"
                  ativo=False

            # controi o nivel se o gamestate for nivel       
        if gamestate=="nivel":
            tela.fill('black')

            #exibe os blocos do nivel na tela
            for wall1 in walls:
                 pygame.draw.rect(tela, ("blue"), wall1.rect)

            #exibi o sprite do jogador e inimna tela     
            jogador.draw(tela)
            inimigo.draw(tela)
            ativo=True
            inimigo.Update() # atualiza os movimentos do inimigo
            
        # se o sprite do jogador e do inimigo colidir vai ativar a tela de game over    
        if jogador.rect.colliderect(inimigo.rect):
            gamestate="gameover"
            
        if gamestate=="gameover":
            
            tela.fill('pink')
            textinho("GAME OVER",(1920//2),(1080//2),48)
           
            if controle.type == pygame.KEYDOWN and controle.key == pygame.K_SPACE:
                  gamestate="pontuação"
                  ativo=False
            
            if controle.type == pygame.KEYDOWN and controle.key == pygame.K_BACKSPACE:
                  gamestate="menu"
                  ativo=False


            # O jogador pode escrever seu nome na tela de pontuação     
        if gamestate=="pontuação":
            jogador=Jogador()
            tela.fill('orange')
            textinho("Pontuação",(1920//2),(1080//2.5),48)
            if controle.type == pygame.KEYDOWN and controle.type == pygame.K_SPACE :
               
               input_active = True
               text = " " # a variavel text é declada vazia
               
            if controle.type ==pygame.KEYDOWN and input_active:
               if controle.key == pygame.K_RETURN:#esse comando confirma o nome RETURN é o mesmo que a tecla ENTER)
                input_active = False
               elif controle.key == pygame.K_DELETE:# esse comando permite apagar as letras
                text =  text[:-1]
               else:
                text += controle.unicode#esse comando grava as letras dentro da variavel text
            text_surf = font.render(text, True, (255, 0, 0)) # define a fonte, o texto, e a cor
            tela.blit(text_surf, text_surf.get_rect(center = tela.get_rect().center))# exibe na tela
            
        # se o jogo tiver rodando(se ativo for verdadeiro),a movimentação do personagem será permitida com os comandos configurados    
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
        if gamestate=="creditos":
            tela.fill('blue')
        if gamestate=="configuração":
            tela.fill('yellow')
            
            
                 
        pygame.display.update()

        
                 

pygame.quit()




