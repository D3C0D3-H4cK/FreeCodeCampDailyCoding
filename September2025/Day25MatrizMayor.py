def second_largest(arr):
    array = max(arr)
    while array in arr:
        arr.remove(array)
    print(max(arr))
