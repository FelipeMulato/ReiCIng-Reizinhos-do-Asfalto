import pygame as pg

from Classes import carro

def colisao_obstaculo(carro, lista_obstaculos, vidas):

    for obstaculo in lista_obstaculos[:]:
        if carro.hitbox.colliderect(obstaculo.hitbox):
            
            if obstaculo.__class__.__name__ == 'Espinho':
                som_dano = pg.mixer.Sound("Áudios/playerhit.mp3")
                som_dano.set_volume(0.6)
                som_dano.play()
                carro.perder_vida()
                
                if carro.vidas == 2:
                    vidas[2].morreu()
                    vidas[2].viva = False
                    vidas[2].blink = True
                    vidas[2].tempo_blink = pg.time.get_ticks()
                elif carro.vidas == 1:
                    vidas[1].morreu()
                    vidas[1].viva = False
                    vidas[1].blink = True
                    vidas[1].tempo_blink = pg.time.get_ticks()
                elif carro.vidas == 0:
                    vidas[0].morreu()
                    vidas[0].viva = False
                    vidas[0].blink = True
                    vidas[0].tempo_blink = pg.time.get_ticks()
                    
            elif obstaculo.__class__.__name__ == 'Parede':
                carro.estado_queda = 'colidiu'
                carro.velocidade = 0
                carro.tempo_queda = pg.time.get_ticks()