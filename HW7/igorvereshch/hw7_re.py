import re

def is_valid(password):
    pattern = r"(?=.*[$#@])(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=^.{6,16}$)"
    if re.search(pattern, password):
        return 'valid'
    return 'invalid'