def get_fastest_speed(times):
    meters = [320,280,350,300,250]
    final = []
    for i,j in zip(times,meters):
        total = j / i
        final.append([total, meters.index(j)])
    numeroFinal = max(final)
    
    print( f"The luger's fastest speed was {round(numeroFinal[0], 2)} m/s on segment {round(numeroFinal[1] + 1 , 2)}.")
get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128])