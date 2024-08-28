def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(plaintext, key):
    key = generate_key(plaintext, key)
    ciphertext = []
    for i in range(len(plaintext)):
        x = (ord(plaintext[i]) + ord(key[i])) % 26
        x += ord('A')
        ciphertext.append(chr(x))
    return "".join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    key = generate_key(ciphertext, key)
    plaintext = []
    for i in range(len(ciphertext)):
        x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        plaintext.append(chr(x))
    return "".join(plaintext)

# Example usage
plaintext = "HELLO"
key = "KEY"
ciphertext = vigenere_encrypt(plaintext, key)
print("Encrypted:", ciphertext)
decrypted_text = vigenere_decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
