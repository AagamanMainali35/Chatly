from pwdlib import PasswordHash

_hasher = PasswordHash.recommended()

def hash_password(password: str):
    return _hasher.hash(password)
