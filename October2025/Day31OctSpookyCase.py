"""
SpOoKy~CaSe

Given a string representing a variable name, convert it to "spooky case" using the following constraints:

    Replace all underscores (_), and hyphens (-) with a tilde (~).
    Capitalize the first letter of the string, and every other letter after that. Ignore the tilde character when counting. Make all other letters lowercase.

For example, given hello_world, return HeLlO~wOrLd.

"""

def spookify(boo):
    string = ""
    contador = 1
    for caracter in boo:
        if caracter.isalpha():
            if contador % 2 == 0:
                string += caracter.lower()
            else:
                string += caracter.upper()
            contador += 1
        else:
            string += '~'
    print(string)
            
            
spookify("TRICK-or-TREAT")