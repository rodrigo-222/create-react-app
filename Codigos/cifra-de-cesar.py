def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    for i in range(len(texto)):
        char = texto[i]
        if char.isupper():
            resultado += chr((ord(char) + deslocamento - 65) % 26 + 65)
        else:
            resultado += chr((ord(char) + deslocamento - 97) % 26 + 97)
    return resultado

# Exemplo de uso
texto = "HELLO"
deslocamento = 6
print("Texto original: " + texto)
print("Texto criptografado: " + cifra_de_cesar(texto, deslocamento))