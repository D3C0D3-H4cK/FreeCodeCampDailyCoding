import re
def rgb_to_hex(rgb):
    lista = re.findall(r'\d+', rgb)
    r = int(lista[0])
    g = int(lista [1])
    b = int(lista [2])
    return f"#{r:02x}{g:02x}{b:02x}"
    
rgb_to_hex("rgb(1, 2, 3)")