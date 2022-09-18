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
    # ciphertext = input("Please provide your ciphertext\n")
    # key_length = int(input("Please provide your key length\n"))
    cipher_text = "NB TIM YPB JYXB LN NNUBA, CY EXA NMM TWLXB LN NNUBA, CY EXA NMM XOY TN TQMIWJ, QN BIP BBJ IDM IK NLWFNAEVYXA, FB QFA QPY JXLKB TN YMFNMC, QN BIP BBJ MMWWM WC QHHZBLOQQQG, CY EXA NMM PMUXWK WZ QQDPN, NB TIM YPB AYFALV IK LXZESMPA, CY EXA NMM PXLNVD WZ MWMM, CY EXA NMM TQHYMO WZ IMPXUNZ, TM BFL BDYWGQPCSO YMZTZB CM, BM EIX SWQPCSO YMZTZB CM, BM TMLJ IIT ATQKO XNZBKN YW EMUAMK, EY BMOM UQT DWCSO AQLJKQ BBJ WQPYW EXG — CS AEWLY, BEM JJZFWX BIP AI KIO TCPM QPY UZBAYSB MMLNWA, BBFB PWGJ WC QNX VLQMNMPB UZBEWLNBFMM NVPQMYMA WH NBP JYNVD ZYHMFDYI, NLZ ATWA WL KWO MPNT, FV NMM PCJJZIINNDB LYLZBM IK KLUJFZFAIS WKTS."
    formatted_cipher = format_cipher(cipher_text)
    
    key = crack_with_key_length(formatted_cipher, 5)

    plain_text = decrypt(cipher_text, key)

    print(plain_text)