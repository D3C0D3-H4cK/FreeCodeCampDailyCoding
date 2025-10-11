"""
Hex to Decimal

Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.

Hexadecimal is a number system that uses 16 digits:

    0-9 represent values 0 through 9.
    A-F represent values 10 through 15.


    The string will only contain characters 0–9 and A–F.

"""

def hex_to_decimal(hex):
    hexList = "0123456789ABCDEF"
    list = []
    suma = []
    for i in reversed(hex):
        if i in hexList:
            valor = hexList.find(i)
            list.append(valor)
    for indices, val in enumerate(list):
        potencia = 16 ** indices
        operacion = val * potencia
        suma.append(operacion)
    print(sum(suma))
        
hex_to_decimal("FF")