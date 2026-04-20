def dive(map, coordinates):
    tesoure = map[coordinates[0]][coordinates[1]]
    if tesoure == '-':
        print("Empty")
    if tesoure == 'X':
        print("found")
    if tesoure == 'O':
        if coordinates[0] < len(map) - 1:
            if 'O' in map[coordinates[0 + 1]]:
                print( "Found")
        else:
                print("Recovered")
        
        
dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0])