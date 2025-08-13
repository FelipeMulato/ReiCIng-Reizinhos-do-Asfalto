import pygame as pg
import random

class Espinho:
    def __init__(self, arquivo):
        self._surf = pg.image.load(f'Imagens/{arquivo}.png')

        pos_y_aleatoria = random.randint(200, 500)
        self._rect = self._surf.get_rect(topleft=(-100, pos_y_aleatoria))
        self.hitbox = self._rect.inflate(-28, -18)
    
    def mover(self, velocidade):
        self._rect.x += velocidade
        self.hitbox.centerx = self._rect.centerx
        self.hitbox.centery = self._rect.centery

    def mudar_pos(self):
        novo_y = random.randint(200, 500)
        self._rect.y = novo_y