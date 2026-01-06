"""Consonant Count

Given a string and a target number, determine whether the string contains exactly the target number of consonants.

    Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
    Ignore digits, punctuation, spaces, and other non-letter characters when counting.

"""
def has_consonant_count(text, target):
    vocals = "aeiou"
    count = 0
    for i in text.lower():
        if i not in vocals:
            if i.isalpha():
                count += 1
    if count == target:
        return True
    else: 
        return False
            
has_consonant_count("freeCodeCamp Rocks!", 11)