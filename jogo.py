#BIBLIOTECAS
import pygame as pg

#CLASSES
from Classes.carro import Carro
from Classes.pista import Pista
from Classes.fundo import Fundo
from Classes.espinho import Espinho
from Classes.parede import Parede
from Classes.vidas import Vidas
from Classes.hud_trofeu import HUD_Trofeus
from Classes.trofeu import Trofeu
from Classes.slow import Slow
from Classes.coracao_coletavel import Coracao
from Classes.explosao import Explosao

#FUNÇÕES
from Funções.gerar_obstaculo import gerar_obstaculos
from Funções.mover_remover import mover_remover
from Funções.colisao_obstaculo import colisao_obstaculo
from Funções.sobreposicao_objetos import sobreposicao_objeto
from Funções.colisao_coletavel import colisao_coletavel


def game(tela, altura, largura, arquivo_carro):
    
    jogo = True
    limite_superior_pista = 140
    limite_inferior_pista = 630
    velocidade_bg = 10

    # Inicialização de objetos fixos
    pistas = [Pista(-1240), Pista(-3720)]
    fundos = [Fundo(-1240), Fundo(-3720)]
    carro = Carro(arquivo_carro)
    vidas = [Vidas(1050), Vidas(1100), Vidas(1150)]
    hud_trofeus = HUD_Trofeus()

    # Inicialização dos espinhos
    espinhos = []
    tempo_spawn_espinho = 1800
    prox_espinho = pg.time.get_ticks() + tempo_spawn_espinho

    # Inicialização das paredes
    paredes = []
    tempo_spawn_parede = 3000
    prox_parede = pg.time.get_ticks() + tempo_spawn_parede

    # Inicialização dos troféus
    trofeus = []
    timer_trofeus = pg.USEREVENT + 1
    pg.time.set_timer(timer_trofeus, 20000)

    # Inicialização dos slows
    slows = []
    tempo_spawn_slow = 18000
    prox_slow = pg.time.get_ticks() + tempo_spawn_slow
    slow_iniciado = False

    # Inicialização dos corações coletaveis
    coracao_coletavel_lista = []
    timer_coracao_coletavel = pg.USEREVENT + 2
    pg.time.set_timer(timer_coracao_coletavel, 25000)

    # Inicialização da explosão
    explosao = pg.sprite.Group()

    # Loop principal do jogo
    while jogo:

        # Eventos do jogo
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            if event.type == timer_trofeus:
                trofeus.append(Trofeu('trofeu'))
            if carro.vidas <3:
                if event.type == timer_coracao_coletavel:
                    coracao_coletavel_lista.append(Coracao())

        velocidade_bg += 0.0005  # Incrementa a velocidade do fundo

        # Geração dos obstáculos
        tempo_atual = pg.time.get_ticks()
        prox_espinho, tempo_spawn_espinho = gerar_obstaculos(tempo_atual, prox_espinho, espinhos, Espinho, tempo_spawn_espinho, 800)
        prox_parede, tempo_spawn_parede = gerar_obstaculos(tempo_atual, prox_parede, paredes, Parede, tempo_spawn_parede, 2000)
        prox_slow, tempo_spawn_slow = gerar_obstaculos(tempo_atual, prox_slow, slows, Slow, tempo_spawn_slow, 6000)
        
        # Verificar se algum objeto está sobreposto a uma parede
        sobreposicao_objeto(espinhos, paredes) if espinhos and paredes else None
        sobreposicao_objeto(trofeus, paredes) if trofeus and paredes else None
        sobreposicao_objeto(slows, paredes) if slows and paredes else None
        sobreposicao_objeto(coracao_coletavel_lista, paredes) if coracao_coletavel_lista and paredes else None
        
        # Carro está na pista
        if carro.estado_queda == 'nenhum':
            # Movimentação do carro
            if pg.key.get_pressed()[pg.K_UP]:
                carro.cima()
            if pg.key.get_pressed()[pg.K_DOWN]:
                carro.baixo()

            # Move e remove as pistas
            for i in range(2):
                pistas[i].mover(velocidade_bg)
                fundos[i].mover(velocidade_bg)
                if fundos[i].get_x() >= 1240:
                    pistas.pop(i)
                    pistas.append(Pista(-3720))
                    fundos.pop(i)
                    fundos.append(Fundo(-3720))

            # Move e remove os obstáculos
            mover_remover(paredes, velocidade_bg, largura)
            mover_remover(espinhos, velocidade_bg, largura)
            mover_remover(slows, velocidade_bg, largura)
            mover_remover(trofeus, velocidade_bg, largura)
            mover_remover(coracao_coletavel_lista, velocidade_bg, largura)
            # Colisão com os obstáculos
            colisao_obstaculo(carro, espinhos, vidas)
            colisao_obstaculo(carro, paredes, vidas)
            # Colisão com os coletáveis
            colisao_coletavel(carro, coracao_coletavel_lista, vidas)
            colisao_coletavel(carro, slows, vidas)

            # Colisão dos troféus com o carro
            for trofeu in trofeus:
                if carro.hitbox.colliderect(trofeu.hitbox) and not trofeu.pego:
                    trofeu.pego = True
                    if carro.trofeus == 2:
                        for i in range(len(espinhos) - 1, -1, -1):
                            espinhos.pop(i)

                    # Calcula a equação do segundo grau para realizar a movimentação do troféu em forma de parábola
                    xv = trofeu._rect.x
                    yv = trofeu._rect.y
                    a = (109 - yv) / (102 - xv)**2
                    b = (2 * (109 - yv) * xv) / (102 - xv)**2
                    c = ((yv * 4 * a) + b**2) / 4 * a
                    x = trofeu.voar(xv, a, b, c)

                if trofeu.pego:  # Leva o troféu até o contador
                    if trofeu._rect.colliderect((30, 30, 160, 75)):  # Coleta o troféu
                        carro.ganhar_trofeu()
                        hud_trofeus.pegou_trofeu(carro.trofeus)
                        # Remove o troféu da tela após coleta
                        trofeus.remove(trofeu)
                    else:  # Move o troféu novamente
                        x = trofeu.voar(x, a, b, c)

            # Checar se o carro caiu da pista
            if carro.hitbox.centery > limite_inferior_pista:
                carro.estado_queda = 'baixo'
            elif carro.hitbox.centery < limite_superior_pista:
                carro.estado_queda = 'cima'

        # Carro caiu da pista
        elif carro.estado_queda == 'cima' or carro.estado_queda == 'baixo':
            centro_antigo = carro._rect.center

            if carro.estado_queda == 'baixo':
                direcao_rotacao = -8
                direcao_movimento = 1
            elif carro.estado_queda == 'cima':
                direcao_rotacao = 8
                direcao_movimento = -1
        
            # Remove todas as vidas do HUD
            for vida in vidas:
                if vida.viva:
                    vida.morreu()
                    vida.viva = False
                    vida.blink = True
                    vida.tempo_blink = pg.time.get_ticks()

            carro.angulo_rotação += direcao_rotacao
            carro.escala *= 0.97
            carro.velocidade_queda += 0.18

            carro._surf = pg.transform.rotozoom(carro._original_surf, carro.angulo_rotação, carro.escala)
            carro._rect = carro._surf.get_rect(center=centro_antigo)

            carro._rect.y += carro.velocidade_queda * direcao_movimento

            if carro._rect.top > altura or carro._rect.bottom < -110 :
                carro.morrer()
        
        # Carro colidiu com a parede
        elif carro.estado_queda == 'colidiu':
            carro_tempo_colisao = pg.time.get_ticks()

            velocidade_bg = 0

            explosao.add(Explosao(carro._rect.centerx, carro._rect.centery))
            carro.estado_queda = 'explodindo'

            # Remove vidas do HUD
            for vida in vidas:
                if vida.viva:
                    vida.morreu()
                    vida.viva = False
                    vida.blink = True
                    vida.tempo_blink = pg.time.get_ticks()

        # Sprite de colisão
        elif carro.estado_queda == 'explodindo':
            if pg.time.get_ticks() - carro_tempo_colisao > 300:
                carro.morrer()
                
        # Checar se o tempos das respostas visuais já acabou 
        carro.checagem_invencibilidade()
        carro.checagem_slow()
        for vida in vidas:
            vida.checagem_blink()

        # Aplicação do efeito do slow
        if carro.slow and not slow_iniciado:
            slow_iniciado = True
            velocidade_anterior = velocidade_bg
            espinho_anterior = tempo_spawn_espinho
            parede_anterior = tempo_spawn_parede
            slow_anterior = tempo_spawn_slow

            velocidade_bg = 8
            tempo_spawn_espinho = 3000
            tempo_spawn_parede = 5000
            tempo_spawn_slow = 18000

        # Retorno para a situação anterior ao slow
        elif not carro.slow and slow_iniciado:
            slow_iniciado = False

            velocidade_bg = velocidade_anterior
            tempo_spawn_espinho = espinho_anterior
            tempo_spawn_parede = parede_anterior
            tempo_spawn_slow = slow_anterior


        if carro.vidas <= 0:  # Jogador morreu, para o jogo
            print('Morte')
            jogo = False
        if carro.venceu:  # Jogador venceu, para o jogo
            print('Venceu')
            jogo = False

        # Desenha todos os elementos visuais na tela e atualiza o display
        for i in range(2):
            tela.blit(fundos[i]._surf, fundos[i]._rect)
            tela.blit(pistas[i]._surf, pistas[i]._rect)
        for espinho in espinhos:
            tela.blit(espinho._surf, espinho._rect)
        for parede in paredes:
            tela.blit(parede._surf, parede._rect)
        for trofeu in trofeus:
            tela.blit(trofeu.surf, trofeu._rect)
        for slow in slows:
            tela.blit(slow._surf, slow._rect)
        for coracao in coracao_coletavel_lista:
            tela.blit(coracao._surf, coracao._rect)

        tela.blit(hud_trofeus._surf, hud_trofeus._rect)

        desenhar_carro = True
        desenhar_vida = True
        trigger = (pg.time.get_ticks() // 100) % 2

        if carro.invencivel == True: # Resposta visual para quando o carro sofre dano
            if trigger == 0:
                desenhar_carro = False

        if desenhar_carro == True and carro.estado_queda not in ['colidiu', 'explodindo']:
            tela.blit(carro._surf, carro._rect)

        for vida in vidas: # Resposta visual no HUD para quando perde uma vida
            if vida.blink:
                if trigger == 0:
                    desenhar_vida = False
        
        for vida in vidas:
            if vida.blink:
                if not desenhar_vida:
                    vida.viveu()
                else:
                    vida.morreu()
            else:
                if vida.viva:
                    vida.viveu()
                else:
                    vida.morreu()

            tela.blit(vida._surf, vida._rect)

        explosao.draw(tela) # Sprite da explosão
        explosao.update()
            
        pg.display.update()

    return True