"""
Space Week Day 4: Landing Spot

In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

    Each spot in the matrix will contain a number from 0-9, inclusive.
    Any 0 represents a potential landing spot.
    Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
    The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
    Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
    Return the indices of the safest landing spot. There will always only be one safest spot.

For instance, given:

"""


def find_landing_spot(matrix):
    posiciones = []
    suma = []
    for i in range(len(matrix)):
        for l in range(len(matrix[i])):
            if matrix[i][l] == 0:
                numeros = []
                posicion = [i, l]
                posiciones.append(posicion)
                if i > 0:
                    numeros.append(matrix[i - 1][l])
                if i < len(matrix) -1:
                    numeros.append(matrix[i + 1][l])
                if l > 0:
                    numeros.append(matrix[i][l - 1])
                if l < len(matrix[i])  -1 :
                    numeros.append(matrix[i][l + 1])
                suma.append(sum(numeros))
    posicionFinal = suma.index(min(suma))
    return posiciones[posicionFinal]

            
find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]])