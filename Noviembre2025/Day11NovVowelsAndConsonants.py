"""
Vowels and Consonants

Given a string, return an array with the number of vowels and number of consonants in the string.

    Vowels consist of a, e, i, o, u in any case.
    Consonants consist of all other letters in any case.
    Ignore any non-letter characters.

For example, given "Hello World", return [3, 7].
"""

def count(s):
    contadorVowels = 0
    contadorConsonants = 0
    list = []
    vowels = "aeiou"
    for i in s:
        if i.isalpha():
            if i in vowels:
                contadorVowels += 1
            else:
                contadorConsonants +=1   
    list.append(contadorVowels)
    list.append(contadorConsonants)
    print(list)
count("The quick brown fox jumps over the lazy dog.")