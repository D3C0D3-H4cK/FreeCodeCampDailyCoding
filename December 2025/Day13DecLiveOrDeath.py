"""Game of Life

Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the matrix using these rules:

    Each cell is either 1 (alive) or 0 (dead).
    A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
    Cells on the edges have fewer than eight neighbors.

Rules for updating each cell:

    Any live cell with fewer than two live neighbors dies (underpopulation).
    Any live cell with two or three live neighbors lives on.
    Any live cell with more than three live neighbors dies (overpopulation).
    Any dead cell with exactly three live neighbors becomes alive (reproduction).
"""

def game_of_life(grid):
    newGrid = []
    for i in range(len(grid)):
        filaNueva = []
        for j in range(len(grid[0])):
            suma = 0
            if i - 1 >= 0:
                if grid[i - 1][j]== 1:
                    suma += 1
            if i + 1 < len(grid):
                if grid[i + 1][j]== 1:
                    suma += 1
            if j - 1 >= 0:
                if grid[i][j -1 ]== 1:
                    suma += 1
            if j + 1 < len(grid[0]):
                if grid[i][j + 1]== 1:
                    suma += 1
            if i - 1 >= 0 and j - 1 >= 0:
                if grid[i - 1][j - 1] == 1:
                    suma += 1
            if i - 1 >= 0 and j + 1 < len(grid[0]):
                if grid[i - 1][j + 1] == 1:
                    suma += 1
            if i + 1 < len(grid) and j - 1 >= 0:
                if grid[i + 1][j - 1] == 1:
                    suma += 1
            if i + 1 < len(grid) and j + 1 < len(grid[0]):
                if grid[i + 1][j + 1] == 1:
                    suma += 1
            if grid[i][j] == 1:
                if suma < 2 or suma > 3:
                    filaNueva.append(0)  
                else:
                    filaNueva.append(1)  
            else:
                if suma == 3:
                        filaNueva.append(1)  
                else:
                    filaNueva.append(0) 
    
        newGrid.append(filaNueva)
    print(newGrid)    
game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]])

#Que ejercicio mas dificil