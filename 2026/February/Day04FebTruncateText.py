def truncate_text(text):
    texto2 = ""
    if len(text) >= 21:
        for i in text:
            texto2 += i
            if len(texto2) == 17:
                texto2 += "..."
                break
        print(texto2)
    else:
        print(text)
    
    
truncate_text("Exactly twenty chars")