
def main():
    plaintext = input("Please provide your plaintext\n")
    cipher = input("Please provide the cipher\n")
    cipher_idx = 0
    cipher_text = ""

    for c in plaintext:
        if(c.isalpha()):
            if(c.isupper()):
                upper_bound = 90
            else:
                upper_bound = 122

            cipher_c = cipher[cipher_idx]
            offset = 65

            res = ord(c) + ord(cipher_c) - offset
            if(res > upper_bound):
                res = res - 26

            cipher_text = cipher_text + chr(res)
            cipher_idx = (cipher_idx + 1) % len(cipher)

        else:
            cipher_text = cipher_text + c   

    print(cipher_text)


if __name__ == "__main__":
    main()