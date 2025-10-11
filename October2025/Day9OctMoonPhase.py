"""
Space Week Day 6: Moon Phase

For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

    "New": days 1 - 7
    "Waxing": days 8 - 14
    "Full": days 15 - 21
    "Waning": days 22 - 28

After day 28, the cycle repeats with day 1, a new moon.

    Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
    You will not be given any dates before the reference date.
    Return the correct phase as a string.
    
"""

import datetime

def moon_phase(date_string):
    fechaInicial = datetime.date(2000, 1, 6) 
    fechaString = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    diferencia = fechaString - fechaInicial 
    days = (diferencia.days + 1) % 28
    
        
    if days <= 7:
        return "New"
    if 8 <= days <= 14:
        return "Waxing"
    if 15 <= days <= 21:
        return "Full"
    if days >= 22:
        return "Waning"
moon_phase("2014-10-15")