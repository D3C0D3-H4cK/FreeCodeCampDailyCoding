"""
Character Limit

In this challenge, you are given a string and need to determine if it fits in a social media post. Return the following strings based on the rules given:

    "short post" if it fits within a 40-character limit.
    "long post" if it's greater than 40 characters and fits within an 80-character limit.
    "invalid post" if it's too long to fit within either limit.
"""

def can_post(message):
    contador = 0
    for i in message:
        contador += 1
    if contador < 40:
        return "short post"
    elif 40 < contador < 80:
        return "long post"
    else:
        return "invalid post"
can_post("Hello world")