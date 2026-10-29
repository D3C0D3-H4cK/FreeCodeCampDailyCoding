def compress(s):
    words = s.split(" ")
    palabraCompleta = []
    indices = {}
    for i in words:
        if i in indices:
            palabraCompleta.append(indices[i] + 1)
        else:
            indices[i] = words.index(i)
            palabraCompleta.append(i)
    palabraReal = " ".join(map(str, palabraCompleta))
    print(palabraReal)
compress("lorem ipsum dolor sit per elit donec sit nostra libero per donec ligula sit gravida at elit vitae a elit sodales donec en donec at dolor nam ligula dignissim risus at ligula per nam ipsum ipsum gravida en elit per ipsum ligula en gravida per sodales sit at nam lorem sit per libero en ipsum elit sit sodales sit risus elit risus ipsum elit at gravida vitae en dignissim nam sit vitae sollicitudin per nostra per sit libero")