

def Encription(m,key):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    cipher=""
    for i in range(len(m)) :
        if m[i] in alphabet:
            cipher+=alphabet[alphabet.find(m[i])+alphabet.find(key[i%(len(key))])]
        else:
            cipher+=m[i]
    print(cipher)
    return(cipher)

def decription(c,key):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    plain_text=""
    for i in range(len(c)):
        if c[i] in alphabet:
            plain_text+=alphabet[alphabet.find(c[i])-alphabet.find(key[i%(len(key))])]
        else:
            plain_text+=c[i]
    print(plain_text)

key="bfhcjd"
m="hello"
cipher="ijsnx"
Encription(m,key)
decription(cipher,key)


