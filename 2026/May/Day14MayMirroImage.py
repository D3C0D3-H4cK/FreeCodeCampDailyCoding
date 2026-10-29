def is_mirror_image(s1, s2):
    cadena = ""
    espejos = {
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
    "b": "d",
    "d": "b",
    "p": "q",
    "q": "p",
    "(": ")",
    ")": "("
}
    for i in reversed(s1):
        cadena += espejos.get(i, i)
    if cadena == s2:
        print("True")
is_mirror_image("WTYUIOHAXVMwoxv08=+:|-_*^!.[]{}<>bdpq()", "()pqbd<>{}[].!^*_-|:+=80vxowMVXAHOIUYTW")