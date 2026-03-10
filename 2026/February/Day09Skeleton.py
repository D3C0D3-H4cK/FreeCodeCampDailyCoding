def get_difficulty(track):
    traqueo = 0
    for actual, siguiente in zip(track, track[1:]):
        if actual == "R" and siguiente == "L":
            traqueo += 15
        elif actual == "L" and siguiente == "R":
            traqueo += 15
        elif actual == "S" and siguiente == "R" or siguiente == "L":
            traqueo += 5
    if traqueo <= 100:
        print("Easy")
    elif 101 <= traqueo <= 199 :
        print("Medium")
    else:
        print("Hard")


get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR")