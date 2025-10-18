import re
def strip_tags(html):

    patron = "<.*?>"
    nuevoTexto = re.sub(patron, "", html)
    print(nuevoTexto)
strip_tags('<a href="#">Click here</a>')