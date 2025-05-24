import pygame

class  Cooldown:
    def init(self):
        self.tempo = 0 
        self.ua = 0 
        self.c = 0


    def entrar_c(self, n):
        self.c = n
        self.ua = pygame.time.get_ticks()

    def verificar(self):
        self.tempo = pygame.time.get_ticks()
        if self.tempo - self.ua >= self.c:
            return True
        return False