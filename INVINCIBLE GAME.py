import pygame


pygame.init()
tela=pygame.display.set_mode((1920,1080))
icon=pygame.image.load('data\MARK.jpg')
x=100
y=900
pygame.display.set_icon(icon)
def Menu ():
 menu=pygame.image.load ('menu.jpg')
 tela.blit(menu,(0,0))
 pygame.display.update()
menuOn=True
rodar=True

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
             if controle.type == pygame.KEYDOWN and controle.key == pygame.K_RIGHT:
                
                if x==100:
                    x=627
                    y=900
                elif x==627:
                    x=1170
                    y=900
             if controle.type == pygame.KEYDOWN and controle.key == pygame.K_LEFT:
                
                if x==1170:
                    x=627
                    y=900
                elif x==627:
                    x=100
                    y=900

             pygame.display.flip()
             
             
pygame.display.flip()
pygame.quit()


