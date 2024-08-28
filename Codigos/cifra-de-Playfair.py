def generate_key_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    used_chars = set()

    for char in key:
        if char not in used_chars and char.isalpha():
            matrix.append(char)
            used_chars.add(char)

    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def prepare_text(text):
    text = text.upper().replace('J', 'I')
    prepared_text = ""
    i = 0

    while i < len(text):
        prepared_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared_text += 'X'
        elif i + 1 < len(text):
            prepared_text += text[i + 1]
            i += 1
        else:
            prepared_text += 'X'
        i += 1

    return prepared_text

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    plaintext = prepare_text(plaintext)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        row1, col1 = find_position(matrix, plaintext[i])
        row2, col2 = find_position(matrix, plaintext[i + 1])

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_key_matrix(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        row1, col1 = find_position(matrix, ciphertext[i])
        row2, col2 = find_position(matrix, ciphertext[i + 1])

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    # Remove filler 'X' characters used during encryption
    cleaned_plaintext = ""
    i = 0
    while i < len(plaintext):
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1] and plaintext[i + 1] == 'X':
            cleaned_plaintext += plaintext[i]
            i += 2
        else:
            cleaned_plaintext += plaintext[i]
            i += 1

    # Remove trailing 'X' if it was added as a filler
        if cleaned_plaintext[-1] == 'X':
            cleaned_plaintext = cleaned_plaintext[:-1]

    return cleaned_plaintext

# Example usage
plaintext = "HELLO"
key = "la"
ciphertext = playfair_encrypt(plaintext, key)
print("Encrypted:", ciphertext)
decrypted_text = playfair_decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)