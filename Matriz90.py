def rotate(matrix):
    numero = len(matrix)
    final = []
    if len(matrix) > 1: 
        for l in range(numero):
            columnas = []
            for i in matrix:
                columnas.append(i[l])
            final.append(columnas[:][::-1])
        print(final)
    else:
        return matrix
                
rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])