import pygame as pg
import sys
import os

class Tela_Ganhou:
    def __init__(self, screen, imagens_dir="Imagens", inic="tela_vitoria.png"):
        self.screen = screen
        self.clock = pg.time.Clock()
        self.rodando = True

        bg_path = os.path.join(imagens_dir, inic)
        self.bg = pg.image.load(bg_path).convert()
        self.bg = pg.transform.smoothscale(self.bg, self.screen.get_size())

    def draw(self):
        self.screen.blit(self.bg, (0, 0))

    def run(self):
        while self.rodando:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit(); sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit(); sys.exit()
                    if event.key == pg.K_RETURN or event.key == pg.K_SPACE:
                        return "tela de início"
            
            self.draw()
            pg.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((1024, 768))
    tela = Tela_Ganhou(screen, imagens_dir="Imagens", inic="tela_vitoria.png")
    tela.run()