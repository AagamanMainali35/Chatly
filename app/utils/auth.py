from fastapi.security import HTTPBearer
from pwdlib import PasswordHash

_hasher = PasswordHash.recommended()

def hash_password(password: str):
    return _hasher.hash(password)

def decode_password(new_password: str, old_password: str):
    return _hasher.verify(new_password, old_password)

scheme = HTTPBearer()
import re

def validate_password(password: str) -> tuple[bool, str]:
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit"
    return True, ""
