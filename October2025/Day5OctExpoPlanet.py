def has_exoplanet(readings):
    cadena = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    calculo = []
    for i in readings:
        if i in cadena:
            calculo.append(cadena.index(i))
    suma = sum(calculo)
    operacion = suma / len(readings)
    operacion = operacion * 0.80
    print(operacion)
    for i in calculo:
        if i <= operacion:
            print("Verdadero")
    
    print("Falseto")
            
            

has_exoplanet("MONOPLONOMONPLNOMPNOMP")