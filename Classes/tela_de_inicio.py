import pygame 
import sys 
import os

class tela_inicial:
    def __init__(self, screen, imagens_dir="Imagens", inic="Tela de Início.png"):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.rodando = True

        bg_path = os.path.join(imagens_dir, inic)
        self.bg = pygame.image.load(bg_path).convert()
        self.bg = pygame.transform.smoothscale(self.bg, self.screen.get_size())

        self.arquivos_carros = ["CarRed.png", "CarBlue.png", "CarGreen.png"]

        self.carros = []
        for carro in self.arquivos_carros:
            path = os.path.join(imagens_dir, carro)
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.smoothscale(img, (200, 110))
            self.carros.append(img)

        self.indice_carro = 0
        self.posicao_carro = (
            self.screen.get_width() // 2 -400,
            int(self.screen.get_height() * 0.75),
        )

        self.font = pygame.font.Font(None, 36)

    def draw(self):
        self.screen.blit(self.bg, (0, 0))

        if self.carros:
            img_carro = self.carros[self.indice_carro]

            img_carro_rot = pygame.transform.rotate(img_carro, -155)

            rect = img_carro_rot.get_rect(center=self.posicao_carro)
            self.screen.blit(img_carro_rot, rect)

    def run(self):
        while self.rodando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return self.indice_carro, self.arquivos_carros[self.indice_carro]

                    elif event.key in (pygame.K_1, pygame.K_KP_1):
                        self.indice_carro = 0
                    elif event.key in (pygame.K_2, pygame.K_KP_2):
                        if len(self.carros) > 1: self.indice_carro = 1
                    elif event.key in (pygame.K_3, pygame.K_KP_3):
                        if len(self.carros) > 2: self.indice_carro = 2

                    elif event.key == pygame.K_LEFT:
                        self.indice_carro = (self.indice_carro - 1) % len(self.carros)
                    elif event.key == pygame.K_RIGHT:
                        self.indice_carro = (self.indice_carro + 1) % len(self.carros)

            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    tela = tela_inicial(screen, imagens_dir="Imagens", inic="Tela de Início.png")
    idx, nome = tela.run()
