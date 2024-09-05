import string
#print(atoz.replace("j","."))
#the key matrix
def key_matrix_creator(key):
    atoz=string.ascii_lowercase.replace('j','.')
    key=key
    key_mat=[''for i in range(5)]
    i=0
    j=0
    for c in key:
        if c in atoz:
            key_mat[i]+=c
            atoz=atoz.replace(c,'.') #marking each character by . to avoid repetitions in future
            j+=1 #changing columns
            if j>4:
                i+=1 #changing row when column becomes greater than or equal to 5
                j=0
    for c in atoz: #taking rest of characters in a to z and filling the key matrix
        if c!='.':
            key_mat[i]+=c
            j+=1
            if j>4:
                i+=1
                j=0
    return key_mat
 #rule  for making the plaintext into pairs. 
def pairing_plain(plaintext):  
   # plaintext="helpmeenemiesarecoming"
    plaintext_pairs=[]
   # cipher_pairs=[]
    i=0
    while i<len(plaintext):
        a=plaintext[i]
        b=''
        if(i+1)==len(plaintext): # if at second last letter
            b='x' #take a vogus character
        else:
            b=plaintext[i+1] #other wise update b with next letter
        if a!=b:
            plaintext_pairs.append(a+b) #if both letters are not same make pairs and store in list
            i+=2 #move two positions forward
        else:
            plaintext_pairs.append(a+'x')
            i+=1 #move single position
    return plaintext_pairs

def rules(mat,plaintext_pairs): #only one of the three rules will be applied once and not all at once
    ciphertext_pairs=[]
    for pair in plaintext_pairs:#going over all pairs one by one
        
        #if letters appear on the same rows of table than replace with immediate next character
        rule_applied=False
        for row in mat:
            if pair[0] in row and pair[1] in row:
                j0=row.find(pair[0])
                j1=row.find(pair[1])
                
                ciphertextpair=row[(j0+1)%5]+row[(j1+1)%5]
                ciphertext_pairs.append(ciphertextpair)
                rule_applied=True
                
        if rule_applied:
            continue  

        #rule 2 if letters appear on the same column than replce with immediate below letter 
        
        for j in range(5):
            col="".join([mat[i][j]for i in range(5)])
            if pair[0] in col and pair[1] in col:
                i0=col.find(pair[0])
                i1=col.find(pair[1])
                
                ciphertextpair=col[(i0+1)%5]+col[(i1+1)%5]
                ciphertext_pairs.append(ciphertextpair)
                rule_applied=True
                
        if rule_applied:
            continue     
        
        #rule3 :if above rules are not satisfied and than we apply the rectangle rule
        i0=0
        i1=0
        j0=0
        j1=0
        for i in range(5):
            row=mat[i]
            if pair[0] in row:
                i0=i
                j0=row.find(pair[0])
            if pair[1] in row:
                i1=i
                j1=row.find(pair[1])
        ciphertextpair=mat[i0][j1]+mat[i1][j0]
        ciphertext_pairs.append(ciphertextpair)
        
    return ciphertext_pairs
    
    
def main():
    key=input("Enter a key:")
    mat=key_matrix_creator(key)
    print("The key matrix:",mat)
    plaintext=input("Enter plaintext:")
    plaintext_pairs=pairing_plain(plaintext)
    print("The Plaintext pairs:","".join(str(x) for x in plaintext_pairs))
    ciphered=rules(mat,plaintext_pairs)
    print("The ciphered text:","".join(str(x) for x in ciphered))
    
    
if __name__=="__main__":
    main()
    
