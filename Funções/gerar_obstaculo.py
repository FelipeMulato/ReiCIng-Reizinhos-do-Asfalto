def gerar_obstaculos(tempo_atual, proximo, lista, classe, tempo_spawn, tempo_minimo):
    
    if tempo_atual >= proximo:
        lista.append(classe(f'{classe.__name__}'))
        tempo_spawn *= 0.98

        if tempo_spawn < tempo_minimo:
            tempo_spawn = tempo_minimo
            print(f'Taxa de spawn de {classe.__name__} máxima atingida! : {1 / (tempo_minimo / 1000):.2F} esp/s')
        proximo = tempo_atual + tempo_spawn
    
    return proximo, tempo_spawn