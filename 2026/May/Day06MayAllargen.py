def get_allergen_friendly_meals(meals, allergens):
    list = []
    for i in meals:
        Seguro = True
        for j in allergens:
            if j in i[1]:
                Seguro = False
        if Seguro:
            list.append(i[0])
    print(list)
        
get_allergen_friendly_meals([["steak", ["soy"]], ["fried rice", []], ["fish tacos", ["fish", "wheat"]], ["chicken parmesan", ["wheat", "milk"]]], ["soy", "fish"])