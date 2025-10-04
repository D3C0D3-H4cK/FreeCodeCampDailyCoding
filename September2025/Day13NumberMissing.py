def find_missing_numbers(arr):
    newList = []
    for i in range(1, max(arr) + 1):
        newList.append(i)
        if i in arr:
            newList.remove(i)
    print(newList)
find_missing_numbers([1, 2, 3, 4, 5])