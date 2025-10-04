def add_time(start, duration, day = "lunes"):
    
    def minutes_horas():
        iteraciones = 0
        Pm_Am = start.split()[-1] 
        separate, separated = start.split(":"), duration.split(":")
        hora, horad= int(separate[0]), int(separated[0])
        minutos, minutosd = separate[1], int(separated[1])
        minutos = int(minutos.split()[0])
        formathour = hora + 12 
        if Pm_Am == "PM":
            formathour = hora + 12 + horad
        if Pm_Am == "AM":
            formathour = hora + horad
        while formathour > 24 and minutostotales < 60:
            formathour = formathour - 24
            iteraciones += 1
            print(formathour)
        if formathour > 12:
            print("tarde, noche")
            formathour = formathour - 12
            Pm_Am = "PM"
        elif formathour < 12:
            print("mañana, dia")
            Pm_Am = "AM"

        print(hora, minutos, Pm_Am, horad, minutosd, formathour, minutostotales, Pm_Am, iteraciones, minutos_completos)
        return hora, minutos, Pm_Am
    
    minutes_horas()
add_time("9:43 PM", "123:10")