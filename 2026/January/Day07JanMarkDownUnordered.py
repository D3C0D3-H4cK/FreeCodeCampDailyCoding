def parse_unordered_list(markdown):
    textoComplete = ""
    texto = markdown.split('- ')
    texto = [palabra for palabra in texto if palabra]
    textoLimpio = [elemento.lstrip() for elemento in texto]
    for i in textoLimpio:
        textoComplete += f"<li>{i}</li>"
    textoComplete = textoComplete.replace('\n', '')
    
    print(textoComplete)

parse_unordered_list("- A-1\n- A-2\n- B-1")