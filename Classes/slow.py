import pygame as pg
import random
from Funções.colisao_coletavel import colisao_coletavel

class Slow():
    def __init__(self, arquivo):
        self._surf = pg.image.load(f"Imagens/{arquivo}.png")
        self._surf = pg.transform.scale(self._surf, (68, 68))
        posição_y = random.randint(200, 500)
        self._rect = self._surf.get_rect(topleft=(-100, posição_y))
        self.hitbox = self._rect.inflate(-5, -5) 

    def mover(self, velocidade):
        self._rect.x += velocidade
        self.hitbox.centerx = self._rect.centerx
        self.hitbox.centery = self._rect.centery
    
    def mudar_pos(self):
        novo_y = random.randint(200, 500)
        self._rect.y = novo_y