def all_unique(s):

    vistos = set()
    for i in s:
        if i in vistos:
            return False
        vistos.add(i)
    
    return False


all_unique("~!@#$%^&*()_+")