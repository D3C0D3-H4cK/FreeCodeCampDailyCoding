def find_org(acronym):
    words = ["National Avocado Storage Authority","Cats Infiltration Agency","Fluffy Beanbag Inspectors","Department Of Jelly","Wild Honey Organization","Eating Pancakes Administration"]
    for i in words:
        palabra = ""
        organizations = i.split(" ")
        for j in organizations:
            palabra += j[0]
        if palabra == acronym:
            print(i)
find_org("CIA")