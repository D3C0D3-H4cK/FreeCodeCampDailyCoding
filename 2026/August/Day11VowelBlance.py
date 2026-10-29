def is_balanced(s):
    mitad = len(s) // 2
    part1 = s[:mitad]
    vowels = "aeiou"
    contador1 = 0
    contador2 = 0
    if len(s) % 2 == 0:
        part2 = s[mitad:]
    else: 
        part2 = s[mitad +1:]
    for i in part1.lower():
        if i in vowels:
            contador1 += 1
    for i in part2.lower():
        if i in vowels: 
            contador2 += 1
    print(part1, part2)

is_balanced('Lorem Ipsum')