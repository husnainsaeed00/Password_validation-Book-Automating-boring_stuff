import re

def check_password_strength(password):
    if (
        re.search(r".{8,}", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[A-Z]", password) and
        re.search(r"\d", password)
    ):
        return True
    else:
        return False
#password =input("input your password:")
check_password_strength("Husnainsaeed123")