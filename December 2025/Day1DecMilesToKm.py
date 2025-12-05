"""
Merry Chrismas 🎅

Miles to Kilometers

Given a distance in miles as a number, return the equivalent distance in kilometers.

    The input will always be a non-negative number.
    1 mile equals 1.60934 kilometers.
    Round the result to two decimal places.
    Remove unnecessary trailing zeros from the rounded result.
"""

def convert_to_km(miles):

    km = miles * 1.60934
    print(round(km, 2))

convert_to_km(1)