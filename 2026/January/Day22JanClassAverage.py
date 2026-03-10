def get_average_grade(scores):
    dictionary = {
        range(97,100):"A+",
        range(93,96):"A",
        range(90,92):"A-",
        (87,89):"B+",
        (83,86):"B",
        (80,82):"B-",
        (77,79):"C+",
        (73,76):"C",
        (70,72):"C-",
        (67,69):"D+",
        (63,66):"D",
        (60,62):"D-",
    }
    suma = sum(scores)
    resultado = suma // len(scores)
    if resultado < 60:
        return "F"
    for rango, letra in dictionary.items():
        if rango[0] <= resultado <= rango[1]:
            print(letra)

get_average_grade([92, 91, 90, 94, 89, 93])