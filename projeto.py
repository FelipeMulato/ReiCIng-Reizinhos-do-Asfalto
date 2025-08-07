import pygame as pg
import sys

class Carro:
    def __init__(self):
        self._x = 1000
        self._y = 330
        self._largura = 100
        self._altura = 60

    def desenhar(self):
        pg.draw.rect(tela, (0, 0, 255), (self._x, self._y, self._largura, self._altura))

    def cima(self):
        self._y -= 1

    def baixo(self):
        self._y += 1

class Faixa:
    def __init__(self, y):
        self._x = -100
        self._y = y
        self._altura = 10
        self._largura = 100
    
    @property
    def x(self):
        return self._x
    
    def desenhar(self):
        pg.draw.rect(tela, (255, 255, 255), (self._x, self._y, self._largura, self._altura))

    def andar(self, velocidade):
        self._x += velocidade
        
pg.init()
altura = 720
largura = 1240
relogio = pg.time.Clock()
relogio.tick(60)

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('ReiCIng')

running = True
velocidade_faixa = 0.1
faixas1 = [Faixa(288)]
faixas2 = [Faixa(432)]
carro = Carro()

while running:
    velocidade_faixa += 0.00001
    tela.fill((255, 0, 0))
    pg.draw.rect(tela, (0, 0, 0), (0, 144, 1240, 432))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if pg.key.get_pressed()[pg.K_UP]:
        carro.cima()
    if pg.key.get_pressed()[pg.K_DOWN]:
        carro.baixo()

    for i in range(len(faixas1)):
        faixas1[i].desenhar()
        faixas2[i].desenhar()
        faixas1[i].andar(velocidade_faixa)
        faixas2[i].andar(velocidade_faixa)

    if faixas1[len(faixas1) - 1].x >= 100:
        faixas1.append(Faixa(283))
        faixas2.append(Faixa(427))
    if faixas1[0].x >= 1240:
        faixas1.pop(0)
        faixas2.pop(0)
    
    carro.desenhar()
    
    pg.display.update()

pg.quit()
sys.exit()