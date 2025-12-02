def calculate_age(birthday):
    actual = [2025,11,27]
    year = birthday.split("-")
    calculateYear = actual[0] - int(year[0]) 
    if (actual[1], actual[2]) < (int(year[1]), int(year[2])):
            calculateYear -= 1
            return calculateYear
    return calculateYear



calculate_age("2000-12-01")