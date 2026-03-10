def knight_moves(position):
    letras = "ABCDEFGH"

    col = position[0]
    fila = int(position[1])

    col_num = letras.index(col)

    # movimientos posibles del caballo
    movimientos = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    posiciones_validas = []

    for dx, dy in movimientos:
        nueva_col = col_num + dx
        nueva_fila = fila + dy

        # validar que no se salga del tablero
        if 0 <= nueva_col < 8 and 1 <= nueva_fila <= 8:
            posiciones_validas.append(letras[nueva_col] + str(nueva_fila))

    return len(posiciones_validas)