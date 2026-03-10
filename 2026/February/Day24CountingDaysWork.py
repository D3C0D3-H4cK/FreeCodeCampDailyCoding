from datetime import date, timedelta

def count_business_days(start, end):
    contador = 0
    start = start.split("-")
    inicio = date(int(start[0]), int(start[1]), int(start[2]))
    final = end.split("-")
    fin = date(int(final[0]), int(final[1]), int(final[2]))
    delta = timedelta(days = 1)
    
    fecha_actual = inicio
    while fecha_actual <= fin:
        if fecha_actual.weekday() <= 4:
            contador += 1
        fecha_actual += delta
    print(contador)



count_business_days("2026-03-08", "2026-03-17")