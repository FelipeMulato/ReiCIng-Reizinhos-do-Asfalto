import pygame as pg
import sys
import random
from Classes.carro import Carro
from Classes.pista import Pista
from Classes.fundo import Fundo
from Classes.espinho import Espinho
from Classes.trofeu import Trofeu

pg.init()
altura = 720
largura = 1240
relogio = pg.time.Clock()
relogio.tick(144)

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('ReiCIng')

limite_superior_pista = 140
limite_inferior_pista = 630
running = True
velocidade_bg = 5
pistas = [Pista(-1240, 'Pista1'), Pista(-3720, 'Pista1')]
fundos = [Fundo(-1240, 'Fundo1'), Fundo(-3720, 'Fundo1')]
carro = Carro('CarRed')

espinhos = []
timer_espinhos = pg.USEREVENT + 1
pg.time.set_timer(timer_espinhos, 3000)

trofeus = []
timer_trofeus = pg.USEREVENT +2
pg.time.set_timer(timer_trofeus, 23000)


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == timer_espinhos:
            espinhos.append(Espinho('espinho'))
        if event.type == timer_trofeus:
            trofeus.append(Trofeu("trofeu"))

    if carro.estado_queda == 'nenhum':
        if pg.key.get_pressed()[pg.K_UP]:
            carro.cima()
        if pg.key.get_pressed()[pg.K_DOWN]:
            carro.baixo()

        velocidade_bg += 0.0005

        if fundos[0].get_x() >= 1240:
            pistas.pop(0)
            pistas.append(Pista(-3720, 'Pista1'))
            fundos.pop(0)
            fundos.append(Fundo(-3720, 'Fundo1'))

        for i in range(2):
            pistas[i].mover(velocidade_bg)    
            fundos[i].mover(velocidade_bg)

        for espinho in espinhos[:]:
            espinho.mover_espinho(velocidade_bg)
            if espinho._rect.left > largura:
                espinhos.remove(espinho)

        for espinho in espinhos:
            if carro.hitbox.colliderect(espinho.hitbox):
                carro.perder_vida() 

        for trofeu in trofeus[:]:
            trofeu.mover_trofeu(velocidade_bg)
            if trofeu._rect.left > largura:
                trofeus.remove(trofeu)
        for trofeu in trofeus[:]:  # iterar sobre uma cópia da lista
            if carro.hitbox.colliderect(trofeu.hitbox):
                carro.ganhar_trofeu()
                trofeus.remove(trofeu)  # remove o troféu da tela após coleta


        if carro.hitbox.centery > limite_inferior_pista:
            carro.estado_queda = 'baixo'
        elif carro.hitbox.centery < limite_superior_pista:
            carro.estado_queda = 'cima'


    if carro.venceu: #jogador venceu, para o jogo
        running = False

    if carro.estado_queda != "nenhum":
        centro_antigo = carro._rect.center

        if carro.estado_queda == "baixo":
            direcao_rotacao = -8
            direcao_movimento = 1 
        else:  
            direcao_rotacao = 8
            direcao_movimento = -1 
        
        carro.angulo_rotação += direcao_rotacao
        carro.escala *= 0.97
        carro.velocidade_queda += 0.18

        carro._surf = pg.transform.rotozoom(carro._original_surf, carro.angulo_rotação, carro.escala)
        carro._rect = carro._surf.get_rect(center=centro_antigo)

        carro._rect.y += carro.velocidade_queda * direcao_movimento

        if carro._rect.top > altura or carro._rect.bottom < -110:
            carro.morrer()

    carro.checagem_invencibilidade()
    
    if carro.vidas <= 0:
        print('Morte')
        running = False
    
    for i in range(2):
        tela.blit(fundos[i]._surf, fundos[i]._rect) 
        tela.blit(pistas[i]._surf, pistas[i]._rect) 
    
    for espinho in espinhos:
        tela.blit(espinho._surf, espinho._rect)
        
    tela.blit(carro._surf,carro._rect)
    pg.draw.rect(tela, (255, 0, 0), carro.hitbox, 2)
    for espinho in espinhos:
        pg.draw.rect(tela, (0, 0, 255), espinho.hitbox, 2)


    for trofeu in trofeus:
        tela.blit(trofeu.surf, trofeu._rect)

    pg.display.update()



pg.quit()
sys.exit()