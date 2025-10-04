def adjust_thermostat(temp, target):
    if temp > target:
        print("cood")
    elif temp < target:
        print("heat")
    else:
        print("hold")
    return temp
adjust_thermostat(72, 72)
#it so easy 