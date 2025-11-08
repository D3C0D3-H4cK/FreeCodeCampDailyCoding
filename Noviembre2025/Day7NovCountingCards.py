def combinations(cards):
    cartas = []
    division = []
    j = 52
    for i in range(cards):
        division.append(i + 1)
        cartas.append(j)
        j -= 1

    numerador = 1
    for x in cartas:
        numerador *= x

    denominador = 1
    for y in division:
        denominador *= y
    resultado = numerador // denominador
    return resultado
combinations(52)