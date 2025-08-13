#BIBLIOTECAS
import pygame as pg
import sys

#ETAPAS
from Etapas.tela_inicio import inicio
from Etapas.selecao import selecao
from Etapas.jogo import game
from Etapas.gameover import gameover
from Etapas.vitoria import vitoria

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
   running = inicio(tela)

   if running:
      running, arquivo_carro = selecao(tela)

      if running:
         running, final = game(tela, altura, largura, arquivo_carro)

         if final == 'morreu':
            running = gameover(tela)
         elif final == 'ganhou':
            running = vitoria(tela)


# Encerra o programa
pg.quit()
sys.exit()