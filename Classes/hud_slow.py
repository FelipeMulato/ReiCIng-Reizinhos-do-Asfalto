import pygame as pg

class HUD_Slow:
    def __init__(self):
        self._surf = pg.image.load(f"Imagens/slow.png")
        self._surf = pg.transform.scale(self._surf, (68, 68))
        self._rect = self._surf.get_rect(topleft=(220, 32)) 
        self.font = pg.font.Font(None, 36)

    def desenhar(self, tela, contagem):
        tela.blit(self._surf, self._rect)
        
        texto_surf = self.font.render(str(contagem), True, (255, 255, 255))
        texto_rect = texto_surf.get_rect(topleft=(self._rect.right + 5, self._rect.centery - 12))
        tela.blit(texto_surf, texto_rect)