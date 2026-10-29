def get_meeting_time(availability):
    bloquesPrincipal = []
    for i in range(len(availability[0])):
        bloques = []
        for persona in availability:
            bloques.append(persona[i])
        bloquesPrincipal.append(bloques)
    for i in range(len(bloquesPrincipal)):
        for j in range(len(bloquesPrincipal[i])):
            print(bloquesPrincipal[i][j][0], i,j)

    
            
get_meeting_time([[[9, 10], [12, 15]], [[10, 11], [13, 14]], [[9, 11], [10, 14]]])