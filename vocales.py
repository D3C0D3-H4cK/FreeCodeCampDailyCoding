def repeat_vowels(s):
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    contador = {"a":0, "e":0, "i":0, "o":0, "u":0}
    palabra = ""
    primeravocal = True
    contador2 = 0
    for letra in s:
        if letra in vocales:
            contador[letra.lower()] += 1
            contador2 += 1
            if primeravocal:
                palabra += letra
                primeravocal = False
            else:
                if letra.lower() in contador:
                    contador[letra.lower()] += 1 
                    if contador[letra.lower()] >= 1:
                        palabra += letra + (letra.lower() * (contador2 - 1))
                
        else:
            palabra += letra
    print(palabra, contador, contador2)

 
            
    
            
repeat_vowels("helo word")