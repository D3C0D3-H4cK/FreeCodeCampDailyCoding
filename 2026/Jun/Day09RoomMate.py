def get_roommates(people):
    grupos = {}
    resultado = []
    for i in people: 
        if i["group"] in grupos:
            grupos[i['group']].append(i['name'])
        else:
            grupos[i['group']] = [i['name']]
    for i in grupos.values():
        for j in range(0, len(i), 2):
            grupito = i[j:j+2]
            if len(grupito) == 2:
                agrupar = " and ".join(grupito)
                resultado.append(agrupar)
            else:
                agrupar = " ".join(grupito)
                resultado.append(agrupar)
    print(resultado)
                
get_roommates([{ "name": "Adam", "group": "D" }, { "name": "Abraham", "group": "E" }, { "name": "Austin", "group": "E" }, { "name": "Augustus", "group": "D" }, { "name": "Angelica", "group": "D" }, { "name": "Aaron", "group": "E" }])