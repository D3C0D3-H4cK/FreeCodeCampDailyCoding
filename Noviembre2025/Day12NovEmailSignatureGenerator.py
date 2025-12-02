import re
def generate_signature(name, title, company):
    texto = ""
    if re.match(r'^[A-Ia-i]', name):
        texto = ">>" + name
    elif re.match(r'^[J-Rj-r]', name):
        texto = "--" + name
    else:
        texto = "::" + name
    textocompleto = texto + ", " + title + " at " + company
    print(textocompleto)
    
generate_signature("Iuinn Waverly", "Founder and CEO", "TechCo")