def lcm(a, b):
    mayor = max(a, b)
    while True:
        if mayor % a == 0 and mayor % b == 0:
            return mayor
 
        mayor +=1
          

lcm(4, 6)