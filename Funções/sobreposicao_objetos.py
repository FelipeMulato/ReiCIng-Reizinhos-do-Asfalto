def sobreposicao_obstaculo(obstaculos1, obstaculos2):
    for obstaculo1 in obstaculos1:
        for obstaculo2 in obstaculos2:
            if obstaculo1.hitbox.colliderect(obstaculo2.hitbox):
                obstaculo1._rect.y -= 10  # Ajusta a posição do obstáculo para evitar sobreposição
                obstaculo2._rect.y += 10  # Ajusta a posição do outro obstáculo