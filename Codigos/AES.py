from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    # Padding to ensure the text is a multiple of 16 bytes
    padding_length = 16 - len(text) % 16
    padding = chr(padding_length) * padding_length
    return text + padding

def unpad(text):
    # Remove padding
    padding_length = ord(text[-1])
    return text[:-padding_length]

def aes_encrypt(plaintext, key):
    # Ensure the key is 16, 24, or 32 bytes long
    key = key.ljust(32)[:32]
    plaintext = pad(plaintext)
    iv = get_random_bytes(16)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return base64.b64encode(iv + ciphertext).decode('utf-8')

def aes_decrypt(ciphertext, key):
    # Ensure the key is 16, 24, or 32 bytes long
    key = key.ljust(32)[:32]
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:16]
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[16:]).decode('utf-8')
    return unpad(plaintext)

# Example usage
plaintext = "HELLO"
key = "mysecretkey"
ciphertext = aes_encrypt(plaintext, key)
print("Encrypted:", ciphertext)
decrypted_text = aes_decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
