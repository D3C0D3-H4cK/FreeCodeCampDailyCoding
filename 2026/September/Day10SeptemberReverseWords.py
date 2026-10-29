#reverse word

def reverse_sentence(sentence):
    lista = []
    texto = sentence.split()
    for i in reversed(texto):
        
        lista.append(i)
    textoFinal = " ".join(lista)
    print(textoFinal)

reverse_sentence("world hello")