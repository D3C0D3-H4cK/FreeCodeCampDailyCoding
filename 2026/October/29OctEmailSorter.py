#Volvimos a empezar con la racha 


def sort(emails):

    ordenamiento = sorted(emails, key=lambda x: (x.split("@")[1].lower(), x.split("@")[0].lower()))
    print(ordenamiento)
    
sort(["jill@mail.com", "john@example.com", "jane@example.com"])