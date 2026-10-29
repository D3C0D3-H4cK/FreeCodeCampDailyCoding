def get_oldest(people):
    Mayores = []
    max_age = max(people, key=lambda person: person['age'])
    mayorEdad = max_age['age']
    for i in people:
        if i['age'] == mayorEdad:
            Mayores.append(i['name'])
    print(Mayores)
            
    
get_oldest([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }])