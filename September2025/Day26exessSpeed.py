def speeding(speeds, limit):
    exess = []
    total = []
    for i in speeds:
        if i > limit:
            exessLimit = i - limit
            exess.append(exessLimit)
            average  = sum(exess) / len(exess)
    if len(exess) == 0:
        return [0, 0]
    if average.is_integer():
        average = int(average)
    
    total.append(len(exess))
    total.append(average)
    print(total)
            
            
speeding([50, 60, 55], 60)