from hashlib import sha256
import secrets
import random

SECRET_KEY = 's3cr3t'

def password_generator(plaintext, app_name):
    salt = get_hexdigest(SECRET_KEY, app_name)
    var2 = get_hexdigest(salt, plaintext)
    return ''.join((salt, var2))


def get_hexdigest(salt, plaintext):
    return sha256((salt+plaintext).encode('utf-8')).hexdigest()


def password(plaintext, app_name, length):
    raw_hex_value = password_generator(plaintext, app_name)
    LETTERS = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '(,._-~*&%$!<>|\/?@)^+=')
    numbers = int(raw_hex_value, 16)
    characters = []

    while len(characters) < length:
        a = random.randint(0, len(LETTERS)-1)
        b = LETTERS[a]
        c = random.randint(0, len(b)-1)
        characters.append(b[c])

    return ''.join(characters)