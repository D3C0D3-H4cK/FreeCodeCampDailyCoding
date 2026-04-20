import re
def largest_number(s):
    numeros = re.findall(r'-?\d+\.?\d*', s)
    numeros = [float(n) for n in numeros]
    mayor = max(numeros)
    
    if mayor.is_integer():
        return int(mayor)
    return(mayor)
largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011")