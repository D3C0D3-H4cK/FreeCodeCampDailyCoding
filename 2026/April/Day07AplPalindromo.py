"""
Palindrome Characters

Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

    A palindrome is a string that is the same forward and backward.
    If it's not a palindrome, return "none".


"""

def palindrome_locator(s):
    n = len(s)
    mid = n // 2
    string = ""
    for i in reversed(s):
        string += i
    if string == s:
        if n % 2 == 0:  # par
            return s[mid-1:mid+1]
        else:  # impar
            return s[mid]
    else:
        return "none"
        


palindrome_locator("racecsar")