"""
Pounds to Kilograms

Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

    Replace "(lbs)" with the input number.
    Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
    1 pound equals 0.453592 kilograms.
    If the input is 1, use "pound" instead of "pounds".
    If the converted value is 1, use "kilogram" instead of "kilograms".
"""

def convert_to_kgs(lbs):

    Kilograms =  0.453592 
    operation = lbs * Kilograms
    formatted = f"{operation:.2f}"
    if lbs == 1:
        print(f"{lbs} pound equals {operation:.2f} kilograms.")
    else: 
        print(f"{lbs} pounds equals {formatted} kilogram{'s' if formatted != '1.00' else ''}.")
        
        

convert_to_kgs(2.20462)