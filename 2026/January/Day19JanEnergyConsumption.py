def compare_energy(calories_burned, watt_hours_used):

    joulesCalories = calories_burned * 4184
    joulesWatt = watt_hours_used * 3600
    
    if joulesCalories > joulesWatt:
        return "Workout"
    elif joulesCalories < joulesWatt:
        return "Devices"
    else:
        return "Equal"
compare_energy(250, 50)