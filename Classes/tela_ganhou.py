import pygame as pg

class Tela_Ganhou:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pg.time.Clock()
        self.rodando = True

        self.bg = pg.image.load('Imagens/Telas/tela_vitoria.png').convert()
        self.bg = pg.transform.smoothscale(self.bg, self.screen.get_size())

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
            
            self.draw()
            pg.display.flip()

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((1240, 720))
    tela = Tela_Ganhou(screen)
    tela.run()