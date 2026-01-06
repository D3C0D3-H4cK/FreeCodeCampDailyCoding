def purge_most_frequent(arr):
    lista = []
    elemento_mas_repetido = max(set(arr), key=arr.count)
    for i in arr:
        if i != elemento_mas_repetido:
            lista.append(i)
    print(lista)

purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"])