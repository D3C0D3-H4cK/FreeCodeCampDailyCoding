import re
def generate_slug(str):
    especialCharacters = r'[^a-zA-Z0-9\s]'
    re.search(especialCharacters, str)
    nueva_cadena = re.sub(especialCharacters, '', str)
    nueva_cadena = nueva_cadena.strip()
    
    if " " in nueva_cadena:
        if nueva_cadena.count(" ") >= 1:
            espacios = r'\s+'
            cadena_final = re.sub(espacios, '%20', nueva_cadena).lower()
            
            print(cadena_final)
    print(nueva_cadena.lower())
        
generate_slug(" hello-world ")