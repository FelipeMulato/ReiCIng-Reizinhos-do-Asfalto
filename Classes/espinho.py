import pygame as pg
import random

class Espinho:
    def __init__(self, arquivo):
        self._surf = pg.image.load(f'ReiCIng-Reizinhos-do-Asfalto/Imagens/{arquivo}.png')

        pos_y_aleatoria = random.randint(200, 500)
        self._rect = self._surf.get_rect(topleft=(-100, pos_y_aleatoria))
    
    def mover_espinho(self, velocidade):
        self._rect.x += velocidade
        