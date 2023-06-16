# import random
#문자열
# encript="abcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+1234567890"
#문자열 섞기
# print(''.join(random.sample(encript,len(encript))))
# cok="jvOfQH9A2#J3(!XMuNUZIn&c5yKkp4w)zF8YtTD7B@ib1+m*JRg0%qPd^x$slhrCW6EVSoaeL_"
# cov="^PCNTJ#vg0k6ifRZ!u8jsMFab+h72IJQl3U5oL@q(wVOmnSByA1YXrdDp_z)$*c4x9%teKW&EH"
# print({key:value for key,value in zip(cok,cov)})

cripto = {'j': '^', 'v': 'P', 'O': 'C', 'f': 'N', 'Q': 'T', 'H': 'J', '9': '#', 'A': 'v', '2': 'g', '#': '0', 'J': 'y', '3': '6', '(': 'i', '!': 'f', 'X': 'R', 'M': 'Z', 'u': '!', 'N': 'u', 'U': '8', 'Z': 'j', 'I': 's', 'n': 'M', '&': 'F', 'c': 'a', '5': 'b', 'y': '+', 'K': 'h', 'k': '7', 'p': '2', '4': 'I', 'w': 'J', ')': 'Q', 'z': 'l', 'F': '3', '8': 'U', 'Y': '5', 't': 'o', 'T':
'L', 'D': '@', '7': 'q', 'B': '(', '@': 'w', 'i': 'V', 'b': 'O', '1': 'm', '+': 'n', 'm': 'S', '*': 'B', 'R': 'A', 'g': '1', '0': 'Y', '%': 'X', 'q': 'r', 'P': 'd', 'd': 'D', '^': 'p', 'x': '_', '$': 'z', 's': ')', 'l': '$', 'h': '*', 'r': 'c', 'C': '4', 'W': 'x', '6': '9', 'E': '%', 'V': 't', 'S': 'e', 'o': 'K', 'a': 'W', 'e': '&', 'L': 'E', '_': 'H'}

decripto = {value:key for key,value in cripto.items()}

def encript(text,cripto):
    result=""
    for word in text:
        if word in cripto.keys():
            result+=cripto[word]
        else:
            result+=word
    
    return result


def decript(text,decripto):
    result=""
    for word in text:
        if word in decripto.keys():
            result+=decripto[word]
        else:
            result+=word
    return result