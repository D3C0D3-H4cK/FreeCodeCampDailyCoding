def get_longest_word(sentence):
    Palabras = sentence.split()
    nuevaLista = []
    for i in Palabras:
        ignore = i.replace(".", "")
        nuevaLista.append(ignore)
    palabraLarga = max(nuevaLista, key=len)
    print(palabraLarga)
        
        
get_longest_word("Coding challenges are fun and educational.")