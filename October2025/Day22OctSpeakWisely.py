import re
def wise_speak(sentence):
    palabras = ['have','must', 'are', 'will', 'can']
    oracion = re.findall(r'\w+|[^\w\s]', sentence)
    puntuacion = oracion[-1]
    oracion.remove(puntuacion)
    for i in oracion:
            if i in palabras:
                oracion1 = ' '.join(oracion[oracion.index(i) + 1:])
                oracion2 =  ' '.join(oracion[:oracion.index(i) + 1])
    oracionCompleta = oracion1 + ', '+ oracion2 + puntuacion
    return oracionCompleta.capitalize()
            
        
wise_speak("You must speak wisely.")