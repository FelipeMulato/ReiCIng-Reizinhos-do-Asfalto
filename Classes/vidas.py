import pygame as pg

class Vidas:
    def __init__(self, x):
        self._surf = pg.image.load(f'Imagens/coracao_cheio.png')
        self._rect = self._surf.get_rect(topleft=(x, 25))

    def morreu(self):
        self._surf = pg.image.load(f'Imagens/coracao_vazio.png')