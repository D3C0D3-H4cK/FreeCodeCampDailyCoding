def get_frequency(s):
    contador = 0 
    lista = []
    diccionary = {}
    for i in s:
        if i not in lista:
            lista.append(i) 
            diccionary[i] = s.count(i)  
    print(diccionary)
get_frequency("The quick brown fox jumps over the lazy dog.")