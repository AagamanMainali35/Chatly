from fastapi.security import HTTPBearer
from pwdlib import PasswordHash

_hasher = PasswordHash.recommended()

def hash_password(password: str):
    return _hasher.hash(password)

def decode_password(new_password: str, old_password: str):
    return _hasher.verify(new_password, old_password)

scheme = HTTPBearer()

def validate_password(password: str) -> tuple[bool, str]:
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    return True, ""
