from datetime import datetime, timezone
def odd_or_even_day(timestamp):
    milisegundos = timestamp
    fecha = datetime.fromtimestamp(milisegundos / 1000.0, tz=timezone.utc)
    if fecha.day % 2 == 0:
        print('even')
    else:
        print('odd')
odd_or_even_day(1769472000000)