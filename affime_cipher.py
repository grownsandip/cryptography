dict={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,
      "p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
rev_dict={v:k for k,v in dict.items() }

def encrypt(message,k1,k2):
    c=""
    for i in range(len(message)):
        t=(dict[message[i]]*k1)%26
        c+=rev_dict[(t+k2)%26]
    return c 
     
def find_inv(k1):
    for i in range(0,26):
        if((k1*i)%26==1):
            return i
           
def decrypt(str,k2,k1):
    inv=find_inv(k1)
    p=""
    for i in range(len(str1)):
        t=(dict[str[i]]-k2)%26
        p+=rev_dict[(t*inv)%26]
    return p

message=input("Enter your message:")
k1=int(input("Enter first key:"))
k2=int(input("Enter second key:"))
str1=encrypt(message,k1,k2)
str2=decrypt(str1,k2,k1)
print("The encrypted message is:",str1)
print("The decrypted message:",str2)
