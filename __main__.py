import pygame as pg
import sys
import random
from Classes.carro import Carro
from Classes.pista import Pista
from Classes.fundo import Fundo
from Classes.espinho import Espinho
from Classes.vidas import Vidas

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
velocidade_bg = 1
pistas = [Pista(-1240, 'Pista1'), Pista(-3720, 'Pista1')]
fundos = [Fundo(-1240, 'Fundo1'), Fundo(-3720, 'Fundo1')]
carro = Carro('CarRed')
vidas = [Vidas(1050), Vidas(1100), Vidas(1150)]

espinhos = []
timer_espinhos = pg.USEREVENT + 1
pg.time.set_timer(timer_espinhos, 3000)


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == timer_espinhos:
            espinhos.append(Espinho('espinho'))

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

                if carro.vidas == 2:
                    vidas[2].morreu()
                elif carro.vidas == 1:
                    vidas[1].morreu()
                elif carro.vidas == 0:
                    vidas[0].morreu()

        if carro.hitbox.centery > limite_inferior_pista:
            carro.estado_queda = 'baixo'
        elif carro.hitbox.centery < limite_superior_pista:
            carro.estado_queda = 'cima'



    if carro.estado_queda != "nenhum":
        centro_antigo = carro._rect.center

        if carro.estado_queda == "baixo":
            direcao_rotacao = -8
            direcao_movimento = 1 
        else:  
            direcao_rotacao = 8
            direcao_movimento = -1 
        
        for vida in vidas:
            vida.morreu()
            
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
    
    for vida in vidas:
        tela.blit(vida._surf, vida._rect)
        
    tela.blit(carro._surf,carro._rect)
    pg.draw.rect(tela, (255, 0, 0), carro.hitbox, 2)
    for espinho in espinhos:
        pg.draw.rect(tela, (0, 0, 255), espinho.hitbox, 2)

    pg.display.update()

pg.quit()
sys.exit()