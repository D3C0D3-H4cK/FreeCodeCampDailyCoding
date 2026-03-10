def separate_letters_and_numbers(s):
    texto = ""
    anterior = s[0]
    for i in s:
        if (i.isdigit() and anterior.isalpha()) or (i.isalpha() and anterior.isdigit()):
            texto += f'-{i}'
        else:
            texto += i
        anterior = i
    print(texto)

separate_letters_and_numbers("H3LL0W0RLD")