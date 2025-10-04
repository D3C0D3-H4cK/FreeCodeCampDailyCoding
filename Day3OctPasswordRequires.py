def check_strength(password):
    rules = 0
    if len(password) >= 8: 
        rules += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        rules +=1
    if any(c.isdigit() for c in password):
        rules +=1
    if any(c in "!@#$%^&*" for c in password):
        rules += 1
    if rules == 4:
        print("strong")
    if rules == 3 or rules == 2:
        print("medium")
    else:
        print("weak")
check_strength("123456")