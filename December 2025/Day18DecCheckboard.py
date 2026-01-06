""""
def create_board(dimensions):
    list = []
    for i in range(dimensions[0]):
        objetos = []
        for j in range(dimensions[1]):
            if (i + j) % 2 == 0:
                objetos.append('X')
            else:
                objetos.append('O')
        list.append(objetos)
    print(list)
"""
def create_board(dimensions):
    list = []
    for i in range(dimensions[0]):
        objetos = []
        for j in range(dimensions[1]):
            if (i + j) % 2 == 0:
                objetos.append('X')
            else:
                objetos.append('O')
        list.append(objetos)
    print(list)
            
    

create_board([2, 10]) 

