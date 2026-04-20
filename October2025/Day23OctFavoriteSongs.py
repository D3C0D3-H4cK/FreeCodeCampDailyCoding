def favorite_songs(playlist):
    diccionario_ordenado = sorted(playlist, key=lambda x: x['plays'], reverse=True)
    cancionesMas = []
    for i in range(2):
        cancionesMas.append(diccionario_ordenado[i]['title'])
    
    return cancionesMas

favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ])