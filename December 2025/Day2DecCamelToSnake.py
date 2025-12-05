"""
Camel to Snake

Given a string in camel case, return the snake case version of the string using the following rules:

    The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
    Every uppercase letter in the camel case string starts a new word.
    Convert all letters to lowercase.
    Separate words with an underscore (_).

"""

def to_snake(camel):
    resultado = ""
    for letra in camel:
        if letra.isupper():
            resultado += "_" + letra.lower()
        else:
            resultado += letra
    return resultado
to_snake("helloWorld")