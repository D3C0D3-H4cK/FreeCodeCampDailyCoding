def to_binary(decimal):
    binario = []
    n = decimal
    while (n > 0):
        modulo = n % 2
        binario.append(modulo)
        n = n // 2
    listStr = [str(numero) for numero in reversed(binario)]
    resultado = "".join(listStr)
    print(resultado)
        
    
        
        
        
to_binary(50)