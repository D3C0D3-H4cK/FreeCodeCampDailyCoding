def get_number_words(n):
    numeros = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
    }
    decenas = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
    }   
    if n == 0:
        print("zero")
    elif 1 <= n <= 19:
        print(f'{numeros[n]}')
    elif n % 10 == 0:
        print(f"{decenas[n]}")
    else:
        n = str(n)
        primerNumero = int(n[0]) * 10
        segundoNumero = int(n[1])
        print(f"{decenas[primerNumero]}-{numeros[segundoNumero]}")
        
get_number_words(21)