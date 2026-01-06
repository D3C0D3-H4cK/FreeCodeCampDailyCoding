def daylight_hours(latitude):
    hours = {

        -90:24,
        -75:23,
        -60:21,
        -45:15,
        -30:13,
        -15:12,
        0:12,
        15:11,
        30:10,
        45:9,
        60:6,
        75:2,
        90:0,
    }
    clave_cercana = min(hours.keys(), key=lambda k: abs(k - latitude))
    print(hours[clave_cercana])
daylight_hours(-10)