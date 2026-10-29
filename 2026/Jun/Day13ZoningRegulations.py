def get_zone_violations(grid):

    prohibidos = {
    "i": ["R", "I"],
    "A": ["C"],
    "R": ["i", "C"],
    "I": ["i"],
    "C": ["R", "A"]
    }
    lista = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            actual = grid[i][j]
            if actual == "":
                continue
            
            if j + 1 < len(grid[i]):
                if grid[i][j+1] in prohibidos[actual]:
                        lista.append([i,j])
                        continue

            if j - 1 >= 0:
                if grid[i][j - 1] in prohibidos[actual]:
                        lista.append([i,j])
                        continue

            if i + 1 < len(grid):
                if grid[i + 1][j] in prohibidos[actual]:
                        lista.append([i,j])
                        continue

            if i - 1 >= 0:
                if grid[i - 1][j] in prohibidos[actual]:
                        lista.append([i,j])
                        continue

                    
    print(lista)
                
get_zone_violations([["R", "R", "C", "R", "R"], ["R", "I", "C", "", "A"], ["R", "R", "", "i", "A"]])
