def build_matrix(rows, cols):
    lista = [] 
    contador = 0     
    numero = 0
    while len(lista) < rows:
        lista.append([])
        for i in range(cols):
            lista[contador].append(numero)
            numero += 1
        contador += 1
    print(lista)
build_matrix(4, 3)