def get_weekday(date_string):
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
    if  2200 <= int(fecha[0]) <= 2299:
         suma = meses + int(fecha[2]) + 2 + int(year[-2:]) + divicionYear #Si es mayor a los 2000
    elif 2100 <= int(fecha[0]) <= 2199:
        suma = meses + int(fecha[2]) + 4 + int(year[-2:]) + divicionYear #Si es mayor a los 2000
    elif 2000 <= int(fecha[0]) <= 2099:
        suma = meses + int(fecha[2]) + 6 + int(year[-2:]) + divicionYear #Si es mayor a los 2000

    else:
         suma = meses + int(fecha[2]) + int(year[-2:]) + divicionYear #Si es mayor a los 2000
    total = suma % 7
    
    print(day[total])
get_weekday("2345-10-01")