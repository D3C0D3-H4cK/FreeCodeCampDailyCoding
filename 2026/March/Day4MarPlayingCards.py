def card_values(cards):
    value = []
    for i in cards: 
        if any(char.isdigit() for char in i):
            number = ""
            for char in i:
                if char.isdigit():
                    number += char
            value.append(int(number))
        else:
            if i[0] in ["J", "Q", "K"]:
                value.append(10)
            elif i[0] == "A":
                value.append(1)
    print(value)
            
                       
            

card_values(["AS", "10S", "10H", "6D", "7D"])