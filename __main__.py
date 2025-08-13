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
velocidade_bg = 10
velocidade_anterior = 10
pistas = [Pista(-1240, 'Pista1'), Pista(-3720, 'Pista1')]
fundos = [Fundo(-1240, 'Fundo1'), Fundo(-3720, 'Fundo1')]
carro = Carro('CarRed')
vidas = [Vidas(1050), Vidas(1100), Vidas(1150)]
hud_trofeus = HUD_Trofeus()
# Inicialização do Espinho
espinhos = []
tempo_spawn_espinho = 3000
prox_espinho = pg.time.get_ticks() + tempo_spawn_espinho
# Inicialização da Parede
paredes = []
tempo_spawn_parede = 5000
prox_parede = pg.time.get_ticks() + tempo_spawn_parede
# Inicialização do Troféu
trofeus = []
timer_trofeus = pg.USEREVENT + 1
pg.time.set_timer(timer_trofeus, 20000)
# Inicialização do Slow
slows = []
tempo_spawn_slow = 18000
prox_slow = pg.time.get_ticks() + tempo_spawn_slow
slow_iniciado = False
# Inicialização coração coletavel
coracao_coletavel_lista = []
timer_coracao_coletavel = pg.USEREVENT + 2
pg.time.set_timer(timer_coracao_coletavel, 25000)

explosao = pg.sprite.Group()

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