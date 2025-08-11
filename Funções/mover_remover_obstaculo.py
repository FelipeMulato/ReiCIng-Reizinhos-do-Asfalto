def mover_remover_obstaculos(lista, velocidade, largura):
    for obstaculo in lista:
        obstaculo.mover(velocidade)
        if obstaculo._rect.left > largura:
            lista.remove(obstaculo)