def shift_matrix(matrix, shift):
    rows = len(matrix)
    cols = len(matrix[0])
    total = rows * cols
    nuevamatrix = [[0 for _ in range(cols)] for _ in range(rows)]
    shift = ((shift % total) + total)% total
    for r in range(rows):
        for c in range(cols):
            pos = r * cols + c
            nueva_posición = (pos + shift) % total
            new_r = nueva_posición // cols
            new_c = nueva_posición % cols
            nuevamatrix[new_r][new_c] = matrix[r][c]
    print(nuevamatrix)
shift_matrix([[1, 2, 3], [4, 5, 6]], 1)