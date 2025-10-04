def to_decimal(binary):
    suma = []
    for indice,i in enumerate(reversed(str(binary))):
        operacion = 2**indice
        resultado = int(i) * int(operacion)
        suma.append(int(resultado))
    print(sum(suma))

to_decimal(1011)