def format_cipher(ciphertext:str):
    formatted = ""

    for c in ciphertext:
        if(c.isalpha()): formatted += c.capitalize()

    return formatted  