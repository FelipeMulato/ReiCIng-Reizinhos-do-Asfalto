import pygame
import random

class SLow():
    def __init__(self,arquivo):

        self.retrato= pygame.image.load(f"Imagens/{arquivo}.png")
        self.retrato= pygame.transform.scale(self.retrato, (80, 80))
        
        posição_y= random.randint(200, 500)
        
        self._rect= self.retrato.get_rect(topleft=(-400, posição_y))
        self.hitbox = self._rect.inflate(-28, -18)

    def movimentação_slow(self, velocidade):
        self._rect.x += velocidade
        self.hitbox.centerx = self._rect.centerx
        self.hitbox.centery = self._rect.centery