import pygame as pg

class HUD_Trofeus:
    def __init__(self):
        self._surf = pg.image.load(f'Imagens/0trofeus.png')
        self._rect = self._surf.get_rect(topleft=(10, -35))

    def pegou_trofeu(self, trofeus):
        if trofeus == 1:
            self._surf = pg.image.load(f'Imagens/1trofeus.png')
        elif trofeus == 2:
            self._surf = pg.image.load(f'Imagens/2trofeus.png')
        elif trofeus == 3:
            self._surf = pg.image.load(f'Imagens/3trofeus.png')