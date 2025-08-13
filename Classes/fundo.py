import pygame as pg

class Fundo:
    def __init__(self, x):
        self._surf = pg.image.load(f'Imagens/Fundo.png')
        self._rect = self._surf.get_rect(topleft = (x, 0))

    def get_x(self):
        return self._rect.x

    def mover(self, velocidade):
        self._rect.x += velocidade