def gcd(e,phi):
    while phi:
        e,phi=phi,e%phi
    return e
    
def encrypt(msg,e,n):
    c=(msg**e)%n
    return c
def decrypt(c,d,n):
    p=(c**d)%n
    return p
def cal_e(phi):
    e=2
    while(e<phi):
        if(gcd(e,phi)==1):
            break
        else:
            e=e+1
    return e
def cal_d(phi,e):
    k=2
    d=((k*phi)+1)//e
    return d
    
def main():
    p=int(input("Enter a num1:"))
    q=int(input("Enter a num2:"))
    n=p*q
    phi=(p-1)*(q-1)
    e=cal_e(phi)
    d=cal_d(phi,e)
    msg=int(input("Enter the message:"))
    c=encrypt(msg,e,n)
    print("The encrypted message is:",c)
    decrypted=decrypt(c,d,n)
    print("The decrypted message is:",decrypted)
    
if __name__=="__main__":
    main()