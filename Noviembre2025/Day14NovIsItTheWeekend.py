def days_until_weekend(date_string):
    months = {
        "01":0,
        "02":3,
        "03":3,
        "04":6,
        "05":1,
        "06":4,
        "07":6,
        "08":2,
        "09":5,
        "10":0,
        "11":3,
        "12":5,
    }
    day = {
        0:"Sunday",
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday"
    }
    
    fecha = date_string.split("-")
    meses = months[fecha[1]]
    year = fecha[0]
    divicionYear = int(year[-2:]) // 4
    suma = meses + int(fecha[2]) + 6 + int(year[-2:]) + divicionYear #Si es mayor a los 2000
    total = suma % 7
    if total == 0 or total == 6:
        print("It's the weekend!")
    else:
        diasFaltantes = 6 - total
        if diasFaltantes <= 1:
            print(diasFaltantes, "day until the weekend.")
        else:
            print (diasFaltantes, "days until the weekend.")
days_until_weekend("2025-01-01")