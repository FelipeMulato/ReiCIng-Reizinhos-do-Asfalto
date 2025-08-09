import pygame as pg
import random

class Trofeu:
    def __init__(self, arquivo):
        self.surf = pg.image.load(f"Imagens/{arquivo}.png")
        self.surf = pg.transform.scale(self.surf, (75, 75))

        pos_y_aleatoria = random.randint(200, 500)
        self._rect = self.surf.get_rect(topleft=(-100, pos_y_aleatoria))
        self.hitbox = self._rect.inflate(-28, -18)

    def mover_trofeu(self, velocidade):
        self._rect.x += velocidade
        self.hitbox.centerx = self._rect.centerx
        self.hitbox.centery = self._rect.centery