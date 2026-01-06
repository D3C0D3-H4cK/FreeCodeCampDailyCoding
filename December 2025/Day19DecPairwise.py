def pairwise(arr, target):
    lista = set()
    total = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if i not in lista and j not in lista:
                if arr[i] + arr[j] == target:
                    total += i + j
                    lista.add(i)
                    lista.add(j)

    print(total)
pairwise([4, 1, 5, 2, 6, 3], 7)