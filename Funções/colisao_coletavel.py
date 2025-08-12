import pygame as pg

def colisao_coletavel(carro, lista_coletavel, velocidade_bg, vidas):
    for coletavel in lista_coletavel[:]: 
        if coletavel.__class__.__name__ == 'Slow':
            if carro.hitbox.colliderect(coletavel.hitbox):
                carro.ganhar_slow()
                lista_coletavel.remove(coletavel)

                carro.slow = True
                carro.inicio_slow = pg.time.get_ticks()

        elif coletavel.__class__.__name__ == 'Coracao':
            if carro.hitbox.colliderect(coletavel.hitbox):
                carro.ganhar_vida()
                lista_coletavel.remove(coletavel)

                if carro.vidas == 3:
                    vidas[2].viveu()
                    vidas[2].viva = True
                    vidas[2].blink = True
                    vidas[2].tempo_blink = pg.time.get_ticks()
                elif carro.vidas == 2:
                    vidas[1].viveu()
                    vidas[1].viva = True
                    vidas[1].blink = True
                    vidas[1].tempo_blink = pg.time.get_ticks()
