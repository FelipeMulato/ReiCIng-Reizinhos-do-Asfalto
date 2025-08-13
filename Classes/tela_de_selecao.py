import pygame as pg
     
class Tela_Selecao:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pg.time.Clock()
        self.rodando = True

        self.bg = pg.image.load('Imagens/Telas/tela_selecao.png').convert()
        self.bg = pg.transform.smoothscale(self.bg, self.screen.get_size())

        self.press_start = pg.Rect(260, 585, 670, 90)

        self.carros_de_corrida = ["carro_0", "carro_1", "carro_2", "carro_3", "carro_4"]
        self.arquivos_carros = [
            "preview_carro_0.png", "preview_carro_1.png", "preview_carro_2.png", "preview_carro_3.png", "preview_carro_4.png"]
        self.carros = [
        ]
        for f in self.arquivos_carros:
            img = pg.image.load(f'Imagens/Carros/{f}').convert_alpha()
            self.carros.append(img)
        self.indice_carro = 0
        
        self.boxes = [
        pg.Rect(92, 44, 283, 245),
        pg.Rect(438, 44, 285, 245),
        pg.Rect(813, 44, 283, 245),
        pg.Rect(196, 300, 357, 270),
        pg.Rect(612, 300, 350, 270)]

        self._surf0 = pg.image.load("Imagens/Carros/preview_carro_0.png")
        self._surf0 = pg.transform.scale(self._surf0, (283, 245))
        self._surf1 = pg.image.load("Imagens/Carros/preview_carro_1.png")
        self._surf1 = pg.transform.scale(self._surf1, (285, 245))
        self._surf2 = pg.image.load("Imagens/Carros/preview_carro_2.png")
        self._surf2 = pg.transform.scale(self._surf2, (283, 245))
        self._surf3 = pg.image.load("Imagens/Carros/preview_carro_3.png")
        self._surf3 = pg.transform.scale(self._surf3, (357, 270))
        self._surf4 = pg.image.load("Imagens/Carros/preview_carro_4.png")
        self._surf4 = pg.transform.scale(self._surf4, (350, 270))

        self._rect0 = self._surf0.get_rect(topleft = (92, 44))
        self._rect1 = self._surf1.get_rect(topleft = (438, 44))
        self._rect2 = self._surf2.get_rect(topleft = (813, 44))
        self._rect3 = self._surf3.get_rect(topleft = (196, 300))
        self._rect4 = self._surf4.get_rect(topleft = (612, 300))

    def draw(self, screen):
        self.screen.blit(self.bg, (0, 0))

        self.screen.blit(self._surf0, self._rect0)
        self.screen.blit(self._surf1, self._rect1)
        self.screen.blit(self._surf2, self._rect2)
        self.screen.blit(self._surf3, self._rect3)
        self.screen.blit(self._surf4, self._rect4)
        if self.indice_carro == 0:
            pg.draw.rect(screen, (0, 255, 0), (92, 44, 283, 245), 8)
        elif self.indice_carro == 1:
            pg.draw.rect(screen, (0, 255, 0), (438, 44, 285, 245), 8)
        elif self.indice_carro == 2:
            pg.draw.rect(screen, (0, 255, 0), (813, 44, 283, 245), 8)
        elif self.indice_carro == 3:
            pg.draw.rect(screen, (0, 255, 0), (196, 300, 357, 270), 8)
        elif self.indice_carro == 4:
            pg.draw.rect(screen, (0, 255, 0), (612, 300, 350, 270), 8)
        
    def run(self, screen):

        while self.rodando:
            for event in pg.event.get():
                if event.type == pg.QUIT:

                    return False, ''

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN or event.key == pg.K_SPACE: 

                        return True, self.carros_de_corrida[self.indice_carro]
                    
                    elif event.key == pg.K_1 or event.key == pg.K_KP_1: self.indice_carro = 0
                    elif event.key == pg.K_2 or event.key == pg.K_KP_2: self.indice_carro = 1
                    elif event.key == pg.K_3 or event.key == pg.K_KP_3: self.indice_carro = 2
                    elif event.key == pg.K_4 or event.key == pg.K_KP_4: self.indice_carro = 3
                    elif event.key == pg.K_5 or event.key == pg.K_KP_5: self.indice_carro = 4

                    if event.key == pg.K_LEFT: self.indice_carro = 4 if self.indice_carro == 0 else self.indice_carro - 1
                    elif event.key == pg.K_RIGHT: self.indice_carro = 0 if self.indice_carro == 4 else self.indice_carro + 1
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.press_start.collidepoint(event.pos): 

                        return True, self.carros_de_corrida[self.indice_carro]

                    elif self.boxes[0].collidepoint(event.pos): self.indice_carro = 0
                    elif self.boxes[1].collidepoint(event.pos): self.indice_carro = 1
                    elif self.boxes[2].collidepoint(event.pos): self.indice_carro = 2
                    elif self.boxes[3].collidepoint(event.pos): self.indice_carro = 3
                    elif self.boxes[4].collidepoint(event.pos): self.indice_carro = 4

            self.draw(screen)
            pg.display.flip()
