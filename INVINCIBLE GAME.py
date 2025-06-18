import pygame


pygame.init()
tela=pygame.display.set_mode((800,600))
tela.fill((255,0,0))
icon=pygame.image.load('data\MARK.jpg')
pygame.display.set_icon(icon) 

pygame.display.update()


