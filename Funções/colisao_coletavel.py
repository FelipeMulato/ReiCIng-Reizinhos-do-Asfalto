def colisao_coletavel(carro, lista_coletavel, lista_espinhos, hud_trofeus, velocidade_bg):

    for coletavel in lista_coletavel:
     
        if coletavel.__class__.__name__ == 'Slow':

            #Colisão do slow com o carro
            if carro.hitbox.colliderect(coletavel.hitbox):
                carro.ganhar_slow()

                if velocidade_bg <= 2:
                    incremento = 0
                else:    
                    incremento = -1

                return velocidade_bg + incremento
            else:

                return velocidade_bg