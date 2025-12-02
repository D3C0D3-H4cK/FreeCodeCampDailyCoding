def scale_recipe(ingredients, scale):
    listFinal = []
    for i in ingredients:
        i = i.split()
        result = float(i[0]) * scale
        if result == int(result):
            finalText = f"{int(result)} {" ".join(i[1:])}"
        else:
            finalText = f"{result } {" ".join(i[1:])}"
        listFinal.append(finalText)
    print(listFinal)
scale_recipe(["2 C Flour", "1.5 T Sugar"], 2)