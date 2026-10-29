def is_valid_schema(obj):
    roles = ["user", "creator", "moderator", "staff", "admin"]
    if type(obj["username"]) != str:
        return False
    if type(obj["posts"]) != int:
        return False
    if type(obj["verified"]) != bool:
        return False
    if obj["role"] not in roles:
        return False
    if "supporter" in obj:
        if type(obj["supporter"]) != bool:
            return False
    if type(obj["badges"]) != list:
        return False
    if not all(type(item) == str for item in obj["badges"]):
        return False
    
    return True
is_valid_schema({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False, "badges": ["early-adopter", "popular"]})