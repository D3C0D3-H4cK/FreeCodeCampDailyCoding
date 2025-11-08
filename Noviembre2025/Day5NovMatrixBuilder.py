def build_matrix(rows, cols):
    listPrincipal = []
    lista = []
    for i in range(rows): 
        for j in range(cols):
            lista.append(0)
            if len(lista) == cols:
                listPrincipal.append(lista)
        lista = []
            
                
            
    print(listPrincipal)
            

build_matrix(2, 3)