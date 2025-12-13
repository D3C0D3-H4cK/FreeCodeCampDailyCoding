"""
String Compression

Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

    Only consecutive duplicates are compressed.
    Words are separated by single spaces.

For example, given "yes yes yes please", return "yes(3) please".

"""

def compress_string(sentence):
    string = []
    oracion = sentence.split(' ')

    for i in oracion:
        contar = oracion.count(i)
        if contar > 1:
            palabra = f"{i}({oracion.count(i)})"
            if palabra not in string:
                string.append(palabra)
        else:
            string.append(i)
    string = " ".join(string)        
    print(string)
      

compress_string("one one three and to the the the the")