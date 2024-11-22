def calc(a,b,N):
    if(a==1):
        return b;
    return pow(a,b)%N


def main():
    G=int(input("Enter a prime number1:"))
    N=int(input("Enter a prime number2:"))
    x=int(input("Enter a private key for Alice:"))
    y=int(input("Enter a private key for Bob:"))
    a=calc(G,x,N)
    print("a:",a)
    b=calc(G,y,N)
    print("b:",b)
    ka=calc(b,x,N)
    kb=calc(a,y,N)
    print("The secret key for them are:",ka,kb)
    
if __name__=="__main__":
    main()
    