"""
Given a date in the format "Month day, year", return the date in the format "YYYY-MM-DD".

    The given month will be the full English month name. For example: "January", "February", etc.
    In the return value, pad the month and day with leading zeros if necessary to ensure two digits.

For example, given "December 6, 2025", return "2025-12-06".

"""


def format_date(date_string):
    fechas = {
        "January":"01",
        "February":"02",
        "March":"03",
        "April":"04",
        "May":"05",
        "June":"06",
        "July":"07",
        "August":"08",
        "September":"09",
        "October":"10",
        "November":"11",
        "December":"12",

    }
    date = date_string.split(" ")
    month = fechas[date[0]]
    day = date[1].replace(",", "").zfill(2)
    year = date[2]
    
    print(f"{year}-{month}-{day}")

format_date("September 7, 512")