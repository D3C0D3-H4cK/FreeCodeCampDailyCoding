def find_differences(arr):
    final = []
    for i in range(len(arr)):
        if i + 1 < len(arr):
            posicionDelantera = arr[i + 1]
            posicionTrasera = arr[i]
            resultado = posicionDelantera - posicionTrasera
            final.append(resultado)
    final.append(0)
    print(final)

find_differences([1, 2, 4, 7])