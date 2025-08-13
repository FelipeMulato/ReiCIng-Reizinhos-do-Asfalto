import pygame as pg
import random

class Coracao:
    def __init__(self):
        self._surf = pg.image.load("Imagens/Coracao/coracao_cheio.png")
        self._surf = pg.transform.scale(self._surf, (68, 68))
        posição_y = random.randint(200, 500)
        self._rect = self._surf.get_rect(topleft=(-100, posição_y))
        self.hitbox = self._rect

    def mover(self, velocidade):
        self._rect.x += velocidade
        self.hitbox.centerx = self._rect.centerx
        self.hitbox.centery = self._rect.centery


class hud_coracao_coletavel:
    def __init__(self):
        self._surf = pg.image.load(f"Imagens/Coracao/coracao_cheio.png") 
        self._surf = pg.transform.scale(self._surf, (68, 68))
        self._rect = self._surf.get_rect(topleft=(250, 20))
        self.font = pg.font.Font(None, 36)

    def desenhar(self, tela, contagem):
        tela.blit(self._surf, self._rect)
        
        texto_surf = self.font.render(str(contagem), True, (255, 255, 255))
        texto_rect = texto_surf.get_rect(topleft=(self._rect.right + 5, self._rect.centery - 12))
        tela.blit(texto_surf, texto_rect)