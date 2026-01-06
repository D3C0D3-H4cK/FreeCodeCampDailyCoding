def update_inventory(inventory, shipment):
    totalProducts = []
    products = []
    for i in inventory:
        totalProducts.append(i)
    for l in shipment:
        totalProducts.append(l)
    for i in totalProducts:
        pass
    
update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]])