#BIBLIOTECAS
import pygame as pg
import sys

#ETAPAS
from jogo import game


# Inicialização do sistema
pg.init()
altura = 720
largura = 1240
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('ReiCIng')
relogio = pg.time.Clock()
relogio.tick(60)

running = True

# Loop principal
while running:
   running = game(tela, altura, largura, 'CarRed')


# Encerra o programa
pg.quit()
sys.exit()