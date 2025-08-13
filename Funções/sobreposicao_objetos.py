def sobreposicao_objeto(lista_objeto, paredes):
    
    for parede in paredes:
        for objeto in lista_objeto:
            if objeto.hitbox.colliderect(parede.hitbox):
                objeto.mudar_pos()  # Ajusta a posição do obstáculo para evitar sobreposição
