def is_valid_ipv4(ipv4):
    ipv4part = ipv4.split(".")
    verdadero = ""
    if len(ipv4part) == 4:
        for partes in ipv4part:
            if len(partes) == 1 and 0 <= int(partes) <= 255:
                 verdadero = "verdadero"
            elif len(partes) > 1 and partes.startswith("0"):
                verdadero = "falso"
                break
            elif len(partes) > 1 and 0 <= int(partes) <= 255:
                verdadero = "verdadero"
            else: 
                verdadero = "falso" 
                break 
        if verdadero == "verdadero":
            return True
        else:
            return False    
    else:
        verdadero = "falso"
#is_valid_ipv4("255.01.50.111")
#is_valid_ipv4("192.168.1.1")
#is_valid_ipv4("0.0.0.0")
#is_valid_ipv4("192.168.101.")
