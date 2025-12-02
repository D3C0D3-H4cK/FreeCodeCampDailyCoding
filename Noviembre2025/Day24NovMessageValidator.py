def is_valid_message(message, validation):
    palabras = message.split()
    estado = True
    if len(palabras) == len(validation):
        for i,j in zip(palabras,validation):
                if i[0].lower() != j.lower():
                    estado = False
    else:
        estado = False                
    print(estado)


is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD")