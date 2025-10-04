def reverse_sentence(sentence):
    palabraReves=[]

    palabra = sentence.split()
    for i in reversed(palabra):
        palabraReves.append(i)
    convertirString = map(str, palabraReves)
    ultimaCadena = " ".join(convertirString)
    print(ultimaCadena)
reverse_sentence("push commit git")