
from utils import format_cipher

def main():
    cipher_text = "I XI S OPNJ PAK. ... E SI H DOLTBBMH TLM. L AJ WF QULSWRXYLECP LDN. F XWHPPUH MV HARLC HV DFOWWZPC. KOTANAY, T JQOT JGPOTMJ AQ WDH HMNXT JU VEZPZVE, XJV ZV YNW KKKO BVC BHRQWAJ DSZW AFHK IL. T CRN'Q YGJZFKW A AKUPVC ERR FP, SJK YDYEO DSRL, EGRUDD A DHGD D RBOHAJE ERR JAVEJTMH AKZ VKJENUS. YAKEKPR, L AJ APPYPLHLV OMLLCRWIQEGQZ, DTIFFYAAUEKB SL PG NLDOHCQ IWZPNHQE, XJQSHJ (H DM TADH-LOTFAQAV AUZTJH KKL PV MD VUMAJOATSLORO, TQA T ZP SRLWNZEHWILQK). JV, T QHFROW PV NNQSRHL W KZBWOO BJKT DOLTB. PZWA JNX POKTWIWX ZIIH FKA FMGEOOLWUO. VHLI, E MJKPQVTXJV EA, EGRUDD. GB JZTUSB, E UWU'E DAPIWAJ DSN LT FO HNLNHVEIU LDHE H DM JKJPPQXLND EF POTR FAPA TU TJ RSIQA: A WT ADUFBYLHF HDOL XSSNL EGDT F YSJUZS SAV KMP ASD GOZPGNZ MX QOQ YGJZFKWIKC LDLX; H NNLS TAAEDU TEWF WUJNQE QDSP IJ ZOL QDAO P LL RNIU AJQFQLND IQOLWE DNA JG KUP DOSB. XMP ZEHOL, FB A ZVY'S FOKOMHA L CRCQKJ EA TR IRLI KLPED. PY IENAY TR EAA, SWHS EGHN IAL EA STUT BRWJ DZQVE!"
    plain_text = "I am a sick man. ... I am a spiteful man. I am an unattractive man. I believe my liver is diseased. However, I know nothing at all about my disease, and do not know for certain what ails me. I don't consult a doctor for it, and never have, though I have a respect for medicine and doctors. Besides, I am extremely superstitious, sufficiently so to respect medicine, anyway (I am well-educated enough not to be superstitious, but I am superstitious). No, I refuse to consult a doctor from spite. That you probably will not understand. Well, I understand it, though. Of course, I can't explain who it is precisely that I am mortifying in this case by my spite: I am perfectly well aware that I cannot pay out the doctors by not consulting them; I know better than anyone that by all this I am only injuring myself and no one else. But still, if I don't consult a doctor it is from spite. My liver is bad, well then let it hurt even worse!"
    # cipher_text = "QABRZCQABRZCQA"
    # plain_text = "hihihihihihihi"
    
    formatted_cipher = format_cipher(cipher_text)
    formatted_plain = format_cipher(plain_text)
    count = 0
    differences = []
    for i in range(0, len(formatted_cipher) - 3):
        substring = formatted_cipher[i:i+3]
        index = formatted_cipher[i+3:].find(substring)
        if(index >= 0):
            print("Index Left: ", i, "Index Right: ", index+i+3)  
            print("Cipher Left: ", formatted_cipher[i:i+3], "Cipher Right", formatted_cipher[index+i+3:index+i+6])    
            print("Plain Left: ", formatted_plain[i:i+3], "Plain Right: ", formatted_plain[index+i+3:index+i+6])  
            if(formatted_plain[i:i+3] == formatted_plain[index+i+3:index+i+6]):
                differences.append(index + 3)
                count+=1



    print(count)

if __name__ == "__main__":
    main()