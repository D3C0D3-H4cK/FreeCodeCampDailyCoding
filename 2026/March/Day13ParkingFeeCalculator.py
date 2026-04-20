import math
def calculate_parking_fee(park_time, pickup_time):
    estado = False
    park_time = park_time.split(":")
    entradaMinutes = int(park_time[0])*60 + int(park_time[1])
    pickup_time = pickup_time.split(":")
    salidaMinutes = int(pickup_time[0])*60 + int(pickup_time[1])
    if salidaMinutes < entradaMinutes:
        salidaMinutes += 1440
        estado = True
    tiempoTotal = salidaMinutes - entradaMinutes
    horas = math.ceil(tiempoTotal / 60)
    precio = horas * 3
    if estado:
        precio += 10
    if precio < 5:
        precio = 5
    return f'${precio}'

calculate_parking_fee("09:00", "11:00")