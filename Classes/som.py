import pygame 

class Sons:
    def __init__(self):
        self.som_trofeu = pygame.mixer.Sound("Áudios/smw_coin.wav")
        self.som_trofeu.set_volume(0.8)
        self.som_explosao = pygame.mixer.Sound("Áudios/explosao.wav")
        self.som_explosao.set_volume(0.8)
        self.som_cair = pygame.mixer.Sound("Áudios/Falling.mp3")
        self.som_cair.set_volume(0.1)

    def trofeu(self):
        self.som_trofeu.play()
    def explosao(self):
        self.som_explosao.play()
    def cair(self):
        self.som_cair.play()

    def fundo(self):
        pygame.mixer.music.load("Áudios/car_chase.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
    def vitoria(self):
        pygame.mixer.music.load("Áudios/tema_vitoria.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()
    def derrota(self):
        pygame.mixer.music.load("Áudios/som_derrota.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
  