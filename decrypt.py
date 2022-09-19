
def decrypt(ciphertext: str, key: str):
    key_idx = 0
    plaintext = ""

    for c in ciphertext:
        if(c.isalpha()):
            if(c.isupper()):
                lower_bound = 65
            else:
                lower_bound = 97

            key_c = key[key_idx]
            offset = 65

            res = ord(c) - ord(key_c) + offset
            if(res < lower_bound):
                res = res + 26

            plaintext = plaintext + chr(res)
            key_idx = (key_idx + 1) % len(key)

        else:
            plaintext = plaintext + c   

    #print(plaintext)
    return plaintext

if __name__ == "__main__":
    ciphertext = input("Please provide your ciphertext\n")
    key = input("Please provide the cipher key\n")
    plain_text = decrypt(ciphertext, key)
    print(plain_text)