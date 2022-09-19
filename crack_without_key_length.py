

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
    ic_table = [10000]
    length = len(cipher_text)

    for key_length in range(1, int(len(cipher_text) / 20)):
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
    possible_lengths = [0]

    # if(int(len(ic_table) / 6) > 40):
    #     key_to_search = 40
    # elif()    

    # key_to_search = 40 if int(len(ic_table) / 6) > 40 else ()

    for i in range(1, int(len(ic_table))):
        index = i
        sum = 0
        count = 0
        while(index < len(ic_table)):
            sum += ic_table[index]
            count += 1
            index += i

        possible_lengths.insert(i, sum / count) 

    best_key_length_ic = 1

    for subject_key_length in range(2, len(ic_table)):
        key_ratio = subject_key_length / best_key_length_ic
        ic_ratio = ic_table[best_key_length_ic] / ic_table[subject_key_length]
        pl_ratio = possible_lengths[best_key_length_ic] / possible_lengths[subject_key_length]
        switch_multiples = ic_ratio > 2.5

        if(
            (key_ratio < 6 and best_key_length_ic != 1 or best_key_length_ic != 2 and subject_key_length % best_key_length_ic != 0)
            or (key_ratio < 8 and best_key_length_ic == 2) 
            or (key_ratio < 14 and best_key_length_ic == 1)):
            if(ic_table[subject_key_length] < ic_table[best_key_length_ic] and subject_key_length % best_key_length_ic != 0):
                best_key_length_ic = subject_key_length
            elif(subject_key_length % best_key_length_ic == 0 and switch_multiples):  
                best_key_length_ic = subject_key_length

    best_key_length_pl = 1

    for subject_key_length in range(2, len(possible_lengths)):
        key_ratio = subject_key_length / best_key_length_pl
        #ic_ratio = ic_table[best_key_length_ic] / ic_table[subject_key_length]
        pl_ratio = possible_lengths[best_key_length_pl] / possible_lengths[subject_key_length]
        switch_multiples = pl_ratio > 2.5

        if(
            (key_ratio < 6 and best_key_length_pl != 1 or best_key_length_pl != 2 and subject_key_length % best_key_length_pl != 0)
            or (key_ratio < 8 and best_key_length_pl == 2) 
            or (key_ratio < 14 and best_key_length_pl == 1)):
            if(possible_lengths[subject_key_length] < possible_lengths[best_key_length_pl] and subject_key_length % best_key_length_pl != 0):
                best_key_length_pl = subject_key_length
            elif(subject_key_length % best_key_length_pl == 0 and switch_multiples):  
                best_key_length_pl = subject_key_length

    return best_key_length_ic

if __name__ == "__main__":
    cipher_text = input("Please provide your ciphertext\n")
    #key_length = int(input("Please provide your key length\n"))
    #cipher_text = "I XI S OPNJ PAK. ... E SI H DOLTBBMH TLM. L AJ WF QULSWRXYLECP LDN. F XWHPPUH MV HARLC HV DFOWWZPC. KOTANAY, T JQOT JGPOTMJ AQ WDH HMNXT JU VEZPZVE, XJV ZV YNW KKKO BVC BHRQWAJ DSZW AFHK IL. T CRN'Q YGJZFKW A AKUPVC ERR FP, SJK YDYEO DSRL, EGRUDD A DHGD D RBOHAJE ERR JAVEJTMH AKZ VKJENUS. YAKEKPR, L AJ APPYPLHLV OMLLCRWIQEGQZ, DTIFFYAAUEKB SL PG NLDOHCQ IWZPNHQE, XJQSHJ (H DM TADH-LOTFAQAV AUZTJH KKL PV MD VUMAJOATSLORO, TQA T ZP SRLWNZEHWILQK). JV, T QHFROW PV NNQSRHL W KZBWOO BJKT DOLTB. PZWA JNX POKTWIWX ZIIH FKA FMGEOOLWUO. VHLI, E MJKPQVTXJV EA, EGRUDD. GB JZTUSB, E UWU'E DAPIWAJ DSN LT FO HNLNHVEIU LDHE H DM JKJPPQXLND EF POTR FAPA TU TJ RSIQA: A WT ADUFBYLHF HDOL XSSNL EGDT F YSJUZS SAV KMP ASD GOZPGNZ MX QOQ YGJZFKWIKC LDLX; H NNLS TAAEDU TEWF WUJNQE QDSP IJ ZOL QDAO P LL RNIU AJQFQLND IQOLWE DNA JG KUP DOSB. XMP ZEHOL, FB A ZVY'S FOKOMHA L CRCQKJ EA TR IRLI KLPED. PY IENAY TR EAA, SWHS EGHN IAL EA STUT BRWJ DZQVE!"
    formatted_cipher = format_cipher(cipher_text)
    key_length_ic = get_key_length(formatted_cipher)
    key_ic = crack_with_key_length(formatted_cipher, key_length_ic)
    plain_text = decrypt(cipher_text, key_ic)
    print(plain_text)
