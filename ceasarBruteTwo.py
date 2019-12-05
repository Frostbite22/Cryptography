#defining the alphabet
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#encryption function 
def encrypt_ceasar(message,key):
    encrypted_message = ""
    for index,letter in enumerate(message):
        encrypted_message += alphabet[(alphabet.index(message[index])+key)%len(alphabet)] 
    return encrypted_message 

message = "OSFFBDWCJFDAPSGSY"
encrypt = encrypt_ceasar(message,1)
print(encrypt)

#brute for decryption 
def brute_force_decrypt_cesear(encrypted_message): 
    decrypted_message = ""
    decrypted_words = []
    for key in range(1,26):    
        for index, letter in enumerate(encrypted_message):
            decrypted_message += alphabet[(alphabet.index(encrypted_message[index])-key)%len(alphabet)] 
        decrypted_words.append(decrypted_message)
        decrypted_message = ""
    return decrypted_words 

#brute_paire, tries 26*26 combination by incrementing odd numbers altogether and even numbers altogether
def brute_paire(encrypted_message):
    decrypted_message = ""
    decrypted_words = []
    for key1 in range(1,26): 
        for key2 in range(1,26):
            for index, letter in enumerate(encrypted_message):
                if index%2 == 0: 
                    decrypted_message += alphabet[(alphabet.index(encrypted_message[index])-key1)%len(alphabet)] 
                else: 
                    decrypted_message +=  alphabet[(alphabet.index(encrypted_message[index])-key2)%len(alphabet)] 
                       
            decrypted_words.append(decrypted_message)
            decrypted_message = ""
    return decrypted_words 



decrypt = brute_paire(message)
print(decrypt)  




