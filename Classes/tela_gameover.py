import pygame as pg
import sys
import os

class Tela_Gameover:
    def __init__(self, screen, imagens_dir="Imagens", inic="tela_derrota.png"):
        self.screen = screen
        self.clock = pg.time.Clock()
        self.rodando = True

        bg_path = os.path.join(imagens_dir, inic)
        self.bg = pg.image.load(bg_path).convert()
        self.bg = pg.transform.smoothscale(self.bg, self.screen.get_size())

        self.yes = pg.Rect(310, 500, 170, 60)
        self.no = pg.Rect(560, 500, 120, 60)

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
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.yes.collidepoint(event.pos):
                        return "tela de início"
                    if self.no.collidepoint(event.pos):
                        pg.quit(); sys.exist()
            
            self.draw()
            pg.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((1024, 768))
    tela = Tela_Gameover(screen, imagens_dir="Imagens", inic="tela_derrota.png")
    tela.run()