def get_number_of_plants(field_size, unit, crop):
    dictionaryCampo ={
        "acres":4046.86,
        "hectares":10000
    }
    dictionaryPlants = {
        "corn":1,
        "whet":0.1,
        "soybeans":0.5,
        "tomatoes":0.25,
        "lettuce":0.2
    }
    totalCampo = dictionaryCampo[unit] * field_size
    totalPlantas = totalCampo / dictionaryPlants[crop]
    print(int(totalPlantas))
    
get_number_of_plants(16.75, "acres", "tomatoes")