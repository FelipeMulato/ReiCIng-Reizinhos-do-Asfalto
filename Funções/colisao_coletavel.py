import pygame as pg

def colisao_coletavel(carro, lista_coletavel, vidas):
    for coletavel in lista_coletavel[:]: 
        if coletavel.__class__.__name__ == 'Slow':
            if carro.hitbox.colliderect(coletavel.hitbox):
                som_slow = pg.mixer.Sound("Áudios/time.mp3")
                som_slow.set_volume(0.5)
                som_slow.play()
                carro.ganhar_slow()
                lista_coletavel.remove(coletavel)
        
        elif coletavel.__class__.__name__ == 'Coracao':
            if carro.hitbox.colliderect(coletavel.hitbox):
                carro.ganhar_vida()
                lista_coletavel.remove(coletavel)

                som_coracao = pg.mixer.Sound("Áudios/Cure1.wav")
                som_coracao.set_volume(0.5)
                som_coracao.play()

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