import re
def parse_link(markdown):
    patron2 = r'\[(.*?)\]'
    patron1 = r'\((.*?)\)'
    texto1 = re.findall(patron1, markdown)
    texto2 = re.findall(patron2, markdown)
    Ahref = f'<a href="{" ".join(texto1)}">{" ".join(texto2)}</a>'
    print(Ahref)
parse_link("[freeCodeCamp](https://freecodecamp.org/)")