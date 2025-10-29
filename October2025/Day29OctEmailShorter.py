"""
Email Sorter

On October 29, 1971, the first email ever was sent, introducing the username@domain format we still use. Now, there are billions of email addresses.

In this challenge, you are given a list of email addresses and need to sort them alphabetically by domain name first (the part after the @), and username second (the part before the @).

    Sorting should be case-insensitive.
    If more than one email has the same domain, sort them by their username.
    Return an array of the sorted addresses.
    Returned addresses should retain their original case.

For example, given ["jill@mail.com", "john@example.com", "jane@example.com"], return ["jane@example.com", "john@example.com", "jill@mail.com"].

"""

def sort(emails):
    listaOrdenada = sorted(emails, key=str.lower)
    Dominio = sorted(listaOrdenada, key=lambda x: x.split('@')[1].lower(), )
    print(Dominio)
    
sort(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"])