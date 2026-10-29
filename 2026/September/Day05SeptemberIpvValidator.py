
def is_valid_ipv4(ipv4):

    partes = ipv4.split('.')
    if len(partes) != 4:
        return False
    for i in partes:
        if not i.isdigit():
            return False
        if not (0 <= int(i) <= 255):
            return False
        if len(i) >= 2 and i[0] == '0' and i[1].isdigit():
            print('aca')
    return True


is_valid_ipv4("192.168.1.01")