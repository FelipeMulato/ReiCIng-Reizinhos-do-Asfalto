import pygame as pg
import random

class Trofeu:
    def __init__(self, arquivo):
        self.surf = pg.image.load(f"Imagens/{arquivo}.png")
        self.surf = pg.transform.scale(self.surf, (65, 98))

        pos_y_aleatoria = random.randint(200, 500)
        self._rect = self.surf.get_rect(topleft=(-100, pos_y_aleatoria))
        self.hitbox = self._rect.inflate(-28, -18)
        self.pego = False

    def mover_trofeu(self, velocidade):
        self._rect.x += velocidade
        self.hitbox.centerx = self._rect.centerx
        self.hitbox.centery = self._rect.centery
    
    def voar(self, x, a, b, c):
        prox_x = x - 30
        prox_y = a * prox_x**2 - b * prox_x + c
        self._rect.x = prox_x
        self._rect.y = round(prox_y)

        return prox_x
    
    def mudar_pos(self):
        novo_y = random.randint(200, 500)
        self._rect.y = novo_y