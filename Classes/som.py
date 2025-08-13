import pygame 

class Sons:
    def __init__(self):
        self.som_trofeu = pygame.mixer.Sound("Áudios/smw_coin.wav")
        self.som_trofeu.set_volume(0.3)
        self.som_explosao = pygame.mixer.Sound("Áudios/explosao.wav")
        self.som_explosao.set_volume(0.3)
        self.som_fundo = pygame.mixer.Sound("Áudios/car_chase.mp3")
        self.som_fundo.set_volume(0.1)
        self.som_cair = pygame.mixer.Sound("Áudios/Falling.mp3")
        self.som_cair.set_volume(0.3)
        self.som_dano = pygame.mixer.Sound("Áudios/playerhit.mp3")
        self.som_dano.set_volume(0.3)

    def trofeu(self):
        self.som_trofeu.play()
    def explosao(self):
        self.som_explosao.play()
    def fundo(self):
        self.som_fundo.play()
    def cair(self):
        self.som_cair.play()
    def dano(self):
        self.som_dano.play()
