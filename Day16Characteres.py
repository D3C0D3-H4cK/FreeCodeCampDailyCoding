def capitalize(paragraph):
    list_paragraph = paragraph.split(" ")
    if len(list_paragraph) == 1:
        print("es solo una cadena xdxdxd")
    for i in range(len(list_paragraph) - 1):
        palabra = list_paragraph[i]
        if palabra.endswith(".") or palabra.endswith("!") or palabra.endswith("?"):
            list_paragraph[i + 1] = list_paragraph[i + 1].capitalize()
    string = (" ").join(list_paragraph)
    stringFinal = string[0].upper() + string[1:]
    print(stringFinal)


capitalize("crazy!!!strange???unconventional...sentences.")