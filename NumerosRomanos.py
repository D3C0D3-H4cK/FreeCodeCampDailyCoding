def parse_roman_numeral(numeral):
    contador = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    total = 0
    actual = None
    previo = 0
    for i in reversed(numeral):
        actual = contador[i]
        if i in (contador):
            if actual is not None:
                    if actual < previo:
                        total -= actual
                        
                    if actual >= previo:
                        total += actual
            previo = actual
    return total
            
            
            
        
parse_roman_numeral("DIV")
#10, 100,1, 10 = 99