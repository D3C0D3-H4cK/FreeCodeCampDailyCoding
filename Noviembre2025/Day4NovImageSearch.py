def image_search(images, term):
    list = []
    for i in images:
        if term.lower() in i.lower():
            list.append(i)
    print(list)
image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun")