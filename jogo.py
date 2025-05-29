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
        self.cooldown2 = Cooldown()
        self.cooldown2.entrar_c(200)
        self.iniciado = False
        self.pa = 0
        self.ponto = 0

        self.vel_cano = 5

        self.pulo = False
        self.forca_gravidade = 0
        self.antig = False

        self.cor_fundo = (0, 0, 0)


        self.ae = 0 # altura especifica
        self.ea = 0 # espaçamento entre canos alternativa
    

    def criar_canos(self, y, espaçamento):
        altura_superior = y
        altura_inferior = 600 - (y + espaçamento)



        cc = pygame.draw.rect(self.tela, (0, 255, 0), (620, 0, 400, altura_superior))
        cb = pygame.draw.rect(self.tela, (0, 255, 0), (620, y + espaçamento, 400, altura_inferior))

        c = {
            "superior": cc,
            "inferior": cb,
            "x": 620,
            "y": y,
        }

        self.canos.append(c)
        return c

    
    def atualizar_canos(self):
        for cano in self.canos:
            cano["x"] -= self.vel_cano
            cano["superior"].x = cano["x"]
            cano["inferior"].x = cano["x"]

            cano["superior"].width = 60
            cano["inferior"].width = 60

            pygame.draw.rect(self.tela, (0, 255, 0), cano["superior"])
            pygame.draw.rect(self.tela, (0, 255, 0), cano["inferior"])
            if cano["x"] < 0:
                self.canos.remove(cano)
                self.ponto += 1
            


            # if isinstance(cano, pygame.Rect):

            #     cano.x -= self.vel_cano
            #     cano.width = 60
            
            #     pygame.draw.rect(self.tela, (0, 255, 0), cano)

            #     if cano.x == 0:
            #         self.canos.remove(cano)
            #         self.pa += 1
            #         if self.pa >= 2:
            #             self.pa = 0
            #             self.ponto += 1


    def verificar_colisao(self, x):
        if isinstance(x, pygame.Rect):
            for cano in self.canos:
                if cano["superior"].colliderect(x) or cano["inferior"].colliderect(x):
                    self.canos = []
                    self.ponto = 0
                    self.pa = 0
                    self.vel_cano = 5
                    self.ae = 0
                    return True
        return False


    def gravidade(self, y_player):

        if self.pulo:
            self.forca_gravidade = -15
            self.pulo = False
        if self.forca_gravidade < 4:
            self.forca_gravidade += 7
        if not self.antig:
            self.cor_fundo = (0, 0, 0)
            y_player += self.forca_gravidade
        else:
            self.cor_fundo = (255, 255, 255)
            y_player -= self.forca_gravidade

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.pulo = True
        return y_player
    def ativar_desativa_antig(self):
        if self.antig:
            self.antig = False
            self.forca_gravidade *= -1
        else:
            self.antig = True
            self.forca_gravidade *= -1


    def jogo(self):
        if self.iniciado:
            if self.ponto <= 10:
                if self.cooldown.verificar():
                    self.criar_canos(randint(30,self.altura - 60), 150)
                    self.cooldown.entrar_c(2000)
            elif self.ponto <= 20:
                if self.cooldown.verificar():
                    
                    self.criar_canos(randint(30,self.altura - 60), 150)
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
            elif self.ponto <= 100:
                if self.cooldown.verificar():
                    if self.vel_cano <= 19:
                        self.vel_cano += 1

                    self.ae = 100 - randint(-40 , 40)

                    self.criar_canos(self.ae, 150)
                    self.cooldown.entrar_c(400)
                    self.ea = 300
            elif self.ponto <= 120:                
                if self.cooldown.verificar():
                    self.ae == self.altura//2
                    if not self.ea < 70:
                        self.ea -= 10
                    self.criar_canos(self.ae, self.ea)
                    self.cooldown.entrar_c(400)
            elif self.ponto <= 8000:
                if self.cooldown.verificar():
                    self.criar_canos(randint(70, 500), 150)
                    self.cooldown.entrar_c(1500)
                if self.cooldown2.verificar():
                    self.ativar_desativa_antig()
                    self.cooldown2.entrar_c(randint(1000, 2000))

            self.atualizar_canos()







