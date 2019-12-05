#importing required libraries 
import math 

#defining the alphabet
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#chiffrement affine

message = "GOLD"

def function_encryption(a,b,x,alpha): 
    return ((a*alpha.index(x))+b)%len(alpha) 

def function_encryption_index(a,b,x,alpha): 
    return ((a*x)+b)%len(alpha) 

def chiffrement_affine(message,fn,*args): 
    values = []
    for value in args:
        values.append(value)
    if math.gcd(values[0][0],len(values[0][3])) == 1 and 0<values[0][1]<len(values[0][3]):
        listLetters = []
        for letter in message: 
            listLetters.append(values[0][3][(fn(values[0][0],values[0][1],letter,values[0][3]))])
    return listLetters 

listEncrypyted = chiffrement_affine(message,function_encryption,(9,9,'c',alphabet))
print(listEncrypyted)

####################################################
#the decription part

encrypted_message = "LFEK"

def function_decryption(a1,b,x,alpha): 
    return a1*(alpha.index(x)-b)%26 

def function_decryption_index(a1,b,x,alpha):
    return a1*(x-b)%26

def dechiffrement_affine(encrypted_msg,fn,*args):
    values = []
    for value in args:
        values.append(value)
    if math.gcd(values[0][0],len(values[0][3])) == 1 and 0<values[0][1]<len(values[0][3]):

        decryptList = []
        firstLetterEncrypted = encrypted_msg[0]
        firstLetterDecryptedIndex = 0
        a1 = 0

        while fn(values[0][0],values[0][1],firstLetterDecryptedIndex,values[0][3]) != values[0][3].index(firstLetterEncrypted):
            firstLetterDecryptedIndex += 1

        while function_decryption(a1,values[0][1],firstLetterEncrypted,values[0][3]) != firstLetterDecryptedIndex:
            a1+=1

        for letter in encrypted_msg:        
            decryptList.append(values[0][3][(function_decryption(a1,values[0][1],letter,values[0][3]))])

    return decryptList 


listDecrypyted = dechiffrement_affine(encrypted_message,function_encryption_index,(9,9,0,alphabet))
print(listDecrypyted)