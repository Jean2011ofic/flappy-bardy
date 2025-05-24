import pygame
from cooldonw import Cooldown
from random import randint

class Jogo:
    def __init__(self, tela):
        self.tela = tela
        self.canos = []
        self.altura = 480
        self.largura = 640
        self.cooldown = Cooldown()
        self.cooldown.entrar_c(200)
        self.iniciado = False
        self.pa = 0
        self.ponto = 79
        self.vel_cano = 5


        self.ae = 0 # altura especifica
    

    def criar_canos(self, y, espaçamento):
        altura_superior = y
        altura_inferior = 600 - (y + espaçamento)



        cc = pygame.draw.rect(self.tela, (0, 255, 0), (620, 0, 400, altura_superior))
        cb = pygame.draw.rect(self.tela, (0, 255, 0), (620, y + espaçamento, 400, altura_inferior))


        self.canos.append(cc)
        self.canos.append(cb)
    
    def atualizar_canos(self):
        for cano in self.canos:

            if isinstance(cano, pygame.Rect):

                cano.x -= self.vel_cano
                cano.width = 60
            
                pygame.draw.rect(self.tela, (0, 255, 0), cano)

                if cano.x == 0:
                    self.canos.remove(cano)
                    self.pa += 1
                    if self.pa >= 2:
                        self.pa = 0
                        self.ponto += 1


    def verificar_colisao(self, x):
        if isinstance(x, pygame.Rect):
            for cano in self.canos:
                if cano.colliderect(x):
                    self.canos = []
                    self.ponto = 0
                    self.pa = 0
                    self.vel_cano = 5
                    self.ae = 0
                    return True
        return False

    def jogo(self):
        if self.iniciado:
            if self.ponto <= 10:
                if self.cooldown.verificar():
                    self.criar_canos(randint(20,self.altura - 40), 150)
                    self.cooldown.entrar_c(2000)
            elif self.ponto <= 20:
                if self.cooldown.verificar():
                    
                    self.criar_canos(randint(20,self.altura - 40), 150)
                    self.cooldown.entrar_c(1500)
            elif self.ponto <= 50:
                if self.cooldown.verificar():
                    self.ae += 10
                    self.criar_canos(self.ae, 150)
                    self.cooldown.entrar_c(400)
            elif self.ponto <= 80:
                if self.cooldown.verificar():
                    self.ae -= 10
                    self.criar_canos(self.ae, 150)
                    self.cooldown.entrar_c(400)
            elif self.ponto <= 2000:
                if self.cooldown.verificar():
                    if self.vel_cano <= 19:
                        self.vel_cano += 1

                    self.ae = 100 - randint(-40 , 40)

                    self.criar_canos(self.ae, 150)
                    self.cooldown.entrar_c(400)

            self.atualizar_canos()
    





