def medication_reminder(medications, current_time):
    horasTomas = []
    horas = []
    Deployxitrin = [8,16]
    Debuggamanizole = [7,13,21]
    hora = current_time.split(":")
    horaMinutos = int(hora[0]) * 60 + int(hora[1])
    for i in medications:
        toma = i[1].split(":")
        horasTomas.append(int(toma[0]) * 60 + int(toma[1]))
    for i in Deployxitrin:
        minutosDeploy = i * 60
        if minutosDeploy > horaMinutos:
            horas.append( ["Deployxitrin", minutosDeploy - horaMinutos])
    for i in Debuggamanizole:
        minutosDebugg = i * 60
        if minutosDebugg > horaMinutos:
            horas.append(["Debuggamanizole", minutosDebugg - horaMinutos])

    lastTaken = horasTomas[2]
    UltimaToma = lastTaken + 240
    proximaToma = UltimaToma - horaMinutos
    horas.append(["Mergeflictamine", proximaToma])
    minimo = min(horas, key=lambda x: x[1])
    horaResultado = minimo[1] // 60
    minutosResutlado = minimo[1] % 60
    
    print(f"{minimo[0]} in {horaResultado}h {minutosResutlado}m ")

        

medication_reminder([["Deployxitrin", "08:00"], ["Debuggamanizole", "13:00"], ["Mergeflictamine", "14:00"]], "14:55")