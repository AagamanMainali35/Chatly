from pwdlib import PasswordHash

_hasher = PasswordHash.recommended()

def hash_password(password: str):
    return _hasher.hash(password)

def decode_password(new_password: str, old_password: str):
    return _hasher.verify(new_password, old_password)
