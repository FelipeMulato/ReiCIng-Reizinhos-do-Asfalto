import pygame as pg
import sys
import random
from Classes.carro import Carro
from Classes.pista import Pista
from Classes.fundo import Fundo
from Classes.espinho import Espinho

pg.init()
altura = 720
largura = 1240
relogio = pg.time.Clock()
relogio.tick(144)

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('ReiCIng')

running = True
velocidade_bg = 1
pistas = [Pista(-1240, 'Pista1'), Pista(-3720, 'Pista1')]
fundos = [Fundo(-1240, 'Fundo1'), Fundo(-3720, 'Fundo1')]
carro = Carro('CarRed')

espinhos = []
timer_espinhos = pg.USEREVENT + 1
pg.time.set_timer(timer_espinhos, 3000)


while running:
    velocidade_bg += 0.0005

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == timer_espinhos:
            espinhos.append(Espinho('espinho'))

    if pg.key.get_pressed()[pg.K_UP]:
        carro.cima()
    if pg.key.get_pressed()[pg.K_DOWN]:
        carro.baixo()

    carro.checagem_invencibilidade()

    for i in range(2):
        pistas[i].mover(velocidade_bg)    
        fundos[i].mover(velocidade_bg)

    for espinho in espinhos[:]:
        espinho.mover_espinho(velocidade_bg)
        if espinho._rect.left > largura:
            espinhos.remove(espinho)

    for espinho in espinhos:
        if carro._rect.colliderect(espinho._rect):
            carro.perder_vida() 

    if fundos[0].get_x() >= 1240:
        pistas.pop(0)
        pistas.append(Pista(-3720, 'Pista1'))
        fundos.pop(0)
        fundos.append(Fundo(-3720, 'Fundo1'))
    
    if carro.vidas <= 0:
        print('Morte')
        running = False
    
    for i in range(2):
        tela.blit(fundos[i]._surf, fundos[i]._rect) 
        tela.blit(pistas[i]._surf, pistas[i]._rect) 
    
    for espinho in espinhos:
        tela.blit(espinho._surf, espinho._rect)
        
    tela.blit(carro._surf,carro._rect)

    pg.display.update()

pg.quit()
sys.exit()