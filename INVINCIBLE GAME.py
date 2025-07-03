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
    
    def __init__(self,image,ix=900,iy=390):
        
        self.sprite=pygame.image.load(image)
        self.rect=self.sprite.get_rect()
        self.rect.y=iy
        self.rect.x=ix
  

    def draw(self, surface):
       surface.blit(self.sprite, (self.rect.x, self.rect.y))
        
       
    

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
class Item (object):
    def __init__(self,xim,yim,imagem):
    
        self.sprite=pygame.image.load(imagem)
        self.rect=self.sprite.get_rect()
        self.rect.y=yim
        self.rect.x=xim
    def draw(self, surface):
       surface.blit(self.sprite, (self.rect.x, self.rect.y))
        


pygame.init()


tela=pygame.display.set_mode((1920,1080))
icon=pygame.image.load('data\MARK.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption("INVINCIBLE")

#comandos para configurar musica
'''musica = pygame.mixer.Sound("data/musica.mp3")
musica.set_volume(0.40)
musica.play(-1, 0, 1000)
musica.stop()'''


thragg="data\Thragg.png"
sinistro='data\Sinistro.png'
conquest="data\Conquest.png"

saida= pygame.Rect(1920//2, 1080//2, 30, 30)

timer_interval =1000 #500 # 0.5 seconds
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event , timer_interval)
clock = pygame.time.Clock()
velocidade=4
aviso="esperando"
itemvisivel=False
counter =5
counter2=15
counter3=90



font = pygame.font.SysFont(None, 100)


texter = font.render(str(counter), True, (0, 128, 0))
texter2 = font.render(str(counter2), True, (0, 128, 0))
texter3 = font.render(str(counter3), True, (0, 128, 0))

text = ""
input_active = True
x=627
y=900
ativo=False
walls=[]
level1 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                               W                              W",
"W   WWWWWWWWW                   W                  WWWWWWWWW   W",
"W                    W          W         W                    W",
"W                    W          W         W                    W",
"WWWWWWWWWWWWWWW      W                    W      WWWWWWWWWWWWWWW",
"W             W   WWWWWWW              WWWWWWW   W             W",
"W             W                                  W             W",
"WWWWWWWWWWWWWWW           WWWWWWWWWWWWW          WWWWWWWWWWWWWWW",
"W                               W                              W",
"W                               W                              W",
"W                               W                              W",
"W             WWWWWWW                      WWWWWWW             W",
"W   W         W                                  W         W   W",
"W   W         W        WWW            WWW        W         W   W",
"W   W         W        W  W          W  W        W         W   W",
"W   WWWW      W   W    W                W    W   W      WWWW   W",
"W                 W    W                W    W                 W",
"W                 W    W                W    W                 W",
"W                 W    WWWWWWWWWWWWWWWWWW    W                 W",
"W                 W                          W                 W",
"W                                                              W",                                      
"W                         WWWWWWWWWWWWW                        W",
"W     WWWWWWW                   W                  WWWWWWW     W",
"W                               W                              W",
"W                               W                              W",
"WWWWWWWWWWWWWW   WWWWWWWW       W       WWWWWWWW  WWWWWWWWWWWWWW",
"W            W          W               W         W            W",
"W            W          W               W         W            W",
"WWWWWWWWWWWWWW     W    W               W   W     WWWWWWWWWWWWWW",
"W                  W                        W                  W",
"W                  W                        W                  W",
"W  WWWWWWWWWWWWWWWWW                        WWWWWWWWWWWWWWW    W",
"W                                                              W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]

powerup='data/powerUp .png'


def textinho(texto,x,y,tamanho):
    
    
 
    font=pygame.font.Font('freesansbold.ttf', tamanho)
    text = font.render(texto, True, "yellow")
   

    textRect = text.get_rect()

    textRect.center = (x,y)
    tela.blit(text, textRect)

def Menu ():
 tela.fill('red')
 menu=pygame.image.load ('data/menu.jpg')
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

st1(level1) #aqui a gente ta chamando a função para construir o labirinto e alimentando (passando como argumento) com o desenho do nivel 1

gamestate="menu" #essa variavel vai verificar qual tela foi selecionada

rodar=True
jogador=Jogador()
inimigo=Inimigo(thragg)
inimigo2=Inimigo(sinistro,700,500)
inimigo3=Inimigo(conquest,900,700)
item=Item(1920//1.8,150,powerup)
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
             inimigo=Inimigo(thragg)
             inimigo2=Inimigo(sinistro,700,500)
             inimigo3=Inimigo(conquest,900,700)
             item=Item(1920//1.8,150,powerup)
             itemvisivel=False
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
       
        if jogador.rect.colliderect(saida):
            gamestate="ganhou"
        if gamestate=="ganhou":
            
            tela.fill('black')
            textinho("VOCÊ GANHOU!",(1920//2),(1080//2),48)
            itemvisivel=False
           
            if controle.type == pygame.KEYDOWN and controle.key == pygame.K_SPACE:
                  gamestate="creditos"
                  ativo=False
            
            if controle.type == pygame.KEYDOWN and controle.key == pygame.K_BACKSPACE:
                  gamestate="menu"
                  ativo=False   
        # se o sprite do jogador e do inimigo colidir vai ativar a tela de game over    
        if jogador.rect.colliderect(inimigo.rect)or jogador.rect.colliderect(inimigo2.rect)or jogador.rect.colliderect(inimigo3.rect):
            gamestate="gameover"
        if inimigo.rect.colliderect(inimigo2.rect)or inimigo.rect.colliderect(inimigo3.rect):
             inimigo.rect.x+=60
             inimigo.rect.y+=60
        if inimigo2.rect.colliderect(inimigo.rect)or inimigo2.rect.colliderect(inimigo3.rect):
             inimigo2.rect.x+=60
             inimigo2.rect.y+=60
        if inimigo3.rect.colliderect(inimigo.rect)or inimigo3.rect.colliderect(inimigo2.rect):
             inimigo3.rect.x+=60
             inimigo3.rect.y+=60
        
        if gamestate=="gameover":
            itemvisivel=False
            
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

            
        if controle.type == timer_event:
            if aviso == "começou":
                counter -= 1
                texter = font.render(str(counter), True, (0, 128, 0))
                if counter == 0:
                  aviso="esperando"
                  
                  
            if aviso == "pegou":
                   counter2 -= 1
                   texter2 = font.render(str(counter2), True, (0, 128, 0))
                   if counter2 == 0:
                    aviso="esperando"
                   
                       
            if ativo==True:
                counter3 -= 1
                texter3 = font.render(str(counter3), True, (0, 128, 0))
                if counter3 < 0:
                    counter3=0
                    if counter3==0:
                     gamestate="gameover"  
                     active=False
        if aviso=="pegou":
                      
                   texterRect_tx2= texter2.get_rect()
                   texterRect_tx2.center = ((1920//2),(1080//2))
                   
                   if counter2>0:
                    tela.blit(texter2, texterRect_tx2)
                    
                   
                   
        if aviso=="começou":
                  
                   textRectt = texter.get_rect()
                   textRectt.center = ((1920//2),(1080//2))
                   
                   if counter>0:
                    tela.blit(texter, textRectt)
                    
                   
        # se o jogo tiver rodando(se ativo for verdadeiro),a movimentação do personagem será permitida com os comandos configurados    
       

        if jogador.rect.colliderect(item.rect):
               velocidade=6
               itemvisivel=False 
        if gamestate=="creditos":
            tela.fill('blue')
            textinho('Obrigado por jogar o NOSSO jogo!',1920//2,300,72)
            textinho('Thiago\n Pedro\n Rafael\n',1920//2,1080//2,40)

            
        if gamestate=="configuração":
            tela.fill('yellow')
        pygame.display.update()
   
   
    if ativo:
            
          key = pygame.key.get_pressed()
          if key[pygame.K_LEFT]:
            jogador.move((-velocidade), 0)
          if key[pygame.K_RIGHT]:
            jogador.move(velocidade, 0)
          if key[pygame.K_UP]:
            jogador.move(0, -velocidade)
          if key[pygame.K_DOWN]:
            jogador.move(0, velocidade)
    if gamestate=="nivel":
            tela.fill('black')
            
            #exibe os blocos do nivel na tela
            for wall1 in walls:
                 pygame.draw.rect(tela, ("blue"), wall1.rect)

            #exibi o sprite do jogador e inimna tela     
            jogador.draw(tela)
            inimigo.draw(tela)
            inimigo2.draw(tela)
            inimigo3.draw(tela)
              
           
            ativo=True
            inimigo.Update()
            inimigo2.Update()# atualiza os movimentos do inimigo
            inimigo3.Update()
            pygame.draw.rect(tela, ("red"), saida)
            if not jogador.rect.colliderect(item.rect)and not velocidade==6:
                   itemvisivel=True
                   
    if itemvisivel:
        item.draw(tela)
            
            
    clock.tick(60)/1000         
    pygame.display.update()

        
                 

pygame.quit()





