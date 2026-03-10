def is_sorted(arr):
    asc = True
    desc = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            asc = False
        if arr[i] > arr[i - 1]:
            desc = False

    if asc:
        return "Ascending"
    elif desc:
        return "Descending"
    else:
        return "Not sorted"

