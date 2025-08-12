import pygame as pg
import random

class Coracao:
    def __init__(self, arquivo):
        self._surf = pg.image.load(f"Imagens/{arquivo}.png")
        self._surf = pg.transform.scale(self._surf, (44, 48))

        pos_y_aleatoria = random.randint(200, 500)
        self._rect = self._surf.get_rect(topleft=(-100, pos_y_aleatoria))
        self.hitbox = self._rect.inflate(-15, -17)
    
    def mover(self, velocidade):
        self._rect.x += velocidade
        self.hitbox.centerx = self._rect.centerx
        self.hitbox.centery = self._rect.centery



