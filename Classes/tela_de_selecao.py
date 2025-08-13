import pygame as pg
import sys
import os
     
class Tela_Selecao:
    def __init__(self, screen, imagens_dir="Imagens", inic="tela_selecao.png"):
        self.screen = screen
        self.clock = pg.time.Clock()
        self.rodando = True

        bg_path = os.path.join(imagens_dir, inic)
        self.bg = pg.image.load(bg_path).convert()
        self.bg = pg.transform.smoothscale(self.bg, self.screen.get_size())

        self.press_start = pg.Rect(240, 610, 550, 72)

        self.carros_de_corrida = ["carro_0", "carro_1", "carro_2", "carro_3", "carro_4"]
        self.arquivos_carros = [
            "preview_carro_0.png", "preview_carro_1.png", "preview_carro_2.png", "preview_carro_3.png", "preview_carro_4.png"]
        self.carros = [
        ]
        for f in self.arquivos_carros:
            path = os.path.join(imagens_dir, f)
            img = pg.image.load(path).convert_alpha()
            self.carros.append(img)
        self.indice_carro = 0
        
        self.boxes = [
        pg.Rect(78,  60, 242, 222),
        pg.Rect(390,  60, 242, 222),
        pg.Rect(702,  60, 242, 222),
        pg.Rect(212,  333, 262, 222),
        pg.Rect(550,  333, 262, 222)]

        self._surf0 = pg.image.load("Imagens/preview_carro_0.png")
        self._surf0 = pg.transform.scale(self._surf0, (278, 260))
        self._surf1 = pg.image.load("Imagens/preview_carro_1.png")
        self._surf1 = pg.transform.scale(self._surf1, (279, 260))
        self._surf2 = pg.image.load("Imagens/preview_carro_2.png")
        self._surf2 = pg.transform.scale(self._surf2, (278, 260))
        self._surf3 = pg.image.load("Imagens/preview_carro_3.png")
        self._surf3 = pg.transform.scale(self._surf3, (297, 265))
        self._surf4 = pg.image.load("Imagens/preview_carro_4.png")
        self._surf4 = pg.transform.scale(self._surf4, (297, 265))

        self._rect0 = self._surf0.get_rect(topleft = (60, 40))
        self._rect1 = self._surf1.get_rect(topleft = (372, 40))
        self._rect2 = self._surf2.get_rect(topleft = (685, 40))
        self._rect3 = self._surf3.get_rect(topleft = (195, 320))
        self._rect4 = self._surf4.get_rect(topleft = (534, 320))

    def draw(self):
        self.screen.blit(self.bg, (0, 0))

        self.screen.blit(self._surf0, self._rect0)
        self.screen.blit(self._surf1, self._rect1)
        self.screen.blit(self._surf2, self._rect2)
        self.screen.blit(self._surf3, self._rect3)
        self.screen.blit(self._surf4, self._rect4)
        if self.indice_carro == 0:
            pg.draw.rect(screen, (0, 255, 0), (60, 40, 278, 260), 8)
        elif self.indice_carro == 1:
            pg.draw.rect(screen, (0, 255, 0), (372, 40, 279, 260), 8)
        elif self.indice_carro == 2:
            pg.draw.rect(screen, (0, 255, 0), (685, 40, 278, 260), 8)
        elif self.indice_carro == 3:
            pg.draw.rect(screen, (0, 255, 0), (195, 320, 297, 265), 8)
        elif self.indice_carro == 4:
            pg.draw.rect(screen, (0, 255, 0), (534, 320, 297, 265), 8)
        
    def run(self):
        while self.rodando:
            for event in pg.event.get():
                if event.type == pg.QUIT: pg.quit(); sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN or event.key == pg.K_SPACE: return self.carros_de_corrida[self.indice_carro]
                    
                    elif event.key == pg.K_1 or event.key == pg.K_KP_1: self.indice_carro = 0
                    elif event.key == pg.K_2 or event.key == pg.K_KP_2: self.indice_carro = 1
                    elif event.key == pg.K_3 or event.key == pg.K_KP_3: self.indice_carro = 2
                    elif event.key == pg.K_4 or event.key == pg.K_KP_4: self.indice_carro = 3
                    elif event.key == pg.K_5 or event.key == pg.K_KP_5: self.indice_carro = 4

                    if event.key == pg.K_LEFT: self.indice_carro = 4 if self.indice_carro == 0 else self.indice_carro - 1
                    elif event.key == pg.K_RIGHT: self.indice_carro = 0 if self.indice_carro == 4 else self.indice_carro + 1
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.press_start.collidepoint(event.pos): return self.carros_de_corrida[self.indice_carro]

                    elif self.boxes[0].collidepoint(event.pos): self.indice_carro = 0
                    elif self.boxes[1].collidepoint(event.pos): self.indice_carro = 1
                    elif self.boxes[2].collidepoint(event.pos): self.indice_carro = 2
                    elif self.boxes[3].collidepoint(event.pos): self.indice_carro = 3
                    elif self.boxes[4].collidepoint(event.pos): self.indice_carro = 4

            self.draw()
            pg.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((1024, 768))
    tela = Tela_Selecao(screen, imagens_dir="Imagens", inic="tela_selecao.png")
    print(tela.run())