"""
Email Validator

Given a string, determine if it is a valid email address using the following constraints:

    It must contain exactly one @ symbol.
    The local part (before the @):
        Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
        Cannot start or end with a dot.
    The domain part (after the @):
        Must contain at least one dot.
        Must end with a dot followed by at least two letters.
    Neither the local or domain part can have two dots in a row.

"""

def validate(email):
    textoSeparado = email.split('@')
    empieza = textoSeparado[0].startswith(".")
    termina = textoSeparado[0].endswith(".")
    if len(textoSeparado) == 2:
        if termina or empieza == True:
            print(False)
        if "." in textoSeparado[1]:
            dominio = textoSeparado[1].split('.')
            if '..' in textoSeparado[1]:
                return False
            if len(dominio[-1]) >= 2:
                contador = 0
                for caracter in dominio[-1]:
                    if caracter.isalpha():
                        contador += 1
                if contador >= 2:
                    print(True)
                else:
                    print(False)
                        
            
validate("hell.-w.rld@example.c..om")