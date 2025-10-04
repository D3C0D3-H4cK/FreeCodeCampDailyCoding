def array_diff(arr1, arr2):
    diferencia = list(set(arr1) ^ set(arr2))
    diferencia.sort()
    print(diferencia)



array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"])