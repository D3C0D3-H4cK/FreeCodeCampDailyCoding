"""SCREAMING_SNAKE_CASE

Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

The given variable names will be written in one of the following formats:

    camelCase
    PascalCase
    snake_case
    kebab-case

In the above formats, words are separated by an underscore (_), a hyphen (-), or a new word starts with a capital letter.

To convert to SCREAMING_SNAKE_CASE:

    Make all letters uppercase
    Separate words with an underscore (_)
"""
def to_screaming_snake_case(variable_name):
    anterior = ""
    resultado = ""
    for i in variable_name:
        if i.isupper() and anterior.islower():
            resultado += "_"
        if not i.isalpha(): 
            resultado += "_"
        else:
            resultado += i.upper()
        anterior = i
    print(resultado)
        
to_screaming_snake_case("User-Email")