def string_sum(s):
    suma = []
    numero = ''
    for i in range(len(s)):
        caracter = s[i]
        if i + 1 < len(s):
            siguiente = s[i + 1]
        else:
            siguiente = ''
        if caracter.isdigit():
            numero += caracter
            if not siguiente.isdigit():
                suma.append(int(numero))
                numero = ''
    print(sum(suma))
  
            
            
            
            
string_sum("125344")