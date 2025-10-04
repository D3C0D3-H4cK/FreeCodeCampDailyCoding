def add_time(start, duration, day = ""):
    
    def minutes_horas():
        Pm_Am = start.split()[-1] 
        separate, separated = start.split(":"), duration.split(":")
        hora, horad= int(separate[0]), int(separated[0])
        minutos, minutosd = separate[1], int(separated[1])
        minutos = int(minutos.split()[0])
        if Pm_Am == "PM":
            hora_total = hora + 12 + horad
            minutos_totales = hora_total * 60 + minutos + minutosd
            dias_totales = minutos_totales // 1440
            minutos_restantes = minutos_totales % 1440
            tarde_dia = minutos_restantes // 720
            hora_final = minutos_restantes // 60
            minutos_final = minutos_restantes % 60
        elif Pm_Am == "AM":
            hora_total = hora + horad
            minutos_totales = hora_total * 60 + minutos + minutosd
            dias_totales = minutos_totales // 1440
            minutos_restantes = minutos_totales % 1440
            tarde_dia = minutos_restantes // 720
            hora_final = minutos_restantes // 60
            minutos_final = minutos_restantes % 60
            minutos_final = str(minutos_final).zfill(2)
        if hora_final == 0:
            hora_final = 12
        if hora_final > 12:
            hora_final -= 12
        if tarde_dia == 1:
            Pm_Am = "PM"
        elif tarde_dia == 0:
            Pm_Am = "AM"
        hora_total_final = f"{hora_final}:{str(minutos_final).zfill(2)} {Pm_Am}"
        return hora_total_final, dias_totales
    def days(day):
        if not day: # Manejar cadenas vacías
            return ""
        return day[0].upper() + day[1:].lower()
    day = days(day)
    hora_total_final, dias_totales = minutes_horas()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day in week:
        index = week.index(day)
        dia_total = index + dias_totales
        if dia_total > 6:
            dia_total = dia_total % 7
        dia_final = week[dia_total]
    if day:
        if dias_totales == 0:
            new_time = f"{hora_total_final}, {dia_final}"
            print(new_time)
        elif dias_totales == 1:
            new_time = f"{hora_total_final}, {dia_final} (next day)"
            print(new_time)
        elif dias_totales > 1:
            new_time = f"{hora_total_final}, {dia_final} ({dias_totales} days later)"
            print(new_time)
    else:   # si NO pasaron un día
        if dias_totales == 0:
            new_time = f"{hora_total_final}"
            print(new_time)
        elif dias_totales == 1:
            new_time = f"{hora_total_final} (next day)"
            print(new_time)
        else:
            new_time = f"{hora_total_final} ({dias_totales} days later)"
            print(new_time)
add_time('11:59 PM', '24:05', 'Wednesday') #Esta fue mi solucion Pero no es nada optima, estudiar caso 