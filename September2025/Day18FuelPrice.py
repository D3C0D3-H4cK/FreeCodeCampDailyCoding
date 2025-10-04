def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    rest = tank_size - fuel_level
    price = price_per_gallon * rest
    priceFinal = "$" + str(price)
    if len(priceFinal) < 6:
        priceFinal2 = priceFinal + "0"
        print(priceFinal2)
    else:
        print(priceFinal)
cost_to_fill(18, 9, 3.25)