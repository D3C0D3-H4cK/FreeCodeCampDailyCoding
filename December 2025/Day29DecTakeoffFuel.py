def fuel_to_add(current_gallons, required_liters):

    liters = current_gallons * 3.78541
    if liters < required_liters:
        faltante = required_liters - liters 
        gallons = faltante / 3.78541
        if gallons % 1 == 0:
            print(int(gallons), + 'XD')
        else:
            gallons = gallons + 1
            print(int(gallons), "LS")
    else:
        print(0)
fuel_to_add(10, 30)