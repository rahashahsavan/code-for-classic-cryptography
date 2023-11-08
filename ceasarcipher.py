alphabet = "abcdefghijklmnopqrstuvwxyz"
def decription(C):
    cipher_text=C.lower()
    plain_text=''
    for letter in cipher_text:
        if letter in alphabet:
            plain_text+=alphabet[(alphabet.find(letter))-3]
        else:
            plain_text+=letter
    print(plain_text)
    return plain_text

def encription(P):
    plain_text=P.lower()
    cipher_text=""
    for letter in plain_text:
        if letter in alphabet:
            cipher_text+=alphabet[alphabet.find(letter)+3]
        else:
            cipher_text+=letter
    print(cipher_text)
    return cipher_text

