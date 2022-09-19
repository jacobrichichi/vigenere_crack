from decrypt import decrypt
from utils import format_cipher

def crack_with_key_length(cipher_text: str, key_length: int):
    expected_freq = { 'A': .082,
        'B': .015,	
        'C': .028,	
        'D': .043,
        'E': .13,		
        'F': .022,	
        'G': .02,		
        'H': .061,		
        'I': .07,	
        'J': .0015,	
        'K': .0077,	
        'L': .04,	
        'M': .024,	
        'N': .067,	
        'O': .075,	
        'P': 0.19,	
        'Q': .00095,		
        'R': .06,	
        'S': .063,	
        'T': .091,	
        'U': .028,	
        'V': .0098,		
        'W': .024,	
        'X': .0015,	
        'Y': .02,	
        'Z': .00074,	
    }
    key = ""
    best_chis = [0] * key_length

    # this goes thru each group of chars
    for i in range(0, key_length):
        idx = i
        currentGroup = ""
        # get the letters that all share the same cipher key char
        while(idx < len(cipher_text)):
            currentGroup = currentGroup + cipher_text[idx]
            idx += key_length

        chi_vals = {}

        # for each letter in the alphabet
        for letter in expected_freq:
            # shift the current group using the current letter
            plaintext = decrypt(currentGroup, letter)
            # get the resultant chi square of this shift, and record it
            chi_square_val = get_chi_square(plaintext, expected_freq)
            chi_vals[letter] = chi_square_val

        key = key + min(chi_vals, key=chi_vals.get).capitalize()
        min_char = min(chi_vals, key=chi_vals.get)
        best_chis[i] = chi_vals[min_char]

    best_chis_avg = sum(best_chis) / len(best_chis)

    return key
        

def get_chi_square(actual_text: str, expected_freq: dict): 
    sum = 0
    num_letters = len(actual_text)
    text_freq = {}

    for letter in expected_freq:
        text_freq[letter] = actual_text.count(letter) + actual_text.count(letter.lower())

    for letter, freq in expected_freq.items():
        sum += ((text_freq[letter] - freq * num_letters) ** 2) / (freq * num_letters)  

    return sum

if __name__ == "__main__":
    cipher_text = input("Please provide your ciphertext\n")
    key_length = int(input("Please provide your key length\n"))
    # cipher_text = "U CI MN UPRUSUDHQ MMP. JA, I MO JAT M ULAOW NEWE FJKEE IJK TAGPPQD QFCMR MNHMN BQA; ZOD CI U OZG KR YAWN TOXNUIOAF-IAVUG AOTARHMSYU. E MM M OWZ OR UQNSFCJOE, AH BXEEJ WZD NQJQ, FUDAD AZF HUQGKZE—AZF E YISJP QVQP XQ SMKZ FO BQOEEEU W YIZF. E MM UPRUSUDHQ, UZFADSFCJP, SUOLXY NGYMUEG LQOBNA DERWOQ TA UAQ MQ. NEWE FJA NOPKHQSE JAMDE AKG SQG OAMQVEYEE KJ OIDEQE SUFAEHAYO, UT UU WE TTQQSH U JWHE NGAZ SGTNAUZFAP BK OEDRATO AF TCNP, DUUPARFKJS GXCOE. WTGJ FHQA WBPDQWOH YG PTEK UAQ OZNU YY EWNDOGPZUNSU, PTEYUAXVQU, KD FUIIQNFU KR TTGED IYCCUNMVEAN—UPZQEP, GRQRKVDUNS CJP AZAPTIZI AJCQRP YE."
    formatted_cipher = format_cipher(cipher_text)
    
    key = crack_with_key_length(formatted_cipher, key_length)
   # key_two = crack_with_key_length(formatted_cipher, 10)

    plain_text = decrypt(cipher_text, key)
    # plain_text = decrypt(cipher_text, key_two)

    print(plain_text)
