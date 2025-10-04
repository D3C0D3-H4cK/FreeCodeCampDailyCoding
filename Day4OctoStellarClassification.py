def classification(temp):
    classification ={
        (30000, float("inf")): "O",
        (10000, 29999): "B",
        (7500, 9999): "A",
        (6000, 7499): "F",
        (5200, 5999): "G",
        (3700, 5199): "K",
        (0, 3699): "M"
        
    }
    for(inicio, fin), categoria in classification.items():
        if inicio <= temp <= fin:
            print(categoria)
classification(110000)