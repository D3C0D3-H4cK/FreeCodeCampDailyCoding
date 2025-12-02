def longest_word(sentence):
    palabra = ""
    for i in sentence:
        if i.isalpha():
            palabra += i
        if i == " ":
            palabra += i
    words = palabra.split(" ")
    print(words)
    palabraLarga =  words[0]
    for i in words:
        if len(i) > len(palabraLarga):
            palabraLarga = i
    print(palabraLarga)
longest_word("Wouldn't you like to know.")