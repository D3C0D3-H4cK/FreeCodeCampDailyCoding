from itertools import permutations

def get_itinerary_count(stops):
    contador = 0
    elementos = ["breakfast", "lunch", "dinner"]
    for i in stops:
        elementos.append(i)
    for p in permutations(elementos):
        if p[0] == "breakfast":
            lunch_pos = p.index("lunch")
            dinner_pos = p.index("dinner")
            if lunch_pos >= 2:
                if dinner_pos - lunch_pos > 1:
                    if (len(p) - dinner_pos - 1) <=1 :
                        contador += 1
    print(contador)
get_itinerary_count(["library", "park", "arcade", "store", "cafe", "market", "museum"])