import pygame as pg
import sys
from Classes.carro import Carro
from Classes.pista import Pista
from Classes.fundo import Fundo
from Classes.espinho import Espinho
from Classes.vidas import Vidas
from Classes.trofeu import Trofeu
from Classes.slow import SLow


pg.init()
altura = 720
largura = 1240
relogio = pg.time.Clock()
relogio.tick(60)

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('ReiCIng')

# Inicialização de objetos
limite_superior_pista = 140
limite_inferior_pista = 630
running = True
velocidade_bg = 2
pistas = [Pista(-1240, 'Pista1'), Pista(-3720, 'Pista1')]
fundos = [Fundo(-1240, 'Fundo1'), Fundo(-3720, 'Fundo1')]
carro = Carro('CarRed')
vidas = [Vidas(1050), Vidas(1100), Vidas(1150)]
espinhos = []
timer_espinhos = pg.USEREVENT + 1
pg.time.set_timer(timer_espinhos, 3000)
trofeus = []
timer_trofeus = pg.USEREVENT +2
pg.time.set_timer(timer_trofeus, 23000)
slows=[]
timer_slow= pg.USEREVENT +3
pg.time.set_timer(timer_slow, 30000)

# Loop principal do jogo
while running:
    # Eventos do jogo
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == timer_espinhos:
            espinhos.append(Espinho('espinho'))
        if event.type == timer_trofeus:
            trofeus.append(Trofeu('trofeu'))
        if event.type == timer_slow:
            slows.append(SLow('slow'))
    # Carro está na pista
    if carro.estado_queda == 'nenhum':
        # Movimentação do carro
        if pg.key.get_pressed()[pg.K_UP]:
            carro.cima()
        if pg.key.get_pressed()[pg.K_DOWN]:
            carro.baixo()

        velocidade_bg += 0.0005 # Incrementa a velocidade do fundo

        # Move e remove as pistas
        for i in range(2):
            pistas[i].mover(velocidade_bg)    
            fundos[i].mover(velocidade_bg)
            if fundos[i].get_x() >= 1240:
                pistas.pop(i)
                pistas.append(Pista(-3720, 'Pista1'))
                fundos.pop(i)
                fundos.append(Fundo(-3720, 'Fundo1'))
        
        # Move e remove os espinhos
        for espinho in espinhos[:]:
            espinho.mover_espinho(velocidade_bg)
            if espinho._rect.left > largura:
                espinhos.remove(espinho)
        # Colisão dos espinhos com o carro
        for espinho in espinhos:
            if carro.hitbox.colliderect(espinho.hitbox):
                carro.perder_vida() 
                if carro.vidas == 2: # Perde a vida no HUD
                    vidas[2].morreu()
                elif carro.vidas == 1:
                    vidas[1].morreu()
                elif carro.vidas == 0:
                    vidas[0].morreu()

        # Move e remove os troféus
        for trofeu in trofeus[:]:
            trofeu.mover_trofeu(velocidade_bg)
            if trofeu._rect.left > largura:
                trofeus.remove(trofeu)
            # Colisão dos troféus com o carro
            if carro.hitbox.colliderect(trofeu.hitbox):
                carro.ganhar_trofeu()
                trofeus.remove(trofeu)  # remove o troféu da tela após coleta

         # Move e remove os Slows
        for slow in slows[:]:
            slow.movimentação_slow(velocidade_bg)
            if slow._rect.left > largura:
                slows.remove(slow)
            # Colisão do slow com o carro
            if carro.hitbox.colliderect(slow.hitbox):
                #velocidade_bg= velocidade_bg//2 #toda vez que pegar o slow a velocidade é diminuida
                velocidade_bg = carro.ganhar_slow(velocidade_bg)
                slows.remove(slow)  # remove o slow da tela após coleta


        # Checar se o carro caiu da pista     
        if carro.hitbox.centery > limite_inferior_pista:
            carro.estado_queda = 'baixo'
        elif carro.hitbox.centery < limite_superior_pista:
            carro.estado_queda = 'cima'

    

    # Carro caiu da pista
    if carro.estado_queda != 'nenhum':
        centro_antigo = carro._rect.center

        if carro.estado_queda == 'baixo':
            direcao_rotacao = -8
            direcao_movimento = 1 
        else:  
            direcao_rotacao = 8
            direcao_movimento = -1 
        
        # Remove todas as vidas do HUD
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

    # Testar se o tempo de invencibilidade acabou
    carro.checagem_invencibilidade()
    

    if carro.vidas <= 0: # Jogador morreu, para o jogo
        print('Morte')
        running = False
    if carro.venceu: # Jogador venceu, para o jogo
        print('Venceu')
        running = False
    
    # Desenha todos os elementos visuais na tela e atualiza o display
    for i in range(2):
        tela.blit(fundos[i]._surf, fundos[i]._rect) 
        tela.blit(pistas[i]._surf, pistas[i]._rect) 
    
    for espinho in espinhos:
        tela.blit(espinho._surf, espinho._rect)

    desenhar_carro = True
    
    if carro.invencivel == True:
        trigger = (pg.time.get_ticks() // 100) % 2
        if trigger == 0:
            desenhar_carro = False
    
    if desenhar_carro == True:
        tela.blit(carro._surf,carro._rect)
        pg.draw.rect(tela, (255, 0, 0), carro.hitbox, 2)

    
    for vida in vidas:
        tela.blit(vida._surf, vida._rect)
        
    for espinho in espinhos:
        pg.draw.rect(tela, (0, 0, 255), espinho.hitbox, 2)

    for trofeu in trofeus:
        tela.blit(trofeu.surf, trofeu._rect)

    for slow in slows:
        tela.blit(slow.retrato, slow._rect)
    
    pg.display.update()

# Encerra o programa
pg.quit()
sys.exit()