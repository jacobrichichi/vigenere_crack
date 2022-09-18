

from crack_with_key_length import crack_with_key_length
from decrypt import decrypt
from utils import format_cipher

def get_key_length(cipher_text: str):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F',	
                'G', 'H', 'I', 'J', 'K', 'L',	
                'M', 'N', 'O', 'P',	'Q', 'R',	
                'S', 'T', 'U', 'V', 'W', 'X', 
                'Y', 'Z',	
    ]
    ic_english = .0686
    ic_table = [10000, 10000]
    length = len(cipher_text)

    for key_length in range(2, int(len(cipher_text) / 3)):
        ic_average = 0
        for i in range(0, key_length):
            idx = i
            currentGroup = ""
            # get the letters that all share the same cipher key char
            while(idx < len(cipher_text)):
                currentGroup = currentGroup + cipher_text[idx]
                idx += key_length

            ic_sum = 0
            N = len(currentGroup)
            
            # for every letter, calc the # of times it occurs, and add this to the sum
            for letter in alphabet:
                freq = currentGroup.count(letter)
                ic_sum += freq * (freq - 1)

            # calc the IoC for this particular group of char's
            ic_average += ic_sum / (N * (N - 1)) 
        ic_table.insert(key_length, (ic_average / key_length) - ic_english)


    ic_table = list(map(abs, ic_table))
    best_key_length = 2
    possible_lengths = [0, 0]

    for i in range(2, int(len(ic_table) / 4)):
        index = i
        sum = 0
        count = 0
        while(index < len(ic_table)):
            sum += ic_table[index]
            count += 1
            index += i

        possible_lengths.insert(i, sum / count) 

    switched = False


    for subject_key_length in range(3, len(possible_lengths)):
        # the ratio of difference between the two IC's
        ic_ratio = abs(possible_lengths[best_key_length] / possible_lengths[subject_key_length])
        # the difference in their sizes, important for not taking large key sizes over smaller key sizes
        size_ratio = subject_key_length / best_key_length

        # if: 1. the IC of the subject is smaller, 2. the subject is not a multiple AND...
        # 3. either difference in size is not large, or we have not yet switched off the default key length
        should_switch_non_multiples = (possible_lengths[subject_key_length] < possible_lengths[best_key_length]
                                    and subject_key_length % best_key_length != 0
                                    and (size_ratio <= 3 or (not switched and size_ratio < 6)))

        # if the subject is a multiple, but the ratio is large enough to consider it, switch over
        should_switch_multiples = (ic_ratio > 1.4 and (size_ratio <= 3 or (not switched and size_ratio < 6)))

        if(should_switch_non_multiples):
            best_key_length = subject_key_length
            switched = True

        elif(should_switch_multiples):
            best_key_length = subject_key_length
            switched = True

    return best_key_length

if __name__ == "__main__":
    # ciphertext = input("Please provide your ciphertext\n")
    # key_length = int(input("Please provide your key length\n"))
    cipher_text = "XL LJ P LULIZ XEXNHIHSOCN SFBCGZCTVJVS, LKRI S VZCYOV BSQ ZC HRJHWVJXGQ FU S JFDV IFGLXET EXJI TH ZC ODEI GI R LAIV. WGZVKWU CXLWCT CQFLF WYT XHVAAQXH GU MXWZJ DX VLRZ D DPF PRN TH FC ZLJ UAUJI WQKTJLEV S QVXYKSDMUYDGG, KWAV KGMWY XK VF LWOC UAAVS AQ KWW PZCVV FU LKV HMUIDMQUXFJ WPELCXWV, KWSW YT AV TDFVZSWUVS SV KWW UZVZWWJD SIDHHIIQ RW HGPV DFH FG GWYTJ RW IZHZG VDLVZWVGK."
    formatted_cipher = format_cipher(cipher_text)
    key_length = get_key_length(formatted_cipher)
    key = crack_with_key_length(formatted_cipher, key_length)
    plain_text = decrypt(cipher_text, key)
    print(plain_text)
