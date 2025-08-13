import pygame as pg

class Tela_Inicial:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pg.time.Clock()
        self.rodando = True

        self.bg = pg.image.load('Imagens/Telas/tela_inicio.png').convert()
        self.bg = pg.transform.smoothscale(self.bg, self.screen.get_size())

        self.press_start = pg.Rect(380, 550, 480, 90)

    def draw(self, screen):
        self.screen.blit(self.bg, (0, 0))

    def run(self, screen):
        while self.rodando:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return False
                        
                    if event.key == pg.K_RETURN or event.key == pg.K_SPACE:
                        self.rodando = False
            
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.press_start.collidepoint(event.pos): 
                        self.rodando = False

            self.draw(screen)
            pg.display.flip()

        return True