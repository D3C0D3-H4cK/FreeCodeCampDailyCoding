def shift_array(arr, n):

    n = n % len(arr)
    if n > 0:
        print( arr[n:] + arr[:n])
    elif n < 0:
        print( arr[n:] + arr[:n])
    else:
        print( arr)
        
shift_array(["alpha", "bravo", "charlie"], -11)