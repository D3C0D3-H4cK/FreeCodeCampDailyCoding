def score_curling(house):
    equipoR = []
    equipoY = []
    for i in range(len(house)):
        for j in range(len(house[i])):
            cell = house[i][j]
            position = i,j
            if cell == "R": 
                if i == 2 and j == 2:
                    equipoR.append(0)
                elif i == 0 or i == 4 or j == 0 or j == 4:
                    equipoR.append(2)
                else: 
                    equipoR.append(1)
            if cell == "Y":    
                if i == 2 and j == 2:
                    equipoY.append(0)
                elif i == 0 or i == 4 or j == 0 or j == 4:
                    equipoY.append(2)
                else: 
                    equipoY.append(1)
                
                
    if not equipoR and not equipoY:
        return "No points awarded"
    if not equipoR:
        return f"R: {len(equipoY)}"
    if not equipoY:
        return f"R: {len(equipoR)}"
    minR = min(equipoR)
    minY = min(equipoY)
    
    if minR == minY:
        return "No points awarded"
    if minR < minY:
        puntos = 0
        for r in equipoR:
            if r < minY:
                puntos += 1 
        print( f"R:{puntos}")
    elif minY < minR:
        puntos = 0
        for r in equipoY:
            if r < minR:
                puntos += 1 
                print( f"Y: {puntos}")
              
score_curling([[".", ".", "R", ".", "."], [".", "R", ".", ".", "."], ["Y", ".", ".", ".", "."], [".", "R", ".", ".", "."], [".", ".", ".", ".", "."]]) 