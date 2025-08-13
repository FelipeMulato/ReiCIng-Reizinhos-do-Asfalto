import pygame as pg
import random

class Coracao:
    def __init__(self):
        self._surf = pg.image.load("Imagens/Coracao/hud_coracao_coletado.png")
        self._surf = pg.transform.scale(self._surf, (60, 55))
        posição_y = random.randint(200, 500)
        self._rect = self._surf.get_rect(topleft=(-100, posição_y))
        self.hitbox = self._rect

    def mover(self, velocidade):
        self._rect.x += velocidade
        self.hitbox.centerx = self._rect.centerx
        self.hitbox.centery = self._rect.centery