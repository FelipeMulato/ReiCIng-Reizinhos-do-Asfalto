import pygame as pg

class Pista:
    def __init__(self, x):
        self._surf = pg.image.load(f'Imagens/Pista.png')
        self._rect = self._surf.get_rect(topleft=(x, 144))

    def get_x(self):
        return self._rect.x

    def mover(self, velocidade):
        self._rect.x += velocidade