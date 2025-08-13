import pygame as pg

class Tela_Gameover:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pg.time.Clock()
        self.rodando = True

        self.bg = pg.image.load('Imagens/Telas/tela_derrota.png').convert()
        self.bg = pg.transform.smoothscale(self.bg, self.screen.get_size())

        self.yes = pg.Rect(418, 480, 170, 70)
        self.no = pg.Rect(615, 480, 170, 70)

    def draw(self):
        self.screen.blit(self.bg, (0, 0))

    def run(self):
        while self.rodando:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return False
                    if event.key == pg.K_RETURN or event.key == pg.K_SPACE:
                        return True
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.yes.collidepoint(event.pos):
                        return True
                    if self.no.collidepoint(event.pos):
                        return False
            
            self.draw()
            pg.display.flip()