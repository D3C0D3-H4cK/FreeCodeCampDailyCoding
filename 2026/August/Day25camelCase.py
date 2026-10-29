import re
def to_camel_case(s):
    contador = 0
    ultimo = ""
    palabras = re.split(r'[-_\s]+', s.lower())
    for i in palabras:
        if contador == 0:
            ultimo += i
            contador += 1
        else:
            ultimo += i.capitalize()
    print(ultimo)

to_camel_case("FREE cODE cAMP")