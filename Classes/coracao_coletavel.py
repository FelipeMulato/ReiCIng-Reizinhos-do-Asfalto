import pygame as pg
import random


class Coração:
    def __init__(self, arquivo):
        self.surf = pg.image.load(f"Imagens/coracao_cheio.png")
        self.surf = pg.transform.scale(self.surf, (44, 48))


        pos_y_aleatoria = random.randint(200, 500)
        self._rect = self.surf.get_rect(topleft=(-100, pos_y_aleatoria))
        self.hitbox = self._rect.inflate(-15, -17)
        self.pego = False


    def mover_coracao(self, velocidade):
        self._rect.x += velocidade
        self.hitbox.centerx = self._rect.centerx
        self.hitbox.centery = self._rect.centery
   
    def voar(self, x, y, a, b, c):
        prox_x = x + 30
        prox_y = a * prox_x**2 - b * prox_x + c
        dx = abs(x - prox_x)
        dy = abs(round(y - prox_y))
        self._rect.x -= dx
        self._rect.y -= dy


        return prox_x, prox_y
