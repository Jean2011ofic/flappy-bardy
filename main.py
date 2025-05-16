import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largula = 640
altura = 480
pulo = False

y_player = altura//2

y_cano_baixo_1 = 470  #maximo e de 470 meio altura//2 + 60
#aproximadamente 510 pixeis de distancia no eixo y
y_cano_cima_1 =  -40 # maximo e de -390 MEIO -210 outro maximo -40

x_cano_1 = largula//2


contador = 0

tela = pygame.display.set_mode((largula, altura))
pygame.display.set_caption('jogo')

forca_gravidade = 4
vida = 0
jogo_nao_comecou = True
fonte = pygame.font.SysFont('arial', 40, True, True)

relogio = pygame.time.Clock()
ponto = 0


while True:
    mensagem = f'pontos: {ponto}'#a mensagem q sera exibida
    texto_formatado = fonte.render(mensagem, True, (255, 255 ,255))


    relogio.tick(30)
    tela.fill((0, 0, 0))

    
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
                    x_cano_1 = largula
                    vida = 1
                    y_player = altura//2
                    ponto = 0

    
    y_player += forca_gravidade


    player = pygame.draw.rect(tela, (0,255,0), (largula//2 - 50, y_player, 30,30),)

    cano_baixo_1 = pygame.draw.rect(tela, (0,255,0), (x_cano_1,y_cano_baixo_1, 40, 400))
    cano_cima_1 = pygame.draw.rect(tela, (0,255,0), (x_cano_1,y_cano_cima_1, 40, 400))

    if not jogo_nao_comecou:
        contador += 1

    x_cano_1 -= 6

    
    if x_cano_1 <= 0:
        x_cano_1 = largula
        y_cano_cima_1 = randint(-390 , -40)
        y_cano_baixo_1 = y_cano_cima_1 + 510
        if not jogo_nao_comecou:
            ponto += 1

    if player.colliderect(cano_baixo_1):
        jogo_nao_comecou = True
    if player.colliderect(cano_cima_1):
        jogo_nao_comecou = True
    if y_player < 0:
        jogo_nao_comecou = True
    elif y_player > altura:
        jogo_nao_comecou = True

    if jogo_nao_comecou:
        tela.fill((0,0,0))
        mensagem3 = 'aperte espaco para comecar'
        texto_formatado3 = fonte.render(mensagem3, True, (255,255,255))


        tela.blit(texto_formatado3,(0, altura//2))
        pygame.display.update()




    def gravidade():
        global y_player
        global forca_gravidade
        global  pulo

        if pulo:
            forca_gravidade = -10
            pulo = False
        if forca_gravidade < 4:
            forca_gravidade += 1
            
       
    gravidade()

        


    tela.blit(texto_formatado,(400,40))
    pygame.display.update()