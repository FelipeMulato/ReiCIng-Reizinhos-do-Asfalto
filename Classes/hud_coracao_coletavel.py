import pygame as pg

class HUD_Coracao_Coletavel:
    def __init__(self):
        self._surf = pg.image.load(f"Imagens/Coracao/hud_coracao_coletado.png") 
        self._rect = self._surf.get_rect(topleft=(1091, 80))
        self.font = pg.font.Font(None, 36)

    def desenhar(self, tela, contagem):
        tela.blit(self._surf, self._rect)
        
        texto_surf = self.font.render(str(contagem), True, (255, 255, 255))
        texto_rect = texto_surf.get_rect(topleft=(self._rect.right + 5, self._rect.centery - 12))
        tela.blit(texto_surf, texto_rect)