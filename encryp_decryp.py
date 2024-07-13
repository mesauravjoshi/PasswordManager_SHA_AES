from getpass import getpass

# for encrypt_message decrypt_message
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_message(key, message):
    message = message.encode()
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted = cipher.encrypt(pad(message, AES.block_size))
    # print(f"encrpted from util.py : {encrypted}")
    return b64encode(cipher.iv + encrypted).decode()

def decrypt_message(key, encrypted_message):
    encrypted_bytes = b64decode(encrypted_message.encode())
    iv = encrypted_bytes[:16]
    encrypted_message = encrypted_bytes[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_message), AES.block_size)
    return decrypted.decode()
