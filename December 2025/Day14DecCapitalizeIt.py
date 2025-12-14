"""
Capitalize It

Given a string title, return a new string formatted in title case using the following rules:

    Capitalize the first letter of each word.
    Make all other letters in each word lowercase.
    Words are always separated by a single space.

"""
def title_case(title):
    texto = []
    palabras = title.split(' ')
    for i in palabras:
        texto.append(i.capitalize())
    texto = ' '.join(texto)
    print(texto)
        
        
        
title_case("JAVASCRIPT AND PYTHON")