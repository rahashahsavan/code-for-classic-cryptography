

def decription(ciphet_text, key="qmjztgfkpwlsboxncryevhiadu"):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plain_text = ""
    for letter in ciphet_text:
        if letter.lower() in alphabet:
            plain_text += alphabet[key.find(letter.lower())]
        else:
            plain_text += letter

    print(plain_text)

cipher_text = input()
decription(cipher_text)

# key="qmjztgfkpwlsboxncryevhiadu"
# alphabet="abcdefghijklmnopqrstuvwxyz"
# cipher_text=input("what's the cipher_text?")
# plain_text=""
# for letter in cipher_text:
#     if letter in alphabet: 
#         plain_text+=alphabet[key.find(letter)]
#     else:
#         plain_text+=letter
# print(plain_text)
