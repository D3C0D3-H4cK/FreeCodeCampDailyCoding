"""
Credit Card Masker

Given a string of credit card numbers, return a masked version of it using the following constraints:

    The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
    Replace all numbers, except the last four, with an asterisk (*).
    Leave the remaining characters unchanged.

For example, given "4012-8888-8888-1881" return "****-****-****-1881".

"""

def mask(card):
    numbers = "1234567890"
    cardMasker = ""
    for digits in card:
        if digits in numbers:
            if len(cardMasker) < 15:
                cardMasker += "*"
            else:
                cardMasker += digits
        else:
            cardMasker+= digits
        
    print(cardMasker)
mask("4012 8888 8888 1881")