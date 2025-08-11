import pygame as pg

class Carro:
    def __init__(self, arquivo):
        self._surf = pg.image.load(f'Imagens/{arquivo}.png').convert_alpha()
        self._original_surf = self._surf
        self._rect = self._surf.get_rect(midbottom = (1000, 330))
        self.hitbox = self._rect.inflate(-18, -12)

        self.vidas = 3
        self.trofeus = 0
        self.slow = 0
        self.venceu = False
        self.invencivel = False
        self.tempo_invencivel = 0
        self.duracao_invencibilidade = 1500
        self.estado_queda = 'nenhum'
        self.velocidade_queda = 0

        self.angulo_rotação = 0
        self.escala = 1.0

    def cima(self):
        self._rect.y -= 5
        self.hitbox.y -= 5

    def baixo(self):
        self._rect.y += 5
        self.hitbox.y += 5

    def perder_vida(self):
        if self.invencivel == False:
            self.vidas -= 1
            self.invencivel = True
            self.tempo_invencivel = pg.time.get_ticks()
            print(f'Colisão. Vidas restantes {self.vidas}') #mensagem para teste de debug depois caso algum problema com colisão
    
    def morrer(self):
        self.vidas = 0
    
    def checagem_invencibilidade(self):
        if self.invencivel == True:
            tempo_atual = pg.time.get_ticks()
            if tempo_atual - self.tempo_invencivel > self.duracao_invencibilidade:
                self.invencivel = False
    
    def ganhar_trofeu(self):
        if self.trofeus < 3:
            self.trofeus += 1
            print(f'Troféus ganhos: {self.trofeus}') 
        if self.trofeus >= 3:
            self.venceu = True
        
        return self.venceu
    
    def ganhar_slow(self):
        self.slow += 1