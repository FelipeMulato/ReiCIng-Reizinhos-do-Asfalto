import pygame as pg

class Carro:
    def __init__(self, arquivo):
        self._surf =pg.image.load(f'ReiCIng-Reizinhos-do-Asfalto/Imagens/{arquivo}.png')
        self._rect = self._surf.get_rect(midbottom = (1000, 330))

    def cima(self):
        self._rect.y -= 5

    def baixo(self):
        self._rect.y += 5