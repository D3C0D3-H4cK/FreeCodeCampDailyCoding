def count_perfect_cubes(a, b):
    contador = 0
    if a > b:
        mayor = a
        menor = b
    else:
        mayor = b
        menor = a
    
    for i in range(menor,mayor + 1):
        raiz_cubica = round(abs(i)**(1/3))
        if (raiz_cubica**3 == abs(i)) == True:
            contador += 1
    print(contador)

count_perfect_cubes(3, 30)