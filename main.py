import pygame
from pygame.locals import *
from sys import exit
from random import randint
from jogo import Jogo

pygame.init()

largula = 640
altura = 480
pulo = False

y_player = altura//2


# 1 minuto e 30 segundos aproximadamente para ultima fase atual

contador = 0

tela = pygame.display.set_mode((largula, altura))
pygame.display.set_caption('jogo')

forca_gravidade = 4
vida = 0
jogo_nao_comecou = True
fonte = pygame.font.SysFont('arial', 40, True, True)

relogio = pygame.time.Clock()
ponto = 0

jogo = Jogo(tela)
# criando canos


while True:
    mensagem = f'pontos: {ponto}'#a mensagem q sera exibida
    texto_formatado = fonte.render(mensagem, True, (255, 255 ,255))


    relogio.tick(30)
    tela.fill(jogo.cor_fundo)  

    ponto = jogo.ponto

    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if not jogo_nao_comecou:
                    pulo = True
                else:
                    jogo_nao_comecou = False
                    jogo.iniciado = True
                    x_cano_1 = largula
                    vida = 1
                    y_player = altura//2
                    ponto = 0 

    
    


    player = pygame.draw.rect(tela, (0,255,0), (largula//2 - 50, y_player, 30,30),)

    if not jogo_nao_comecou:
        contador += 1



    if jogo_nao_comecou:
        tela.fill((0,0,0))
        mensagem3 = 'aperte espaco para comecar'
        texto_formatado3 = fonte.render(mensagem3, True, (255,255,255))


        tela.blit(texto_formatado3,(0, altura//2))
        pygame.display.update()





    # if pulo:
    #     forca_gravidade = -15
    #     pulo = False
    # if forca_gravidade < 4:
    #     forca_gravidade += 7
    # y_player += forca_gravidade

    # if pygame.key.get_pressed()[pygame.K_SPACE]:
    #     pulo = True
            
       
    y_player = jogo.gravidade(y_player)
    jogo.jogo()
    
    if jogo.verificar_colisao(player):
        jogo_nao_comecou = True
        jogo.iniciado = False 
    if y_player < 0 or y_player > altura:
        jogo_nao_comecou = True
        jogo.iniciado = False 
        y_player = altura//2    


    tela.blit(texto_formatado,(400,40))
    pygame.display.update()