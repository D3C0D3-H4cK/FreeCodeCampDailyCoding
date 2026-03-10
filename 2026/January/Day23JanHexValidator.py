def is_valid_hex(s):
    hexa = "0123456789abcdef"
    if not (4 < len(s) < 8):
        return False
    if "#" not in s:
        return False
    s = s.replace("#", "")
    for i in s:
        if i.lower() not in hexa:
            return(False)
    return True

is_valid_hex("#123abc")