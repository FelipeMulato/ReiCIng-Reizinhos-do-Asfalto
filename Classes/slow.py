import pygame as pg
import random
from Funções.colisao_coletavel import colisao_coletavel

class Slow():
    def __init__(self, arquivo):
        self._surf = pg.image.load(f"Imagens/{arquivo}.png")
        self._surf = pg.transform.scale(self._surf, (68, 68))
        posição_y = random.randint(200, 500)
        self._rect = self._surf.get_rect(topleft=(-100, posição_y))
        self.hitbox = self._rect.inflate(-5, -5) 

    def mover(self, velocidade):
        self._rect.x += velocidade
        self.hitbox.centerx = self._rect.centerx
        self.hitbox.centery = self._rect.centery
    
    def mudar_pos(self):
        novo_y = random.randint(200, 500)
        self._rect.y = novo_y

class hud_slow:
    def __init__(self):
        self._surf = pg.image.load(f"Imagens/slow.png")
        self._surf = pg.transform.scale(self._surf, (68, 68))
        self._rect = self._surf.get_rect(topleft=(370, 20)) 
        self.font = pg.font.Font(None, 36)

    def desenhar(self, tela, contagem):
        tela.blit(self._surf, self._rect)
        
        texto_surf = self.font.render(str(contagem), True, (255, 255, 255))
        texto_rect = texto_surf.get_rect(topleft=(self._rect.right + 5, self._rect.centery - 12))
        tela.blit(texto_surf, texto_rect)