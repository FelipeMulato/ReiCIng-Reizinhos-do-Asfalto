#BIBLIOTECAS
import pygame as pg
import sys

#SOM
from Classes.som import Sons

#ETAPAS
from Etapas.tela_inicio import inicio
from Etapas.selecao import selecao
from Etapas.jogo import game
from Etapas.gameover import gameover
from Etapas.vitoria import vitoria

#Classes
from Classes.coracao_coletavel import hud_coracao_coletavel
from Classes.slow import hud_slow 

# Inicialização do sistema
pg.init()
pg.font.init() 

# HUDS
hud_coracao = hud_coracao_coletavel()
hud_slow_obj = hud_slow()

altura = 720
largura = 1240
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('ReiCIng')
relogio = pg.time.Clock()
relogio.tick(60)
musica = Sons()

running = True

# Loop principal
while running:
   musica.fundo()
   running = inicio(tela)

   if running:
      running, arquivo_carro = selecao(tela)

      if running:
         running, final, coracoes_coletados = game(tela, altura, largura, arquivo_carro, hud_coracao, hud_slow_obj)

         if final == 'morreu':
            musica.derrota()
            running = gameover(tela)
         elif final == 'ganhou':
            musica.vitoria()
            running = vitoria(tela)
        
         hud_coracao.desenhar(tela, coracoes_coletados)
         hud_slow_obj.desenhar(tela, 0)
         pg.display.update()

# Encerra o programa
pg.quit()
sys.exit()