alphabet="abcdefghijklmnopqrstuvwxyz"
def decription(c):
    cipher_text=c.lower()
    
    for i in range(26):
        plain_text=''
        for letter in cipher_text:
            if letter in alphabet:
                plain_text+=alphabet[alphabet.find(letter)-i]
            else:
                plain_text+=letter
        print("plain text with key  #%s is: %s" %(i , plain_text))
        
  

decription('GIEWIV GMTLIV HIQS')