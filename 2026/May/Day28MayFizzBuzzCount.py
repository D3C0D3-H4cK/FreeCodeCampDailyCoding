def fizz_buzz_count(start, end):
    fizz = 0
    buzz = 0
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizz += 1
            buzz += 1      
        elif i % 5 == 0:
            buzz += 1
        elif i % 3 == 0:
            fizz += 1
    return {
        "fizz": fizz,
        "buzz": buzz,
    }
    
fizz_buzz_count(-5432, 6789)