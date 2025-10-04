
def tribonacci_sequence(start_sequence, length):
    tribonachi = start_sequence[:]
    if length == 0:
        return []
    if length <= 3:
        tribonachi = start_sequence[:length]
        print(tribonachi)
    else: 
        for i in range(3, length):
            suma = tribonachi[-3] + tribonachi[-2] + tribonachi[-1]
            tribonachi.append(suma)
            print(tribonachi)
    
tribonacci_sequence([21, 32, 43], 1)


def tribonacci_sequence(start_sequence, length):
    # caso especial: si length == 0
    if length == 0:
        return []
    
    # inicializar la lista con la secuencia inicial
    tribonachi = start_sequence[:]
    
    # si length <= 3 devolvemos solo lo que pidieron
    if length <= 3:
        return tribonachi[:length]
    
    # si length > 3, generamos hasta llegar al tamaño pedido
    for i in range(3, length):
        suma = tribonachi[-3] + tribonachi[-2] + tribonachi[-1]
        tribonachi.append(suma)
    
    return tribonachi