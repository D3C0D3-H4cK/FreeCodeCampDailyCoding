def find_pawn_moves(position):
    column = position[0]          # Letra
    row = int(position[1])        # Número convertido a entero
    
    moves = []
    
    # Movimiento normal (una casilla hacia arriba)
    if row + 1 <= 8:
        moves.append(f"{column}{row + 1}")
    
    # Movimiento doble si está en fila inicial
    if row == 2 and row + 2 <= 8:
        moves.append(f"{column}{row + 2}")
    
    print(sorted(moves))
    
find_pawn_moves("D4")