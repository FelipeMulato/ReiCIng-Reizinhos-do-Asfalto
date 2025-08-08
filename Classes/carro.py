import pygame as pg

class Carro:
    def __init__(self, arquivo):
        self._surf =pg.image.load(f'ReiCIng-Reizinhos-do-Asfalto/Imagens/{arquivo}.png')
        self._rect = self._surf.get_rect(midbottom = (1000, 330))

        self.vidas = 3
        self.invencivel = False
        self.tempo_invencivel = 0
        self.duracao_invencibilidade = 3000

    def cima(self):
        self._rect.y -= 5

    def baixo(self):
        self._rect.y += 5

    def perder_vida(self):
        if self.invencivel == False:
            self.vidas -= 1
            self.invencivel = True
            self.tempo_invencivel = pg.time.get_ticks()
            print(f'Colisão. Vidas restantes {self.vidas}') #mensagem para teste de debug depois caso algum problema com colisão
    
    def checagem_invencibilidade(self):
        if self.invencivel == True:
            tempo_atual = pg.time.get_ticks()
            if tempo_atual - self.tempo_invencivel > self.duracao_invencibilidade:
                self.invencivel = False