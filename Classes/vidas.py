import pygame as pg

class Vidas:
    def __init__(self, x):
        self._surf = pg.image.load(f'Imagens/coracao_cheio.png')
        self._rect = self._surf.get_rect(topleft=(x, 25))
        self.blink = False
        self.tempo_blink = pg.time.get_ticks()
        self.duracao_blink = 1000
        self.viva = True

    def morreu(self):
        self._surf = pg.image.load(f'Imagens/coracao_vazio.png')
        self.blink = True
        self.viva = False
    
    def viveu(self):
        self._surf = pg.image.load(f'Imagens/coracao_cheio.png')

    def checagem_blink(self):
        if self.blink == True:
            tempo_atual = pg.time.get_ticks()
            if tempo_atual - self.tempo_blink > self.duracao_blink:
                self.blink = False