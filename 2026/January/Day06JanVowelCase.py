def vowel_case(s):
    texto = ""
    vowel = "aeiou"
    for i in s.lower():
        if  i in vowel:
            texto += i.upper()
        else:
            texto += i
    print(texto)
vowel_case("vowelcase")