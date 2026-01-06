def speed_check(speed_mph, speed_limit_kph):
    km = speed_mph *  1.60934
    if km <= speed_limit_kph:
        return "Not Speeding"
    if km > speed_limit_kph and km - speed_limit_kph <= 5:
        return "Warning"
    return "Ticket"


speed_check(60, 70)